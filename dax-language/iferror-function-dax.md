---
title: "IFERROR Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.IFERROR.f1"
helpviewer_keywords: 
  - "IFERROR function"
ms.assetid: 92d6189e-28dc-488a-b4c8-fc7fc71ab227
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# IFERROR Function (DAX)
Evaluates an expression and returns a specified value if the expression returns an error; otherwise returns the value of the expression itself.  
  
## Syntax  
  
```  
IFERROR(value, value_if_error)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**value**|Any value or expression.|  
|**value_if_error**|Any value or expression.|  
  
## Return Value  
A scalar of the same type as **value**  
  
## Remarks  
You can use the IFERROR function to trap and handle errors in an expression.  
  
If **value** or **value_if_error** is an empty cell, IFERROR treats it as an empty string value ("").  
  
The IFERROR function is based on the IF function, and uses the same error messages, but has fewer arguments. The relationship between the IFERROR function and the IF function as follows:  
  
`IFERROR(A,B) := IF(ISERROR(A), B, A)`  
  
Note that the values that are returned for A and B must be of the same data type; therefore, the column or expression used for **value** and the value returned for **value_if_error** must be the same data type.  
  
## Example  
The following example returns 9999 if the expression 25/0 evaluates to an error. If the expression returns a value other than error, that value is passed to the invoking expression.  
  
```  
=IFERROR(25/0,9999)  
```  
  
## See Also  
[Logical Functions &#40;DAX&#41;](../DAX/logical-functions-dax.md)  
  
