---
title: "Table.SingleRow | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.SingleRow

## Syntax

<pre>
Table.SingleRow(<b>table</b> as table) as record  
</pre> 
  
## About  
Returns the single row in the one row `table`. If the `table` has more than one row, an exception is thrown.

## Example 1
Return the single row in the table.

```powerquery-m
Table.SingleRow(Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}))
```

<table> <tr> <th>CustomerID</th> <td>1</td> </tr> <tr> <th>Name</th> <td>Bob</td> </tr> <tr> <th>Phone</th> <td>123-4567</td> </tr> </table>
