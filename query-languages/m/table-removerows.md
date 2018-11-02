---
title: "Table.RemoveRows | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.RemoveRows

  
## About  
Returns a table with the specified number of rows removed from the table starting at an offset.  
## Syntax

<pre>
Table.RemoveRows( table as table, offset as number, optional count as nullable number) as table </pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to remove rows from.|  
|offset|The row to start removal at.|  
|optional count|Optional number of rows to remove. Default **count** is 1.|  
  
## <a name="__toc360789511"></a>Remarks  
  
-   Table.RemoveRows is similar to List.RemoveRange but requires a table as input.  
  
## Example  
  
```powerquery-m
Table.RemoveRows(Table.FromRecords({  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}), 2)  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|2|Jim|987-6543|  
|4|Ringo|232-1550|  
  
