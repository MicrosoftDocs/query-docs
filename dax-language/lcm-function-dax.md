---
title: "LCM Function (DAX) | Microsoft Docs"
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
ms.assetid: 562842fe-e6df-4270-a47e-002970d4a62a
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# LCM Function (DAX)
Returns the least common multiple of integers. The least common multiple is the smallest positive integer that is a multiple of all integer arguments number1, number2, and so on. Use LCM to add fractions with different denominators.  
  
## Syntax  
  
```  
LCM(number1, [number2], ...)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number1, number2,...|Number1 is required, subsequent numbers are optional. 1 to 255 values for which you want the least common multiple. If value is not an integer, it is truncated.|  
  
## Return Value  
Returns the least common multiple of integers.  
  
## Remarks  
If any argument is nonnumeric, LCM returns the #VALUE! error value.  
  
If any argument is less than zero, LCM returns the #NUM! error value.  
  
If LCM(a,b) &gt;=2^53, LCM returns the #NUM! error value.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=LCM(5, 2)|Least common multiple of 5 and 2.|10|  
|=LCM(24, 36)|Least common multiple of 24 and 36.|72|  
  
