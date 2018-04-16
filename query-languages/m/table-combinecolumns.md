---
title: "Table.CombineColumns | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
  
