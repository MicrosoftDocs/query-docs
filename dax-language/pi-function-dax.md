---
title: "PI Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.PI.f1"
helpviewer_keywords: 
  - "PI function"
ms.assetid: b6bc04b3-d6f4-45f1-884a-f93af06f40d1
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# PI Function (DAX)
Returns the value of Pi, 3.14159265358979, accurate to 15 digits.  
  
## Syntax  
  
```  
PI()  
```  
  
## Return Value  
A decimal number with the value of Pi, 3.14159265358979, accurate to 15 digits.  
  
## Remarks  
Pi is a mathematical constant. In DAX, Pi is represented as a real number accurate to 15 digits, the same as Excel.  
  
## Example  
The following formula calculates the area of a circle given the radius in the column, `[Radius]`.  
  
```  
=PI()*([Radius]*2)  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](../DAX/math-and-trig-functions-dax.md)  
  
