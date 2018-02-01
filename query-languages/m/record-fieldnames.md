---
title: "Record.FieldNames | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 30cc514f-9b96-4d90-af5a-3556aacedf6c
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Record.FieldNames

  
## About  
Returns a list of field names in order of the record's fields.  
  
```  
Record.FieldNames(record as record) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to check.|  
  
## Example  
  
```  
Record.FieldNames( [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0] )  
```  
  
```  
equals {"OrderID","CustomerID", "Bait", "Price"}  
```  
