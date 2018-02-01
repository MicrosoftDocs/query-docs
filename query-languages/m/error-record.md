---
title: "Error.Record | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3845be6b-45f3-4060-9fcc-3494b4440bc6
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Error.Record

  
## About  
Returns a record containing fields “Reason”, “Message”, and “Detail” set to the provided values. The record can be used to raise or throw an error.  
  
```  
Error.Record(reason as text, message as text, detail as any) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|reason|The value to set the Reason as.|  
|message|The value to set the Message as.|  
|detail|The value to set the Detail as.|  
  
## Example  
  
```  
error Error.Record("InvalidCondition","An error has occured", null)  
equals  error with Reason: “InvalidCondition” and Message “An error has occurred”  
```  
