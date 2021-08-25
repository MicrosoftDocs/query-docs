---
description: "Learn more about: IFERROR"
title: "IFERROR function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 08/13/2021
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# IFERROR

Evaluates an expression and returns a specified value if the expression returns an error; otherwise returns the value of the expression itself.  
  
## Syntax  
  
```dax
IFERROR(value, value_if_error)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|value|Any value or expression.|  
|value_if_error|Any value or expression.|  
  
## Return value

A scalar of the same type as **value**  
  
## Remarks

- You can use the IFERROR function to trap and handle errors in an expression.  
  
- If **value** or **value_if_error** is an empty cell, IFERROR treats it as an empty string value ("").  
  
- The IFERROR function is based on the IF function, and uses the same error messages, but has fewer arguments. The relationship between the IFERROR function and the IF function as follows:  
  
  `IFERROR(A,B) := IF(ISERROR(A), B, A)`  
  
  Values that are returned for A and B must be of the same data type; therefore, the column or expression used for **value** and the value returned for **value_if_error** must be the same data type.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

- For best practices when using IFERROR, see [Appropriate use of error functions](best-practices/dax-error-functions.md).

## Example

The following example returns 9999 if the expression 25/0 evaluates to an error. If the expression returns a value other than error, that value is passed to the invoking expression.  
  
```dax
= IFERROR(25/0,9999)  
```
  
## See also

[Logical functions](logical-functions-dax.md)  
