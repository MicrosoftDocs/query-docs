---
description: "Learn more about: Table.TransformColumns"
title: "Table.TransformColumns | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.TransformColumns

## Syntax

<pre>
Table.TransformColumns(<b>table</b> as table, <b>transformOperations</b> as list, optional <b>defaultTransformation</b> as nullable function, optional <b>missingField</b> as nullable number) as table
</pre>
  
## About

Returns a table from the input `table` by applying the transform operation to the column specified in the parameter `transformOperations` (where format is { column name, transformation }). If the column doesn't exist, an exception is thrown unless the optional parameter `defaultTransformation` specifies an alternative (eg. `MissingField.UseNull` or `MissingField.Ignore`).

## Example 1
Transform the number values in column [A] to number values.

**Usage**

```powerquery-m
Table.TransformColumns(
    Table.FromRecords({
        [A = "1", B = 2],
        [A = "5", B = 10]
    }),
    {"A", Number.FromText}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [A = 1, B = 2],
    [A = 5, B = 10]
})
```

## Example 2

Transform the number values in missing column [X] to text values, ignoring columns which don't exist.

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

Transform the number values in missing column [X] to text values, defaulting to null on columns which don't exist.

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

Transform the number values in missing column [X] to text values, giving an error on columns which don't exist.

**Usage**

```powerquery-m
Table.TransformColumns(
    Table.FromRecords({
        [A = "1", B = 2], 
        [A = "5", B = 10]
    }),
    {"X", Number.FromText}
)
```

**Output**

`[Expression.Error] The column 'X' of the table wasn't found.`
