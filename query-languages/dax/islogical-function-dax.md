---
title: "ISLOGICAL Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.ISLOGICAL.f1"
helpviewer_keywords: 
  - "ISLOGICAL function"
ms.assetid: 8b5f9b9f-52ab-48f4-a99f-7999936e2feb
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# ISLOGICAL Function (DAX)
Checks whether a value is a logical value, (TRUE or FALSE), and returns TRUE or FALSE.  
  
## Syntax  
  
```  
ISLOGICAL(<value>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**value**|The value that you want to test.|  
  
## Property Value/Return Value  
TRUE if the value is a logical value; FALSE if any value other than TRUE OR FALSE.  
  
## Example  
The following three samples show the behavior of ISLOGICAL.  
  
```  
//RETURNS: Is Boolean type or Logical  
=IF(ISLOGICAL(true), "Is Boolean type or Logical", "Is different type")  
  
//RETURNS: Is Boolean type or Logical  
=IF(ISLOGICAL(false), "Is Boolean type or Logical", "Is different type")  
  
//RETURNS: Is different type  
=IF(ISLOGICAL(25), "Is Boolean type or Logical", "Is different type")  
```  
  
## See Also  
[Information Functions &#40;DAX&#41;](information-functions-dax.md)  
  
