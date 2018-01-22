---
title: "PATHCONTAINS Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.PATHCONTAINS.f1"
helpviewer_keywords: 
  - "PATHCONTAINS Function (DAX)"
ms.assetid: 7669ab84-db67-4f96-b649-819a7c4ea40d
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# PATHCONTAINS Function (DAX)
Returns **TRUE** if the specified *item* exists within the specified *path*.  
  
## Syntax  
  
```  
PATHCONTAINS(<path>, <item>)  
```  
  
#### Parameters  
path  
A string created as the result of evaluating a PATH function.  
  
item  
A text expression to look for in the path result.  
  
## Return Value  
A value of **TRUE** if *item* exists in *path*; otherwise **FALSE**.  
  
## Remarks  
If *item* is an integer number it is converted to text and then the function is evaluated. If conversion fails then the function returns an error.  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following example creates a calculated column that takes a manager ID and checks a set of employees. If the manager ID is among the list of managers returned by the PATH function, the PATHCONTAINS function returns true; otherwise it returns false.  
  
```  
=PATHCONTAINS(PATH(Employee[EmployeeKey], Employee[ParentEmployeeKey]), "23")  
```  
