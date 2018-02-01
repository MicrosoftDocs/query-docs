---
title: "Table.DemoteHeaders | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 9cbb6d7d-29f1-4f33-8fc7-bede921d5b08
caps.latest.revision: 9
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.DemoteHeaders

  
## About  
Demotes the header row down into the first row of a table.  
  
```  
Table.DemoteHeaders(table as table) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
  
## Example  
  
```  
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
  
