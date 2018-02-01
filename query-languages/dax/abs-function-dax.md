---
title: "ABS Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.ABS.f1"
helpviewer_keywords: 
  - "ABS function"
ms.assetid: 7e754ea7-ba72-454e-bd97-d9b37596a574
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# ABS Function (DAX)
Returns the absolute value of a number.  
  
## Syntax  
  
```  
ABS(<number>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|The number for which you want the absolute value.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
The absolute value of a number is a decimal number, whole or decimal, without its sign. You can use the ABS function to ensure that only non-negative numbers are returned from expressions when nested in functions that require a positive number.  
  
## Example  
The following example returns the absolute value of the difference between the list price and the dealer price, which you might use in a new calculated column, **DealerMarkup**.  
  
```  
=ABS([DealerPrice]-[ListPrice])  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[SIGN Function &#40;DAX&#41;](sign-function-dax.md)  
  
