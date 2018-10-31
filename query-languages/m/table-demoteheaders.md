---
title: "Table.DemoteHeaders | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.DemoteHeaders

  
## About  
Demotes the header row down into the first row of a table.  
  
## Syntax

<pre>
Table.DemoteHeaders(table as table) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
  
## Example  
  
```powerquery-m
Table.DemoteHeaders(Table.FromRecords(  
  
{  
  
    [CustomerID=1, Name="Bob", Phone = "123-4567" ]  
  
}  
  
))  
```  
  
|Column1|Column2|Column3|  
|-----------|-----------|-----------|  
|CustomerID|Name|Phone|  
|1|Bob|123-4567|  
  
