---
title: "Table.CombineColumns | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 4870f5ad-9837-42ef-928b-28cbb954d6d8
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.CombineColumns

  
## About  
The inverse of Table.SplitColumns,  Table.CombineColumns merge columns using a combiner function to produce a new column.  
  
```  
Table.CombineColumns(table as table, sourceColumns as list, combiner as function, column as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|sourceColumns|The list of columns to combine.|  
|combiner|The table combiner function.|  
|column|The column to modify.|  
  
## Example  
  
```  
Table.CombineColumns(Table.FromRecords(  
  
{  
  
[A.1 = "a", A.2 = "b", B = "c" ],  
  
[A.1 = "b", A.2 = "c", B = "d"]},  
  
{"A.1","A.2","B"}),{"A.1", "A.2"},Combiner.CombineTextByDelimiter(","),"Merged")  
```  
  
|Merged|B|  
|----------|-----|  
|a,b|c|  
|b,c|d|  
  
