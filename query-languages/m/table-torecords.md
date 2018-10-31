---
title: "Table.ToRecords | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ToRecords

  
## About  
Returns a list of records from an input table.  
  
## Syntax

<pre>
Table.ToRecords(table as table) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to convert.|  
  
## Example  
  
```powerquery-m
Table.ToRecords(Table.FromRows({{"1", "2"}},{"a", "b"})) equals {[a = "1", b = "2"]}  
```  
