---
title: "Table.ReplaceMatchingRows | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ReplaceMatchingRows

  
## About  
Replaces specific rows from a table with the new rows.  
  
## Syntax

<pre>
Table.ReplaceMatchingRows(table as table, replacements as list, optional equationCriteria as any) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|replacements|The List of replacement rows.|  
|optional equationCriteria|An optional value that specifies how to control comparison between the rows of the table.|  
  
## <a name="__toc360789696"></a>Remarks  
  
-   Table.ReplaceMatchingRows is similar to List.ReplaceMatchingRows but requires a table as input.  
  
-   The new rows must be compatible with the type of the table .  
  
## Example  
  
```powerquery-m
Table.ReplaceMatchingRows(  
  
Table.FromRecords(  
  
{  
  
 [Column1 = 1, Column2 = 2],  
  
 [Column1 = 2, Column2 = 3],  
  
 [Column1 = 3, Column2 = 4],  
  
 [Column1 = 1, Column2 = 2]  
  
}),{  
  
{[Column1 = 1, Column2 = 2],  
  
 [Column1 = -1, Column2 = -2]},  
  
{[Column1  = 2, Column2 = 3],  
  
 [Column1  = -2, Column2 = -3]} })  
```  
  
|Column1|Column2|  
|-----------|-----------|  
|-1|-2|  
|-2|-3|  
|3|4|  
|-1|-2|  
  
