---
description: "Learn more about: Table.TransformColumns"
title: "Table.TransformColumns | Microsoft Docs"
ms.date: 4/23/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

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

```powerquery-m
Table.TransformColumns(
    Table.FromRecords({
        [A = "1", B = 2],
        [A = "5", B = 10]
    }),
    {"A", Number.FromText}
)
```

<table> <tr> <th>A</th> <th>B</th> </tr> <tr> <td>1</td> <td>2</td> </tr> <tr> <td>5</td> <td>10</td> </tr> </table>

## Example 2
Transform the number values in missing column [X] to text values, ignoring columns which don't exist.

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

<table> <tr> <th>A</th> <th>B</th> </tr> <tr> <td>1</td> <td>2</td> </tr> <tr> <td>5</td> <td>10</td> </tr> </table>

## Example 3
Transform the number values in missing column [X] to text values, defaulting to null on columns which don't exist.

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

<table> <tr> <th>A</th> <th>B</th> <th>X</th> </tr> <tr> <td>1</td> <td>2</td> <td></td> </tr> <tr> <td>5</td> <td>10</td> <td></td> </tr> </table>

## Example 4
Transform the number values in missing column [X] to text values, giving an error on columns which don't exist.

```powerquery-m
Table.TransformColumns(
    Table.FromRecords({
        [A = "1", B = 2], 
        [A = "5", B = 10]
    }),
    {"X", Number.FromText}
)
```

`[Expression.Error] The column 'X' of the table wasn't found.`
