---
title: "TAN Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# TAN Function (DAX)
Returns the tangent of the given angle.  
  
## Syntax  
  
```dax
TAN(number)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Required. The angle in radians for which you want the tangent.|  
  
## Return Value  
Returns the tangent of the given angle.  
  
## Remarks  
If your argument is in degrees, multiply it by PI()/180 or use the RADIANS function to convert it to radians.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=TAN(0.785)|Tangent of 0.785 radians (0.99920)|0.99920|  
|=TAN(45*PI()/180)|Tangent of 45 degrees (1)|1|  
|=TAN(RADIANS(45))|Tangent of 45 degrees (1)|1|  
  
