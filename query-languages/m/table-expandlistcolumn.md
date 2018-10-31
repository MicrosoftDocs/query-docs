---
title: "Table.ExpandListColumn | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ExpandListColumn

  
## About  
Given a column of lists in a table, create a copy of a row for each value in its list.  
  
## Syntax

<pre>
Table.ExpandListColumn(table as table, column as text) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|column|The column to expand.|  
  
## Example  
  
```powerquery-m
Table.ExpandListColumn(  
  
    Table.FromRecords(  
  
    {  
  
    [Name= {"Bob", "Jim", "Paul"}, Discount = .15]  
  
}), "Name")  
```  
  
|Name|Discount|  
|--------|------------|  
|Bob|0.15|  
|Jim|0.15|  
|Paul|0.15|  
  
