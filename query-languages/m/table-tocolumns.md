---
title: "Table.ToColumns | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ToColumns

  
## About  
Returns a list of nested lists each representing a column of values in the input table.  
  
## Syntax

<pre>
Table.ToColumns(table as table) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to convert.|  
  
## Example  
  
```powerquery-m 
let  
  
    Source = Table.ToColumns(Table.FromRecords(  
  
{  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"]  
  
}))  
  
in  
  
    Source  
  
equals  
  
{  
  
    {1, 2},  
  
    {"Bob",  "Jim"},  
  
    { "123-4567", "987-6543"}  
  
}  
```  
