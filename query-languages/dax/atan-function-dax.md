---
title: "ATAN Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ATAN Function (DAX)
Returns the arctangent, or inverse tangent, of a number. The arctangent is the angle whose tangent is *number*. The returned angle is given in radians in the range -pi/2 to pi/2.  
  
## Syntax  
  
```dax
ATAN(number)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The tangent of the angle you want.|  
  
## Return Value  
Returns the inverse hyperbolic tangent of a number.  
  
## Remarks  
To express the arctangent in degrees, multiply the result by 180/PI( ) or use the DEGREES function.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=ATAN(1)|Arctangent of 1 in radians, pi/4|0.785398163|  
|=ATAN(1)*180/PI()|Arctangent of 1 in degrees|45|  
  
