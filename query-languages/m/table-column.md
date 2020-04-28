---
title: "Table.Column | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.Column

## Syntax

<pre>
Table.Column(<b>table</b> as table, <b>column</b> as text) as list
</pre>
  
## About  
Returns the column of data specified by `column` from the table `table` as a list.

## Example 1
Returns the values from the [Name] column in the table.

```powerquery-m
Table.Column(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    "Name"
)
```

<table> <tr><td>Bob</td></tr> <tr><td>Jim</td></tr> <tr><td>Paul</td></tr> <tr><td>Ringo</td></tr> </table>
