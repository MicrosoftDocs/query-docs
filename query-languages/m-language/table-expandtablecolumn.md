---
title: "Table.ExpandTableColumn | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 54903f25-75a2-4a44-a9a3-52a9d895ee98
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.ExpandTableColumn

  
## About  
Expands a column of records or a column of tables into multiple columns in the containing table.  
  
```  
Table.ExpandTableColumn(table as table, column as text, columnNames as list, optional newColumnNames as nullable list) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|column|The column to expand.|  
|columnNames|List of column names.|  
|optional newColumnNames|Optional list of new column names.|  
  
