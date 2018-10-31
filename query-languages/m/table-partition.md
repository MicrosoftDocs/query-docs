---
title: "Table.Partition | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Partition

  
## About  
Partitions the table into a list of groups number of tables, based on the value of the column of each row and a hash function. The hash function is applied to the value of the column of a row to obtain a hash value for the row.  The hash value modulo groups determines in which of the returned tables the row will be placed.  
  
## Syntax

<pre>  
Table.Partition ( table as table, column as text, groups as number, hash as function) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|column|The column to apply hash to.|  
|groups|The number of groups to make.|  
|hash|The hash function to apply.|  
  
## Example  
  
```powerquery-m
Table.Partition(Table.FromRecords({[A=1], [A=2], [A=3], [A=4], [A=5], [A=6]}),"A", 2, each _)  
  
equals Table.FromRecords({[A=2], [A=4], [A=6]})  
```  
