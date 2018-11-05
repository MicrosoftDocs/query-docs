---
title: "Type.IsNullable | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.IsNullable

  
## About  
Returns true if a type is a nullable type; otherwise, false.  
  
## Syntax

<pre>  
Type.IsNullable(#"type" as type) as logical  
</pre>
  
## Examples  
  
```powerquery-m
Type.IsNullable(type nullable number) equals true  
```  
  
```powerquery-m 
Type.IsNullable(number) equals false  
```  
