---
description: "Learn more about: Table.Split"
title: "Table.Split | Microsoft Docs"
ms.date: 4/22/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.Split

## Syntax

<pre>
Table.Split(<b>table</b> as table, <b>pageSize</b> as number) as list
</pre>

## About

Splits <code>table</code> into a list of tables where the first element of the list is a table containing the first <code>pageSize</code> rows from the source table, the next element of the list is a table containing the next <code>pageSize</code> rows from the source table, etc.

## Example 1
Split a table of five records into tables with two records each.

```powerquery-m
let 
    Customers = Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Cristina", Phone = "232-1550"],
        [CustomerID = 5, Name = "Anita", Phone = "530-1459"]
    })
in
    Table.Split(Customers, 2)
```  

<table> <tr><td>[Table]</td></tr> <tr><td>[Table]</td></tr> <tr><td>[Table]</td></tr> </table>
