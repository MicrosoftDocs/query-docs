---
title: "Table.UnpivotOtherColumns | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.UnpivotOtherColumns

## Syntax

<pre>
Table.UnpivotOtherColumns(<b>table</b> as table, <b>pivotColumns</b> as list, <b>attributeColumn</b> as text, <b>valueColumn</b> as text) as table 
</pre>
  
## About  
Translates all columns other than a specified set into attribute-value pairs, combined with the rest of the values in each row.

## Example 1
Translates all columns other than a specified set into attribute-value pairs, combined with the rest of the values in each row.

```powerquery-m
Table.UnpivotOtherColumns(
    Table.FromRecords({
        [key = "key1", attribute1 = 1, attribute2 = 2, attribute3 = 3],
        [key = "key2", attribute1 = 4, attribute2 = 5, attribute3 = 6]  
    }),
    {"key"},
    "column1",
    "column2"
)
```

<table> <tr> <th>key</th> <th>column1</th> <th>column2</th> </tr> <tr> <td>key1</td> <td>attribute1</td> <td>1</td> </tr> <tr> <td>key1</td> <td>attribute2</td> <td>2</td> </tr> <tr> <td>key1</td> <td>attribute3</td> <td>3</td> </tr> <tr> <td>key2</td> <td>attribute1</td> <td>4</td> </tr> <tr> <td>key2</td> <td>attribute2</td> <td>5</td> </tr> <tr> <td>key2</td> <td>attribute3</td> <td>6</td> </tr> </table>
