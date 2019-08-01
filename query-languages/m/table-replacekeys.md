---
title: "Table.ReplaceKeys | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ReplaceKeys

## Syntax

<pre>
Table.ReplaceKeys(<b>table</b> as table, <b>keys</b> as list) as table 
</pre>
  
## About  
Returns a new table with new key information set in the **keys** argument.  

  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|Table to modify.|  
|keys|A list with two fields: Columns and Primary. Columns is a list of columns that are keys. Primary is a primary key.|  
  
## Example  
  
```powerquery-m
Table.ReplaceKeys(Table.FromRecords({[A={[B=1], [B=2]}, C=1]}), {[Columns = {"C"}, Primary = true]})  
```  
