---
title: "TAN Function (DAX) | Microsoft Docs"
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
ms.assetid: 9b848e1d-4446-4936-82a1-dea3d7ba78f8
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# TAN Function (DAX)
Returns the tangent of the given angle.  
  
## Syntax  
  
```  
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
  
