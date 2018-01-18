---
title: "Table.CombineColumns | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
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
manager: "erikre"
---
# Table.CombineColumns
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
  
