---
title: "Record.FieldOrDefault | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.FieldOrDefault

  
## About  
Returns the value of a field from a record, or the default value if the field does not exist.  
  
```  
Record.FieldOrDefault(record as record, field as text, optional defaultValue as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to check.|  
|field|The field to return.|  
|optional defaultValue|The default value to return if the field does not exist.|  
  
## Examples  
  
```  
Record.FieldOrDefault([CustomerID =1, Name="Bob"], "Phone") equals null  
```  
  
```  
Record.FieldOrDefault([CustomerID =1, Name="Bob"], "Phone", "123-4567") equals "123-4567"  
```  
