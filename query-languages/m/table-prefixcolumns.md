---
title: "Table.PrefixColumns | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.PrefixColumns

  
## About  
Returns a table where the columns have all been prefixed with a text value.  
  
## Syntax

<pre>
Table.PrefixColumns(table as table, prefix as text) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|prefix|The prefix to add to every text value.|  
  
## Example  
  
```powerquery-m
Table.PrefixColumns(Table.FromRecords(  
  
{  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"]  
  
}  
  
), "MyTable")  
```  
  
|MyTable.CustomerID|MyTable.Name|MyTable.Phone|  
|----------------------|----------------|-----------------|  
|1|Bob|123-4567|  
  
