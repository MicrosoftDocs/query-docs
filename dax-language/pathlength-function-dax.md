---
title: "PATHLENGTH Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.PATHLENGTH.f1"
helpviewer_keywords: 
  - "PATHLENGTH Function (DAX)"
ms.assetid: 930e8b20-08de-40f9-afa3-4ae225f77247
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# PATHLENGTH Function (DAX)
Returns the number of parents to the specified item in a given PATH result, including self.  
  
## Syntax  
  
```  
PATHLENGTH(<path>)  
```  
  
#### Parameters  
path  
A text expression resulting from evaluation of a PATH function.  
  
## Return Value  
The number of items that are parents to the specified item in a given PATH result, including the specified item.  
  
## Remarks  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following example takes an employee ID as input to a PATH function and returns a list of the managers above that employee in the hierarchy, The PATHLENGTH function takes that result and counts the different levels of employees and managers, including the employee you started with.  
  
```  
=PATHLENGTH(PATH(Employee[EmployeeKey], Employee[ParentEmployeeKey]))  
```  
