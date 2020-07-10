---
title: "SWITCH function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# SWITCH

Evaluates an expression against a list of values and returns one of multiple possible result expressions.  
  
## Syntax  
  
```dax
SWITCH(<expression>, <value>, <result>[, <value>, <result>]…[, <else>])  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
| expression  | Any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row/context).   |  
| value |  A constant value to be matched with the results of *expression*.  |
|result |Any scalar expression to be evaluated if the results of *expression* match the corresponding *value*.  |
|else |Any scalar expression to be evaluated if the result of *expression* doesn't match any of the *value* arguments.  |

## Return value

A scalar value coming from one of the *result* expressions, if there was a match with *value*, or from the *else* expression, if there was no match with any *value*.  
  
## Remarks

All result expressions and the else expression must be of the same data type.  
  
## Example

The following example creates a calculated column of month names.  
  
```dax
=SWITCH([Month], 1, "January", 2, "February", 3, "March", 4, "April"  
               , 5, "May", 6, "June", 7, "July", 8, "August"  
               , 9, "September", 10, "October", 11, "November", 12, "December"  
               , "Unknown month number" )  
```
