---
title: "Table.PositionOf | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 9b0756d3-a5eb-47c5-9d72-b97ed364313d
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.PositionOf
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Determines the position or positions of a row within a table.  
  
```  
Table.PositionOf(table as table, row as record, optional occurrence as nullable number, optional equationCriteria as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|row|The row to check for.|  
|optional occurrence|The number for the appropriate occurrence specification.|  
|optional equationCriteria|An optional value that specifies how to control comparison between the rows of the table.|  
  
Occurrence specification  
  
-   Occurrence.First = 0  
  
-   Occurrence.Last = 1  
  
-   Occurrence.All = 2  
  
## <a name="__toc360789683"></a>Remarks  
  
-   Table.PositionOf is similar to List.PositionOf but requires a table as input.  
  
## Examples  
  
```  
Table.PositionOf(   
 Table.FromRecords({  
 [A=1, B=2], [A=3, B=4], [A=1 B=6]}),   
 [A=3,B=4])  
  
 equals 1  
```  
  
```  
Table.PositionOf(  
 Table.FromRecords({  
 [A=1, B=2], [A=3, B=4], [A=1, B=6]}),   
 [A=1],   
 Occurrence.All, "A")  
  
 equals {0, 2}  
```  
