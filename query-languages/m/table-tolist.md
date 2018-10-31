---
title: "Table.ToList | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ToList

  
## About  
Returns a table into a list by applying the specified combining function to each row of values in a table.  
  
## Syntax

<pre> 
Table.ToList(table as table,  optional combiner as nullable function) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to convert.|  
|optional combiner|The combiner function is applied to each row in the table to produce a single value for the row.|  
  
## <a name="__goback"></a>Example  
  
```powerquery-m
let  
  
    input = Table.FromRows({  
  
    {Number.ToText(1),"Bob", "123-4567" },  
  
    {Number.ToText(2), "Jim", "987-6543" },  
  
    {Number.ToText(3), "Paul", "543-7890" }})  
  
in  
  
    Table.ToList(input, Combiner.CombineTextByDelimiter(","))  
  
equals  
  
{  
  
    "1,Bob,123-4567",  
  
    "2,Jim,987-6543",  
  
    "3,Paul,543-7890"  
  
}  
```  
