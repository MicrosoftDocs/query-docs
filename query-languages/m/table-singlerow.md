---
title: "Table.SingleRow | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.SingleRow

  
## About  
Returns a single row from a table.  
  
```  
Table.SingleRow(table as table) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
  
## <a name="__toc360789538"></a>Remarks  
  
-   Table.SingleRow is similar to List.Single but requires a table as input.  
  
## Example  
  
```  
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
  
