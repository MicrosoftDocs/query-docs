---
title: "Table.ToRows | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ToRows

  
## About  
Returns a nested list of row values from an input table.  
  
## Syntax

<pre>
Table.ToRows(table as table) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
  
## Example  
  
```powerquery-m
let  
  
    Source = Table.ToRows(Table.FromRecords({  
  
    [CustomerID =1, Name ="Bob", Phone = "123-4567"],  
  
    [CustomerID =2, Name ="Jim", Phone = "987-6543"],  
  
    [CustomerID =3, Name ="Paul", Phone = "543-7890"]  
  
}))  
  
in  
  
    Source  
  
equals  
  
{  
  
    {1, "Bob", "123-4567"},  
  
    {2, "Jim", "987-6543"},  
  
    {3,  "Paul", "543-7890"}  
  
}  
```  
