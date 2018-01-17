---
title: "FACT Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.FACT.f1"
helpviewer_keywords: 
  - "FACT function"
  - "factorial"
ms.assetid: 5b027430-3ff2-4583-8d48-ca41fd525160
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# FACT Function (DAX)
Returns the factorial of a number, equal to the series 1*2\*3\*...\* , ending in the given number.  
  
## Syntax  
  
```  
FACT(<number>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|The non-negative number for which you want to calculate the factorial.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
If the number is not an integer, it is truncated and an error is returned. If the result is too large, an error is returned.  
  
## Example  
The following formula returns the factorial for the series of integers in the column, `[Values]`.  
  
```  
=FACT([Values])  
```  
The following table shows the expected results:  
  
|Values|Results|  
|----------|-----------|  
|0|1|  
|1|1|  
|2|2|  
|3|6|  
|4|24|  
|5|120|  
|170|7.257415615308E+306|  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](../DAX/math-and-trig-functions-dax.md)  
[TRUNC Function &#40;DAX&#41;](../DAX/trunc-function-dax.md)  
  
