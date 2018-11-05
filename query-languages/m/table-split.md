---
title: "Table.Split | Microsoft Docs"
ms.date: 5/22/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Split

## Syntax

<pre>
Table.Split(<b>table</b> as table, <b>pageSize</b> as number) as list
</pre>

## About
Splits `table` into a list of tables where the first element of the list is a table containing the first `pageSize` rows from the source table, the next element of the list is a table containing the next `pageSize` rows from the source table, etc.

## Example 1
Split a table of five records into tables with two records each.

```powerquery-m
let Customers = Table.FromRecords({ [CustomerID = 1, Name = "Bob", Phone = "123-4567"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"], [CustomerID = 3, Name = "Paul", Phone = "543-7890"], [CustomerID = 4, Name = "Cristina", Phone = "232-1550"], [CustomerID = 5, Name = "Anita", Phone = "530-1459"] }) in Table.Split(Customers, 2)
```

<table> <tr><td>[Table]</td></tr> <tr><td>[Table]</td></tr> <tr><td>[Table]</td></tr> </table>