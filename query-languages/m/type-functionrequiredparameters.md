---
title: "Type.FunctionRequiredParameters | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.FunctionRequiredParameters

  
## About  
Returns a number indicating the minimum number of parameters required to invoke the a type of function.  
  
```  
Type.FunctionRequiredParameters(#"type" as type) as number  
```  
  
## Examples  
  
```  
Type.FunctionRequiredParameters( type function () as any) equals 0  
```  
  
```  
Type.FunctionRequiredParameters( type function (x as number) as any) equals 1  
```  
