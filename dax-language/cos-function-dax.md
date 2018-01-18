---
title: "COS Function (DAX) | Microsoft Docs"
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
ms.assetid: 01a455da-58fc-4623-9cc5-f3e4e216cccb
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# COS Function (DAX)
Returns the cosine of the given angle.  
  
## Syntax  
  
```  
COS(number)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Required. The angle in radians for which you want the cosine.|  
  
## Return Value  
Returns the cosine of the given angle.  
  
## Remarks  
If the angle is in degrees, either multiply the angle by PI()/180 or use the RADIANS function to convert the angle to radians.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=COS(1.047)|Cosine of 1.047 radians|0.5001711|  
|=COS(60*PI()/180)|Cosine of 60 degrees|0.5|  
|=COS(RADIANS(60))|Cosine of 60 degrees|0.5|  
  
