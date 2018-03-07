---
title: "Table.DuplicateColumn | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b8d61603-eea9-4910-b431-1ff4c07de7d5
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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



  
