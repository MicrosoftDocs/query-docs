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
<code>Table.DuplicateColumn(**table** as table, **columnName** as text,** newColumnName** as text, optional **columnType** as nullable type) as table</code>

## About
Duplicate the column named <code>columnName</code> to the table <code>table</code>. The values and type for the column <code>newColumnName</code> are copied from column <code>columnName</code>.

## Example 1
Duplicate the column "a" to a column named "copied column" in the table <code>({[a = 1, b = 2], [a = 3, b = 4]})</code>.

<code>Table.DuplicateColumn(Table.FromRecords({[a = 1, b = 2], [a = 3, b = 4]}), "a", "copied column")</code>

a  |b  |copied column  
---------|---------|---------
1     |   2      |  1       
3     |   4      |   3      



  
