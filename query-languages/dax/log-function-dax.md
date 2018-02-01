---
title: "LOG Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.LOG.f1"
helpviewer_keywords: 
  - "LOG function"
  - "logarithm"
ms.assetid: 970a9371-de0f-41c2-84fe-749d40bd37fc
caps.latest.revision: 3
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# LOG Function (DAX)
Returns the logarithm of a number to the base you specify.  
  
## Syntax  
  
```  
LOG(<number>,<base>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|The positive number for which you want the logarithm.|  
|**base**|The base of the logarithm. If omitted, the base is 10.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
You might receive an error if the value is too large to be displayed.  
  
The function LOG10 is similar, but always returns the common logarithm, meaning the logarithm for the base 10.  
  
## Example  
The following formulas return the same result, 2.  
  
```  
=LOG(100,10)  
=LOG(100)  
=LOG10(100)  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[EXP Function &#40;DAX&#41;](exp-function-dax.md)  
[LOG Function &#40;DAX&#41;](log-function-dax.md)  
[LOG Function &#40;DAX&#41;](log-function-dax.md)  
  
