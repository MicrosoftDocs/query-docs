---
title: "Type.IsNullable | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.IsNullable

  
## About  
Returns true if a type is a nullable type; otherwise, false.  
  
```  
Type.IsNullable(#"type" as type) as logical  
```  
  
## Examples  
  
```  
Type.IsNullable(type nullable number) equals true  
```  
  
```  
Type.IsNullable(number) equals false  
```  
