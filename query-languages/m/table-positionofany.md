---
title: "Table.PositionOfAny | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.PositionOfAny

  
## About  
Determines the position or positions of any of the specified rows within the table.  
  
## Syntax

<pre> 
Table.PositionOfAny(table as table, rows as list, optional occurrence as nullable number, optional equationCriteria as any) as any  
</pre>
  
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
  
```powerquery-m  
Table.PositionOfAny(      
Table.FromRecords({[A=1, B=2],[A=3, B=4],[A=1, B=6]}),      
{[A=2, B=6],[A=3, B=4]})   
equals 1  
```  
  
```powerquery-m
Table.PositionOfAny(      
Table.FromRecords({[A=1, B=2],[A=3, B=4],[A=1, B=6]}),      
{[A=3, B=7],[A=1, B=6]},      
Occurrence.All, "A")   
equals {0, 1, 2}  
```  
