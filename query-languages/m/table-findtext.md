---
title: "Table.FindText | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.FindText

## Syntax

<pre>
Table.FindText(<b>table</b> as table, <b>text</b> as text) as table
</pre>
  
## About  
Returns the rows in the table `table` that contain the text `text`. If the text is not found, an empty table is returned.

## Example 1
Find the rows in the table that contain "Bob".

```powerquery-m
Table.FindText(Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"], [CustomerID = 3, Name = "Paul", Phone = "543-7890"], [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]}), "Bob")
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> </tr> </table>
