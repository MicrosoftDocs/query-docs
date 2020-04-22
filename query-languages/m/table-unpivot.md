---
title: "Table.Unpivot | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.Unpivot

## Syntax

<pre>
Table.Unpivot(<b>table</b> as table, <b>pivotColumns</b> as list, <b>attributeColumn</b> as text, <b>valueColumn</b> as text) as table 
</pre>
  
## About  
Translates a set of columns in a table into attribute-value pairs, combined with the rest of the values in each row.

## Example 1
Take the columns "a", "b", and "c" in the table `({[ key = "x", a = 1, b = null, c = 3 ], [ key = "y", a = 2, b = 4, c = null ]})` and unpivot them into attribute-value pairs.

```powerquery-m
Table.Unpivot(
    Table.FromRecords({
        [key = "x", a = 1, b = null, c = 3], 
        [key = "y", a = 2, b = 4, c = null]
    }),
    {"a", "b", "c"}, 
    "attribute", 
    "value"
)
```

<table> <tr> <th>key</th> <th>attribute</th> <th>value</th> </tr> <tr> <td>x</td> <td>a</td> <td>1</td> </tr> <tr> <td>x</td> <td>c</td> <td>3</td> </tr> <tr> <td>y</td> <td>a</td> <td>2</td> </tr> <tr> <td>y</td> <td>b</td> <td>4</td> </tr> </table>
