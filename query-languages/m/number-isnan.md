---
title: "Number.IsNaN | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.IsNaN

  
## About  
Returns true if a value is Number.NaN.  
  
```  
Number.IsNaN(value as number) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to evaluate.|  
  
## Examples  
  
```  
Number.IsNaN(1) equals false  
```  
  
```  
Number.IsNaN(0/0) equals true  
```  
