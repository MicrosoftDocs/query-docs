---
title: "PATHLENGTH function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# PATHLENGTH function (DAX)
Returns the number of parents to the specified item in a given PATH result, including self.  
  
## Syntax  
  
```dax
PATHLENGTH(<path>)  
```
  
#### Parameters  

|Term|Definition|  
|--------|--------------|  
| path |  A text expression resulting from evaluation of a PATH function. |  
  
## Return value  
The number of items that are parents to the specified item in a given PATH result, including the specified item.  
  
## Remarks  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [https://go.microsoft.com/fwlink/?LinkId=219172](https://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following example takes an employee ID as input to a PATH function and returns a list of the managers above that employee in the hierarchy, The PATHLENGTH function takes that result and counts the different levels of employees and managers, including the employee you started with.  
  
```dax
=PATHLENGTH(PATH(Employee[EmployeeKey], Employee[ParentEmployeeKey]))  
```
