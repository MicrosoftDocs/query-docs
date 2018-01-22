---
title: "LN Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.LN.f1"
helpviewer_keywords: 
  - "LN function"
ms.assetid: 958ba661-7136-4029-b861-3430c50c8b81
caps.latest.revision: 3
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# LN Function (DAX)
Returns the natural logarithm of a number. Natural logarithms are based on the constant e (2.71828182845904).  
  
## Syntax  
  
```  
LN(<number>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|The positive number for which you want the natural logarithm.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
LN is the inverse of the EXP function.  
  
## Example  
The following example returns the natural logarithm of the number in the column, `[Values]`.  
  
```  
=LN([Values])  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[EXP Function &#40;DAX&#41;](exp-function-dax.md)  
  
