---
description: "Learn more about: Table.TransformColumns"
title: "Table.TransformColumns"
ms.subservice: m-source
---
# Table.TransformColumns

## Syntax

<pre>
Table.TransformColumns(<b>table</b> as table, <b>transformOperations</b> as list, optional <b>defaultTransformation</b> as nullable function, optional <b>missingField</b> as nullable number) as table
</pre>
  
## About

Transforms `table` by applying each column operation listed in `transformOperations` (where the format is { column name, transformation } or { column name, transformation, new column type }). If a `defaultTransformation` is specified, it will be applied to all columns not listed in `transformOperations`. If a column listed in `transformOperations` doesn't exist, an exception is thrown unless the optional parameter `missingField` specifies an alternative (for example, [MissingField.UseNull](missingfield-type.md) or [MissingField.Ignore](missingfield-type.md)).

## Example 1

Convert the text values in column [A] to number values, and the number values in column [B] to text values.

**Usage**

```powerquery-m
Table.TransformColumns(
    Table.FromRecords({
        [A = "1", B = 2],
        [A = "5", B = 10]
    }),
    {
        {"A", Number.FromText},
        {"B", Text.From}
    }
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [A = 1, B = "2"],
    [A = 5, B = "10"]
})
```

## Example 2

Convert the number values in missing column [X] to text values, ignoring columns which don't exist.

**Usage**

```powerquery-m
Table.TransformColumns(
    Table.FromRecords({
        [A = "1", B = 2],
        [A = "5", B = 10]
    }),
    {"X", Number.FromText},
    null,
    MissingField.Ignore
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [A = "1", B = 2],
    [A = "5", B = 10]
})
```

## Example 3

Convert the number values in missing column [X] to text values, defaulting to null on columns which don't exist.

**Usage**

```powerquery-m
Table.TransformColumns(
    Table.FromRecords({
        [A = "1", B = 2],
        [A = "5", B = 10]
    }),
    {"X", Number.FromText},
    null,
    MissingField.UseNull
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [A = "1", B = 2, X = null],
    [A = "5", B = 10, X = null]
})
```

## Example 4

Increment the number values in column [B] and convert them to text values, and convert all other columns to numbers.

**Usage**

```powerquery-m
Table.TransformColumns(
    Table.FromRecords({
        [A = "1", B = 2],
        [A = "5", B = 10]
    }),
    {"B", each Text.From(_ + 1), type text},
    Number.FromText
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [A = 1, B = "3"],
    [A = 5, B = "11"]
})
```
