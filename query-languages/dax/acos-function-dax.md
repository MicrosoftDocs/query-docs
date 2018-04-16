---
title: "ACOS Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ACOS Function (DAX)
Returns the arccosine, or inverse cosine, of a number. The arccosine is the angle whose cosine is *number*. The returned angle is given in radians in the range 0 (zero) to pi.  
  
## Syntax  
  
```  
ACOS(number)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Number|The cosine of the angle you want and must be from -1 to 1.|  
  
## Return Value  
Returns the arccosine, or inverse cosine, of a number.  
  
## Remarks  
If you want to convert the result from radians to degrees, multiply it by 180/PI() or use the DEGREES function.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=ACOS(-0.5)|Arccosine of -0.5 in radians, 2*pi/3.|2.094395102|  
|=ACOS(-0.5)*180/PI()|Arccosine of -0.5 in degrees.|120|  
  
