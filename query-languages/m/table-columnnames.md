---
title: "Table.ColumnNames | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.ColumnNames

## Syntax

<pre>
Table.ColumnNames(<b>table</b> as table) as list
</pre>
  
## About  
Returns the column names in the table `table` as a list of text.

## Example 1
Find the column names of the table.

```powerquery-m
Table.ColumnNames( 
    Table.FromRecords({ 
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"], 
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"], 
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"], 
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"] 
    }) 
)
```

<table> <tr><td>CustomerID</td></tr> <tr><td>Name</td></tr> <tr><td>Phone</td></tr> </table>
