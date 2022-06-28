---
description: "Learn more about: ASIN"
title: "ASIN function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# ASIN

Returns the arcsine, or inverse sine, of a number. The arcsine is the angle whose sine is *number*. The returned angle is given in radians in the range -pi/2 to pi/2.  
  
## Syntax  
  
```dax
ASIN(number)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The sine of the angle you want and must be from -1 to 1.|  
  
## Return value

Returns the arcsine, or inverse sine, of a number.  
  
## Remarks

To express the arcsine in degrees, multiply the result by 180/PI( ) or use the DEGREES function.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|= ASIN(-0.5)|Arcsine of -0.5 in radians, -pi/6|-0.523598776|  
|= ASIN(-0.5)*180/PI()|Arcsine of -0.5 in degrees|-30|  
|= DEGREES(ASIN(-0.5))|Arcsine of -0.5 in degrees|-30|  
