---
title: "SIGN Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.SIGN.f1"
helpviewer_keywords: 
  - "SIGN function"
ms.assetid: 28f30847-71fd-4027-b766-938618c0ad6e
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# SIGN Function (DAX)
Determines the sign of a number, the result of a calculation, or a value in a column. The function returns 1 if the number is positive, 0 (zero) if the number is zero, or -1 if the number is negative.  
  
## Syntax  
  
```  
SIGN(<number>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|Any real number, a column that contains numbers, or an expression that evaluates to a number.|  
  
## Return Value  
A whole number. The possible return values are 1, 0, and -1.  
  
|Return Value|Description|  
|----------------|---------------|  
|1|The number is positive|  
|0|The number is zero|  
|-1|The number is negative|  
  
## Example  
The following formula returns the sign of the result of the expression that calculates sale price minus cost.  
  
```  
=SIGN( ([Sale Price] - [Cost]) )  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](../DAX/math-and-trig-functions-dax.md)  
  
