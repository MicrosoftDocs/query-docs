---
title: "Error.Record | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Error.Record

  
## About  
Returns a record containing fields “Reason”, “Message”, and “Detail” set to the provided values. The record can be used to raise or throw an error.  
  
## Syntax

<pre>
Error.Record(reason as text, message as text, detail as any) as record  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|reason|The value to set the Reason as.|  
|message|The value to set the Message as.|  
|detail|The value to set the Detail as.|  
  
## Example  
  
```powerquery-m
error Error.Record("InvalidCondition","An error has occured", null)  
equals  error with Reason: “InvalidCondition” and Message “An error has occurred”  
```  
