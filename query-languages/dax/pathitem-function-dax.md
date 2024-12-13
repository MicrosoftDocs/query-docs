---
description: "Learn more about: PATHITEM"
title: "PATHITEM function (DAX)"
---
# PATHITEM

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]
Returns the item at the specified `position` from a string resulting from evaluation of a PATH function. Positions are counted from left to right.  
  
## Syntax  
  
```dax
PATHITEM(<path>, <position>[, <type>])  
```
  
### Parameters

|Term|Definition|  
|--------|--------------|  
|`path`| A text string in the form of the results of a PATH function.    |  
|`position`|  An integer expression with the position of the item to be returned.  |
|`type`|  (Optional)An enumeration that defines the data type of the result:  |

#### type enumeration

|Enumeration|Alternate Enumeration|Description|
|-----|-----|-----|
|`TEXT`|0|Results are returned with the data type text. (default).|  
|`INTEGER`|1|Results are returned as integers.|  
  
## Return value

The identifier returned by the PATH function at the specified position in the list of identifiers. Items returned by the PATH function are ordered by most distant to current.  
  
## Remarks  
  
- This function can be used to return a specific level from a hierarchy returned by a PATH function. For example, you could return just the skip-level managers for all employees.  
  
- If you specify a number for `position` that is less than one (1) or greater than the number of elements in `path`, the PATHITEM function returns BLANK  
  
- If `type` is not a valid enumeration element an error is returned.  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following example returns the third tier manager of the current employee; it takes the employee and manager IDs as the input to a PATH function that returns a string with the hierarchy of parents to current employee. From that string PATHITEM returns the third entry as an integer.  
  
```dax
= PATHITEM(PATH(Employee[EmployeeKey], Employee[ParentEmployeeKey]), 3, 1)  
```
