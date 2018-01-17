---
title: "ASIN Function (DAX) | Microsoft Docs"
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
ms.assetid: ebad9ae9-d09a-434d-9fe4-55d50ab8dcc7
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# ASIN Function (DAX)
Returns the arcsine, or inverse sine, of a number. The arcsine is the angle whose sine is *number*. The returned angle is given in radians in the range -pi/2 to pi/2.  
  
## Syntax  
  
```  
ASIN(number)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The sine of the angle you want and must be from -1 to 1.|  
  
## Return Value  
Returns the arcsine, or inverse sine, of a number.  
  
## Remarks  
To express the arcsine in degrees, multiply the result by 180/PI( ) or use the DEGREES function.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=ASIN(-0.5)|Arcsine of -0.5 in radians, -pi/6|-0.523598776|  
|=ASIN(-0.5)*180/PI()|Arcsine of -0.5 in degrees|-30|  
|=DEGREES(ASIN(-0.5))|Arcsine of -0.5 in degrees|-30|  
  
