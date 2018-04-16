---
title: "Table.PositionOf | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.PositionOf

  
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
