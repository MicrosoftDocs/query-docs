---
title: "SWITCH Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.SWITCH.f1"
helpviewer_keywords: 
  - "SWITCH Function (DAX)"
ms.assetid: 5e7db20e-1a3b-42e3-8adf-bcc34c6eb550
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# SWITCH Function (DAX)
Evaluates an expression against a list of values and returns one of multiple possible result expressions.  
  
## Syntax  
  
```  
SWITCH(<expression>, <value>, <result>[, <value>, <result>]…[, <else>])  
```  
  
#### Parameters  
expression  
Any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row/context).  
  
value  
A constant value to be matched with the results of *expression*.  
  
result  
Any scalar expression to be evaluated if the results of *expression* match the corresponding *value*.  
  
else  
Any scalar expression to be evaluated if the result of *expression* doesn't match any of the *value* arguments.  
  
## Return Value  
A scalar value coming from one of the *result* expressions, if there was a match with *value*, or from the *else* expression, if there was no match with any *value*.  
  
## Remarks  
All result expressions and the else expression must be of the same data type.  
  
## Example  
The following example creates a calculated column of month names.  
  
```  
=SWITCH([Month], 1, "January", 2, "February", 3, "March", 4, "April"  
               , 5, "May", 6, "June", 7, "July", 8, "August"  
               , 9, "September", 10, "October", 11, "November", 12, "December"  
               , "Unknown month number" )  
```  
