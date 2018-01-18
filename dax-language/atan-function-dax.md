---
title: "ATAN Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e9202e47-59b3-459e-af3e-cf7c187b5935
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# ATAN Function (DAX)
Returns the arctangent, or inverse tangent, of a number. The arctangent is the angle whose tangent is *number*. The returned angle is given in radians in the range -pi/2 to pi/2.  
  
## Syntax  
  
```  
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
  
