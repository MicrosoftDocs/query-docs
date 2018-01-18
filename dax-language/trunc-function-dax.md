---
title: "TRUNC Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.TRUNC.f1"
helpviewer_keywords: 
  - "TRUNC function"
ms.assetid: d9dbeaff-1af0-4396-9195-1ef4f53eb355
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# TRUNC Function (DAX)
Truncates a number to an integer by removing the decimal, or fractional, part of the number.  
  
## Syntax  
  
```  
TRUNC(<number>,<num_digits>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|The number you want to truncate.|  
|**num_digits**|A number specifying the precision of the truncation; if omitted, 0 (zero)|  
  
## Return Value  
A whole number.  
  
## Remarks  
TRUNC and INT are similar in that both return integers. TRUNC removes the fractional part of the number. INT rounds numbers down to the nearest integer based on the value of the fractional part of the number. INT and TRUNC are different only when using negative numbers: `TRUNC(-4.3)` returns -4, but `INT(-4.3)` returns -5 because -5 is the smaller number.  
  
## Example  
The following formula returns 3, the integer part of pi.  
  
```  
=TRUNC(PI())  
```  
  
## Example  
The following formula returns -8, the integer part of -8.9.  
  
```  
=TRUNC(-8.9)  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](../DAX/math-and-trig-functions-dax.md)  
[ROUND Function &#40;DAX&#41;](../DAX/round-function-dax.md)  
[ROUNDUP Function &#40;DAX&#41;](../DAX/roundup-function-dax.md)  
[ROUNDDOWN Function &#40;DAX&#41;](../DAX/rounddown-function-dax.md)  
[MROUND Function &#40;DAX&#41;](../DAX/mround-function-dax.md)  
[INT Function &#40;DAX&#41;](../DAX/int-function-dax.md)  
  
