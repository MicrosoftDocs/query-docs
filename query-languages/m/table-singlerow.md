---
title: "Table.SingleRow | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 0f57e499-b92a-41a2-af2a-d7f7cee9f192
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
  
