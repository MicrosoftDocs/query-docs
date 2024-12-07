---
description: "Learn more about: PATHCONTAINS"
title: "PATHCONTAINS function (DAX) | Microsoft Docs"
---
# PATHCONTAINS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns `TRUE` if the specified `item` exists within the specified `path`.  
  
## Syntax  
  
```dax
PATHCONTAINS(<path>, <item>)  
```
  
### Parameters

|Term|Definition|  
|--------|--------------|  
|`path`| A string created as the result of evaluating a PATH function.  |  
|`item`|  A text expression to look for in the path result.  |

## Return value

A value of `TRUE` if `item` exists in `path`; otherwise `FALSE`.  
  
## Remarks

- If `item` is an integer number it is converted to text and then the function is evaluated. If conversion fails then the function returns an error.  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following example creates a calculated column that takes a manager ID and checks a set of employees. If the manager ID is among the list of managers returned by the PATH function, the PATHCONTAINS function returns true; otherwise it returns false.  
  
```dax
= PATHCONTAINS(PATH(Employee[EmployeeKey], Employee[ParentEmployeeKey]), "23")  
```
