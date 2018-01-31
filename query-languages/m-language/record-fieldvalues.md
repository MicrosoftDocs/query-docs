---
title: "Record.FieldValues | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c2374a35-3e11-4e26-ac38-3b1fb57b9ffd
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Record.FieldValues

  
## About  
Returns a list of field values in order of the record's fields.  
  
```  
Record.FieldValues(record as record) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The record to check.|  
  
## Example  
  
```  
Record.FieldValues( [CustomerID = 1, Name = "Bob", Phone = "123-4567"] ) equals {1, "Bob", "123-4567"}  
```  
