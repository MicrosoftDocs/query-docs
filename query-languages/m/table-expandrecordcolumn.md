---
title: "Table.ExpandRecordColumn | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ExpandRecordColumn

  
## About  
Expands a column of records into columns with each of the values.  
  
```  
Table.ExpandRecordColumn(table as table, column as text, fieldNames as list, optional newColumnNames as nullable list) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify..|  
|column|The column to expand.|  
|fieldNames|List of field names.|  
|optional newColumnNames|Optional list of new column names.|  
  
