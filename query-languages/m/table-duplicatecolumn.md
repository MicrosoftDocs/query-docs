---
title: "Table.DuplicateColumn | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.DuplicateColumn

## Syntax

<pre>
Table.DuplicateColumn(**table** as table, **columnName** as text,** newColumnName** as text, optional **columnType** as nullable type) as table
</pre>

## About
Duplicate the column named `columnName` to the table `table`. The values and type for the column `newColumnName` are copied from column `columnName`.

## Example
Duplicate the column "a" to a column named "copied column" in the table `({[a = 1, b = 2], [a = 3, b = 4]})`.

```powerquery-m
Table.DuplicateColumn(Table.FromRecords({[a = 1, b = 2], [a = 3, b = 4]}), "a", "copied column")```

a  |b  |copied column  
---------|---------|---------
1     |   2      |  1       
3     |   4      |   3      



  
