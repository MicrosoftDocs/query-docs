---
title: "Table.SingleRow | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.SingleRow

  
## About  
Returns a single row from a table.  
  
## Syntax

<pre>
Table.SingleRow(table as table) as record  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
  
## <a name="__toc360789538"></a>Remarks  
  
-   Table.SingleRow is similar to List.Single but requires a table as input.  
  
## Example  
  
```powerquery-m
Table.SingleRow(Table.FromRecords(  
  
{  
  
      [CustomerID = 1, Name = "Bob", Phone = "123-4567"]  
  
}  
  
))  
  
equals [CustomerID = 1, Name = "Bob", Phone = "123-4567"]  
```  
  
|||  
|-|-|  
|CustomerID|1|  
|Name|Bob|  
|Phone|123-4567|  
  
