---
title: "Table.PositionOfAny | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3ecb3407-de28-4026-aa18-5a842a98fcaa
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.PositionOfAny

  
## About  
Determines the position or positions of any of the specified rows within the table.  
  
```  
Table.PositionOfAny(table as table, rows as list, optional occurrence as nullable number, optional equationCriteria as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|rows|The List of rows to check for.|  
|optional occurrence|The number for the appropriate occurrence specification.|  
|optional equationCriteria|An optional value that specifies how to control comparison between the rows of the table.|  
  
Occurrence specification  
  
-   Occurrence.First  = 0  
  
-   Occurrence.Last   = 1  
  
-   Occurrence.All    = 2  
  
## <a name="__toc360793255"></a>Remarks  
  
-   Table.PositionOfAny is similar to List.PositionOfAny but requires a table as input.  
  
## Examples  
  
```  
Table.PositionOfAny(      
Table.FromRecords({[A=1, B=2],[A=3, B=4],[A=1, B=6]}),      
{[A=2, B=6],[A=3, B=4]})   
equals 1  
```  
  
```  
Table.PositionOfAny(      
Table.FromRecords({[A=1, B=2],[A=3, B=4],[A=1, B=6]}),      
{[A=3, B=7],[A=1, B=6]},      
Occurrence.All, "A")   
equals {0, 1, 2}  
```  
