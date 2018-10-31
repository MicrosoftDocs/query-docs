---
title: "Table.ReplaceRows | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ReplaceRows

  
## About  
Returns a table where the rows beginning at an offset and continuing for count are replaced with the provided rows.  
  
## Syntax

<pre>
Table.ReplaceRows(table as table, offset as number, count as number, rows as list) as table  
</pre>
  
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
  
```powerquery-m
Table.ReplaceRows(Table.FromRecords({[Column1=1], [Column1=2], [Column1=3], [Column1=4], [Column1=5]}), 1, 3, {[Column1=6], [Column1=7]})  
```  
  
|Column1|  
|-----------|  
|1|  
|6|  
|7|  
|5|  
  
