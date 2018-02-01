---
title: "Record.AddField | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c3b29fd9-ee68-44e6-9d43-4547d9f66a74
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Record.AddField

  
## About  
Adds a field from a field name and value.  
  
```  
Record.AddField (record as record, fieldName as text, value as any,optional delayed as nullable logical) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to modify.|  
|fieldName|The value to name the field.|  
|value|The value to add to the field.|  
|optional delayed|Indicates whether the field value or a function that computes the field value.|  
  
## Example  
  
```  
Record.AddField( [CustomerID = 1, Name = "Bob", Phone = "123-4567"] , "Address", "123 Main St.")  
```  
  
```  
equals [CustomerID=1, Name= "Bob", Phone="123-4567", Address="123 Main St."]  
```  
  
|||  
|-|-|  
|CustomerID|1|  
|Phone|123-4567|  
|Address|123 Main St.|  
  
