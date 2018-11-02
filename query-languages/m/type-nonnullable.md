---
title: "Type.NonNullable | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.NonNullable

  
## About  
Returns the non nullable type from a type.  
  
## Syntax

<pre>
Type.NonNullable(#"type" as type) as type  
</pre>
  
## Example  
  
```powerquery-m 
Type.NonNullable(type nullable number) equals type number  
```  
