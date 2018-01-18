---
title: "MOD Function (DAX) | Microsoft Docs"
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
f1_keywords: 
  - "sql13.as.daxref.MOD.f1"
helpviewer_keywords: 
  - "MOD function"
ms.assetid: 93dc612d-55cb-4bfe-aadd-5b8277f5b54a
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# MOD Function (DAX)
Returns the remainder after a number is divided by a divisor. The result always has the same sign as the divisor.  
  
## Syntax  
  
```  
MOD(<number>, <divisor>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|The number for which you want to find the remainder after the division is performed.|  
|**divisor**|The number by which you want to divide.|  
  
## Return Value  
A whole number.  
  
## Remarks  
If the divisor is 0 (zero), MOD returns an error. You cannot divide by 0.  
  
The MOD function can be expressed in terms of the INT function: MOD(n, d) = n - d*INT(n/d)  
  
## Example  
The following formula returns 1, the remainder of 3 divided by 2.  
  
```  
=MOD(3,2)  
```  
  
## Example  
The following formula returns -1, the remainder of 3 divided by 2. Note that the sign is always the same as the sign of the divisor.  
  
```  
=MOD(-3,-2)  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](../DAX/math-and-trig-functions-dax.md)  
[ROUND Function &#40;DAX&#41;](../DAX/round-function-dax.md)  
[ROUNDUP Function &#40;DAX&#41;](../DAX/roundup-function-dax.md)  
[ROUNDDOWN Function &#40;DAX&#41;](../DAX/rounddown-function-dax.md)  
[MROUND Function &#40;DAX&#41;](../DAX/mround-function-dax.md)  
[INT Function &#40;DAX&#41;](../DAX/int-function-dax.md)  
  
