---
title: "Table.ExpandTableColumn | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
  
