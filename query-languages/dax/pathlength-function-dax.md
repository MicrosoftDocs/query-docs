---
description: "Learn more about: PATHLENGTH"
title: "PATHLENGTH function (DAX) | Microsoft Docs"
---
# PATHLENGTH

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]
Returns the number of parents to the specified item in a given PATH result, including self.  
  
## Syntax  
  
```dax
PATHLENGTH(<path>)  
```

### Parameters  

|Term|Definition|  
|--------|--------------|  
| path |  A text expression resulting from evaluation of a PATH function. |  
  
## Return value

The number of items that are parents to the specified item in a given PATH result, including the specified item.  
  
## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following example takes an employee ID as input to a PATH function and returns a list of the managers above that employee in the hierarchy, The PATHLENGTH function takes that result and counts the different levels of employees and managers, including the employee you started with.  
  
```dax
= PATHLENGTH(PATH(Employee[EmployeeKey], Employee[ParentEmployeeKey]))  
```
