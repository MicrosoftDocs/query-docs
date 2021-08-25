---
description: "Learn more about: SIN"
title: "SIN function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# SIN

Returns the sine of the given angle.  
  
## Syntax  
  
```dax
SIN(number)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Required. The angle in radians for which you want the sine.|  
  
## Return value

Returns the sine of the given angle.  
  
## Remarks

If an argument is in degrees, multiply it by PI()/180 or use the RADIANS function to convert it to radians.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|= SIN(PI())|Sine of pi radians (0, approximately).|0.0|  
|= SIN(PI()/2)|Sine of pi/2 radians.|1.0|  
|= SIN(30*PI()/180)|Sine of 30 degrees.|0.5|  
|= SIN(RADIANS(30))|Sine of 30 degrees.|0.5|  
