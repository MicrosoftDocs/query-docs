---
title: "Record.FieldOrDefault | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 72317d05-f7f2-4f48-9426-240db65479cb
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
