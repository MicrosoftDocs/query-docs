---
title: "Comparer.Ordinal | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Comparer.Ordinal

  
## About  
Returns a comparer function which uses Ordinal rules to compare values.  
  
## Syntax

<pre> 
Comparer.Ordinal(x as any, y as any) as number  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|x|The left value to compare.|  
|y|The right value to compare.|  
  
## Examples  
  
```powerquery-m 
Comparer.Equals(Comparer.Ordinal, "a","A")equals false  
```  
