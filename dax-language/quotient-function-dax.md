---
title: "QUOTIENT Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.QUOTIENT.f1"
helpviewer_keywords: 
  - "QUOTIENT function"
ms.assetid: 4156e802-9bbb-4dc7-b8a7-ec6286aaf95d
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# QUOTIENT Function (DAX)
Performs division and returns only the integer portion of the division result. Use this function when you want to discard the remainder of division.  
  
## Syntax  
  
```  
QUOTIENT(<numerator>, <denominator>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**numerator**|The dividend, or number to divide.|  
|**denominator**|The divisor, or number to divide by.|  
  
## Return Value  
A whole number.  
  
## Remarks  
If either argument is non-numeric, QUOTIENT returns the **#VALUE!** error value.  
  
You can use a column reference instead of a literal value for either argument. However, if the column that you reference contains a 0 (zero), an error is returned for the entire column of values.  
  
## Example  
The following formulas return the same result, 2.  
  
```  
=QUOTIENT(5,2)  
=QUOTIENT(10/2,2)  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](../DAX/math-and-trig-functions-dax.md)  
  
