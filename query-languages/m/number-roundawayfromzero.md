---
title: "Number.RoundAwayFromZero | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.RoundAwayFromZero

  
## About  
Returns Number.RoundUp(value) when value &gt;= 0 and Number.RoundDown(value) when value &lt; 0.  
  
## Syntax

<pre>
Number.RoundAwayFromZero(value as nullable number) as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to round away from zero.|  
  
## Examples  
  
```powerquery-m
Number.RoundAwayFromZero(-1.2) equals -2  
```  
  
```powerquery-m
Number.RoundAwayFromZero(1.2) equals 2  
```  
