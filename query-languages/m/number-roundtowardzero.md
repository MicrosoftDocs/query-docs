---
title: "Number.RoundTowardZero | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.RoundTowardZero

  
## About  
Returns Number.RoundDown(x) when x &gt;= 0 and Number.RoundUp(x) when x &lt; 0.  
  
```  
Number.RoundTowardZero(value as nullable number) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to round toward zero.|  
  
## Examples  
  
```  
Number.RoundTowardZero(-1.2) equals -1  
```  
  
```  
Number.RoundTowardZero(1.2) equals 1  
```  
