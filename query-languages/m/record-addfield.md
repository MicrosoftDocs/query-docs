---
title: "Record.AddField | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
  
