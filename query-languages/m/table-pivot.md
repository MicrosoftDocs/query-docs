---
description: "Learn more about: Table.Pivot"
title: "Table.Pivot | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.Pivot

## Syntax

<pre>
Table.Pivot(<b>table</b> as table, <b>pivotValues</b> as list, <b>attributeColumn</b> as text, <b>valueColumn</b> as text, optional <b>aggregationFunction</b> as nullable function) as table
</pre>
  
## About  
Given a pair of columns representing attribute-value pairs, rotates the data in the attribute column into a column headings.

## Example 1
Take the values "a", "b", and "c" in the attribute column of table `({ [ key = "x", attribute = "a", value = 1 ], [ key = "x", attribute = "c", value = 3 ], [ key = "y", attribute = "a", value = 2 ], [ key = "y", attribute = "b", value = 4 ] })` and pivot them into their own column.

```powerquery-m
Table.Pivot(
    Table.FromRecords({
        [key = "x", attribute = "a", value = 1],
        [key = "x", attribute = "c", value = 3],
        [key = "y", attribute = "a", value = 2],
        [key = "y", attribute = "b", value = 4]
    }),
    {"a", "b", "c"},
    "attribute",
    "value"
)
```

<table> <tr> <th>key</th> <th>a</th> <th>b</th> <th>c</th> </tr> <tr> <td>x</td> <td>1</td> <td></td> <td>3</td> </tr> <tr> <td>y</td> <td>2</td> <td>4</td> <td></td> </tr> </table>

## Example 2
Take the values "a", "b", and "c" in the attribute column of table `({ [ key = "x", attribute = "a", value = 1 ], [ key = "x", attribute = "c", value = 3 ], [ key = "x", attribute = "c", value = 5 ], [ key = "y", attribute = "a", value = 2 ], [ key = "y", attribute = "b", value = 4 ] })` and pivot them into their own column. The attribute "c" for key "x" has multiple values associated with it, so use the function List.Max to resolve the conflict.

```powerquery-m
Table.Pivot(
    Table.FromRecords({
        [key = "x", attribute = "a", value = 1],
        [key = "x", attribute = "c", value = 3],
        [key = "x", attribute = "c", value = 5],
        [key = "y", attribute = "a", value = 2],
        [key = "y", attribute = "b", value = 4]
    }),
    {"a", "b", "c"},
    "attribute",
    "value",
    List.Max
)
```

<table> <tr> <th>key</th> <th>a</th> <th>b</th> <th>c</th> </tr> <tr> <td>x</td> <td>1</td> <td></td> <td>5</td> </tr> <tr> <td>y</td> <td>2</td> <td>4</td> <td></td> </tr> </table>
