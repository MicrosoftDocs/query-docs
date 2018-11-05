---
title: "Type.FunctionParameters | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.FunctionParameters

  
## About  
Returns a record with field values set to the name of the parameters of a function type, and their values set to their corresponding types.  
  
## Syntax

<pre>
Type.FunctionParameters(functionType as type) as record  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|functionType|The function type to check.|  
  
## Examples  
  
```powerquery-m 
Type.FunctionParameters(type function () as any) equals []  
```  
  
```powerquery-m 
Type.FunctionParameters(type function (x as number, y as text) as any) equals [ x = number, y = text ]  
```  
