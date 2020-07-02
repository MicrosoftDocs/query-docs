---
title: "COS function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# COS

Returns the cosine of the given angle.  
  
## Syntax  
  
```dax
COS(number)  
```
  
### Parameters
  
|Term|Definition|  
|--------|--------------|  
|number|Required. The angle in radians for which you want the cosine.|  
  
## Return value

Returns the cosine of the given angle.  
  
## Remarks

If the angle is in degrees, either multiply the angle by PI()/180 or use the RADIANS function to convert the angle to radians.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|= COS(1.047)|Cosine of 1.047 radians|0.5001711|  
|= COS(60*PI()/180)|Cosine of 60 degrees|0.5|  
|= COS(RADIANS(60))|Cosine of 60 degrees|0.5|  
