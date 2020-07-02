---
title: "PATHLENGTH function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# PATHLENGTH
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
This function is not optimized for use in DirectQuery mode. To learn more, see  [DAX formula compatibility in DirectQuery mode](https://go.microsoft.com/fwlink/?LinkId=219172). 
  
## Example  
The following example takes an employee ID as input to a PATH function and returns a list of the managers above that employee in the hierarchy, The PATHLENGTH function takes that result and counts the different levels of employees and managers, including the employee you started with.  
  
```dax
=PATHLENGTH(PATH(Employee[EmployeeKey], Employee[ParentEmployeeKey]))  
```
