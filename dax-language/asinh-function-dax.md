---
title: "ASINH Function (DAX) | Microsoft Docs"
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
ms.assetid: aea6409a-21a1-4655-9578-2c9f1155cb8a
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# ASINH Function (DAX)
Returns the inverse hyperbolic sine of a number. The inverse hyperbolic sine is the value whose hyperbolic sine is *number*, so ASINH(SINH(number)) equals *number*.  
  
## Syntax  
  
```  
ASINH(number)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Any real number.|  
  
## Return Value  
Returns the inverse hyperbolic sine of a number.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=ASINH(-2.5)|Inverse hyperbolic sine of -2.5|-1.647231146|  
|=ASINH(10)|Inverse hyperbolic sine of 10|2.99822295|  
  
