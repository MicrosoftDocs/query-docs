---
title: "Table.SplitColumn | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.SplitColumn

  
## About  
Returns a new set of columns from a single column applying a splitter function to each value.  
  
## Syntax

<pre> 
Table.SplitColumn(table as table, sourceColumn as text, splitter as function, optional columnNamesOrNumber as any, optional default as any, optional extraValues as any) as record  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|sourceColumn|The column to modify.|  
|splitter||  
|columnNamesOrNumber|List of column names that do not conflict with columns from the target table.|  
|optional default|Default value.|  
|extraValues|Handles of extra values or overflow values.|  
  
## Example  
  
```powerquery-m
let  
  
    Customers = Table.FromRecords({  
  
          [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
          [CustomerID = 2, Name = "Jim", Phone = "987-6543"],  
  
          [CustomerID = 3, Name = "Paul", Phone = "543-7890"],  
  
          [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
})  
  
in  
  
    Table.SplitColumn(Customers,"Name",Splitter.SplitTextByDelimiter("i"),2)  
```  
  
|CustomerID|Name.1|Name.2|Phone|  
|--------------|----------|----------|---------|  
|1|Bob||123-4567|  
|2|J|m|987-6543|  
|3|Paul||543-7890|  
|4|R|ngo|232-1550|  
  
