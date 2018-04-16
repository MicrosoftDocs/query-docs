---
title: "Type.FunctionParameters | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.FunctionParameters

  
## About  
Returns a record with field values set to the name of the parameters of a function type, and their values set to their corresponding types.  
  
```  
Type.FunctionParameters(functionType as type) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|functionType|The function type to check.|  
  
## Examples  
  
```  
Type.FunctionParameters(type function () as any) equals []  
```  
  
```  
Type.FunctionParameters(type function (x as number, y as text) as any) equals [ x = number, y = text ]  
```  
