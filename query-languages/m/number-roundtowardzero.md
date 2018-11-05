---
title: "Number.RoundTowardZero | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.RoundTowardZero

  
## About  
Returns Number.RoundDown(x) when x &gt;= 0 and Number.RoundUp(x) when x &lt; 0.  
  
## Syntax

<pre>
Number.RoundTowardZero(value as nullable number) as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to round toward zero.|  
  
## Examples  
  
```powerquery-m 
Number.RoundTowardZero(-1.2) equals -1  
```  
  
```powerquery-m
Number.RoundTowardZero(1.2) equals 1  
```  
