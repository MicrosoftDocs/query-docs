---
title: "ACOSH Function (DAX) | Microsoft Docs"
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
ms.assetid: 05178a1a-4d60-43b4-9177-699ea17c0ba8
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# ACOSH Function (DAX)
Returns the inverse hyperbolic cosine of a number. The number must be greater than or equal to 1. The inverse hyperbolic cosine is the value whose hyperbolic cosine is *number*, so ACOSH(COSH(number)) equals number.  
  
## Syntax  
  
```  
ACOSH(number)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Any real number equal to or greater than 1.|  
  
## Return Value  
Returns the inverse hyperbolic cosine of a number.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=ACOSH(1)|Inverse hyperbolic cosine of 1.|0|  
|=ACOSH(10)|Inverse hyperbolic cosine of 10.|2.993228|  
  
