---
title: "LOG10 Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.LOG10.f1"
helpviewer_keywords: 
  - "LOG10 function"
  - "logarithm"
ms.assetid: 878879f7-8dac-4a1f-bc00-f9f1784db386
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# LOG10 Function (DAX)
Returns the base-10 logarithm of a number.  
  
## Syntax  
  
```  
LOG10(<number>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|A positive number for which you want the base-10 logarithm.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
The LOG function lets you change the base of the logarithm, instead of using the base 10.  
  
## Example  
The following formulas return the same result, 2:  
  
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
  
