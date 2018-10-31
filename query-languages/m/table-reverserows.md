---
title: "Table.ReverseRows | Microsoft Docs"
ms.date: 5/22/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
#Table.ReverseRows

## Syntax

<pre>
Table.ReverseRows(<b>table</b> as table) as table
</pre>

## About
Returns a table with the rows from the input `table` in reverse order.

## Example 1
Reverse the rows in the table.

```powerquery-m
Table.ReverseRows(Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"], [CustomerID = 3, Name = "Paul", Phone = "543-7890"], [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]}))
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>4</td> <td>Ringo</td> <td>232-1550</td> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> </tr> <tr> <td>2</td> <td>Jim</td> <td>987-6543</td> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> </tr> </table>
