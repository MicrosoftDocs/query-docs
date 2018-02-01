---
title: "Table.ExpandRecordColumn | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c1675e36-4ded-483d-95af-97b04603f67e
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
  
