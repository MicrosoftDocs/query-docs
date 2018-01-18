---
title: "Table.Partition | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: bca04b5c-ab69-4815-8faa-07c3af98775c
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.Partition
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Partitions the table into a list of groups number of tables, based on the value of the column of each row and a hash function. The hash function is applied to the value of the column of a row to obtain a hash value for the row.  The hash value modulo groups determines in which of the returned tables the row will be placed.  
  
```  
Table.Partition ( table as table, column as text, groups as number, hash as function) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|column|The column to apply hash to.|  
|groups|The number of groups to make.|  
|hash|The hash function to apply.|  
  
## Example  
  
```  
Table.Partition(Table.FromRecords({[A=1], [A=2], [A=3], [A=4], [A=5], [A=6]}),"A", 2, each _)  
  
equals Table.FromRecords({[A=2], [A=4], [A=6]})  
```  
