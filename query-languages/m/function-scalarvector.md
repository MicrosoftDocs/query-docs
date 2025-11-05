---
description: "Learn more about: Function.ScalarVector"
title: "Function.ScalarVector"
ms.subservice: m-source
---
# Function.ScalarVector

## Syntax

<pre>
Function.ScalarVector(<b>scalarFunctionType</b> as type, <b>vectorFunction</b> as function) as function
</pre>

## About

Returns a scalar function of type `scalarFunctionType` that invokes `vectorFunction` with a single row of arguments and returns its single output. Additionally, when the scalar function is repeatedly applied for each row of a table of inputs, such as in Table.AddColumn, instead `vectorFunction` will be applied once for all inputs.

`vectorFunction` will be passed a table whose columns match in name and position the parameters of `scalarFunctionType`. Each row of this table contains the arguments for one call to the scalar function, with the columns corresponding to the parameters of `scalarFunctionType`.

`vectorFunction` must return a list of the same length as the input table, whose item at each position must be the same result as evaluating the scalar function on the input row of the same position.

The input table is expected to be streamed in, so `vectorFunction` is expected to stream its output as input comes in, only working with one chunk of input at a time. In particular, `vectorFunction` must not enumerate its input table more than once.

## Example 1

Multiply two columns of the input table by processing the inputs in batches of 100.

**Usage**

```powerquery-m
let
    Compute.ScoreScalar = (left, right) => left * right,
    // When Function.ScalarVector batching kicks in, we'll receive all
    // of the inputs for the entire table here at once.
    Compute.ScoreVector = (input) => let
        chunks = Table.Split(input, 100),
        scoreChunk = (chunk) => Table.TransformRows(chunk, each Compute.ScoreScalar([left], [right]))
      in
        List.Combine(List.Transform(chunks, scoreChunk)),
    Compute.Score = Function.ScalarVector(
        type function (left as number, right as number) as number, 
        Compute.ScoreVector
    ),
    Final = Table.AddColumn(
        Table.FromRecords({
            [a = 1, b = 2],
            [a = 3, b = 4]
        }),
        "Result",
        each Compute.Score([a], [b])
    )
in
    Final
```

**Output**

```powerquery-m

Table.FromRecords({
    [a = 1, b = 2, Result = 2],
    [a = 3, b = 4, Result = 12]
})
```

## Example 2

Compute test scores in batches of two, and populate a batch ID field that can be used to verify that batching is working as expected.

**Usage**

```powerquery-m
let
  _GradeTest = (right, total) => Number.Round(right / total, 2),
  _GradeTests = (inputs as table) as list => let
    batches = Table.Split(inputs, 2),
    gradeBatch = (batch as table) as list =>
      let
        batchId = Text.NewGuid()
      in
        Table.TransformRows(batch, each [Grade = _GradeTest([right], [total]), BatchId = batchId])
  in
    List.Combine(List.Transform(batches, gradeBatch)),
  GradeTest = Function.ScalarVector(type function (right as number, total as number) as number, _GradeTests),
  Tests = #table(type table [Test Name = text, Right = number, Total = number],
    {
      {"Quiz 1", 3, 4},
      {"Test 1", 17, 22},
      {"Quiz 2", 10, 10}
    }),
  // To break batching, replace [Right] with {[Right]}{0}.
  TestsWithGrades = Table.AddColumn(Tests, "Grade Info", each GradeTest([Right], [Total]), type record),
  // To verify batching, also expand BatchId.
  Final = Table.ExpandRecordColumn(TestsWithGrades, "Grade Info", {"Grade"})
in
  Final
```

**Output**

```powerquery-m
#table(
    type table [Test Name = text, Right = number, Total = number, Grade = number],
    {
      {"Quiz 1", 3, 4, 0.75},
      {"Test 1", 17, 22, 0.77},
      {"Quiz 2", 10, 10, 1}
    }
)
```
