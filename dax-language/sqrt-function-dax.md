---
title: "SQRT Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.SQRT.f1"
helpviewer_keywords: 
  - "SQRT function"
ms.assetid: 76a29f33-324a-47de-a8fa-0aad31b89edc
caps.latest.revision: 3
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# SQRT Function (DAX)
Returns the square root of a number.  
  
## Syntax  
  
```  
SQRT(<number>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|The number for which you want the square root, a column that contains numbers, or an expression that evaluates to a number.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
If the number is negative, the SQRT function returns an error.  
  
## Example  
The following formula returns 5.  
  
```  
=SQRT(25)  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](../DAX/math-and-trig-functions-dax.md)  
  
