---
title: "Table.ReplaceRows | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 878e5c43-3661-4afc-905f-c8769f79fcbb
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.ReplaceRows
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table where the rows beginning at an offset and continuing for count are replaced with the provided rows.  
  
```  
Table.ReplaceRows(table as table, offset as number, count as number, rows as list) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|offset|The beginning row index.|  
|count|The number of rows to replace.|  
|rows|The List of replacement rows.|  
  
## <a name="__toc360789522"></a>Remarks  
  
-   Table.ReplaceRows is similar to List.ReplaceRange but requires a table as input.  
  
## Example  
  
```  
Table.ReplaceRows(Table.FromRecords({[Column1=1], [Column1=2], [Column1=3], [Column1=4], [Column1=5]}), 1, 3, {[Column1=6], [Column1=7]})  
```  
  
|Column1|  
|-----------|  
|1|  
|6|  
|7|  
|5|  
  
