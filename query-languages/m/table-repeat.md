---
title: "Table.Repeat | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Repeat

  
## About  
Returns a table containing the rows of the table repeated the **count** number of times.  
  
## Syntax

<pre>
Table.Repeat(table as table, count as number) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|count|The number of times to repeat the table.|  
  
## Example  
  
```powerquery-m
Table.Repeat(Table.FromRecords({[Column1=1], [Column1=2]}), 2)  
```  
  
|Column1|  
|-----------|  
|1|  
|2|  
|1|  
|2|  
  
