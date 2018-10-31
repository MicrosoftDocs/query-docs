---
title: "Function.Invoke | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Function.Invoke

  
## About  
Invokes the given function using the specified Arguments and returns the result.  
  
## Syntax

<pre>
Function.Invoke(function as function, args as list) as any  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|function|The function to invoke.|  
|args|The list of required Arguments.|  
  
## Example  
  
```powerquery-m
Function.Invoke(Record.FieldNames, {[A=1,B=2]}) equals {"A", "B"}  
```  
