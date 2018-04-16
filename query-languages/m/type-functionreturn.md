---
title: "Type.FunctionReturn | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.FunctionReturn

  
## About  
Returns a type returned by a function type.  
  
```  
Type.FunctionReturn(type as type) as type  
```  
  
## Examples  
  
```  
Type.FunctionReturn(type function () as any) equals type any  
```  
  
```  
Type.FunctionReturn(type function () as [A = number]) equals type [A = number]  
```  
