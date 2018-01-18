---
title: "ISNUMBER Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.ISNUMBER.f1"
helpviewer_keywords: 
  - "ISNUMBER function"
ms.assetid: ddf1a240-aa78-49ea-8f99-11050e5301fd
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# ISNUMBER Function (DAX)
Checks whether a value is a number, and returns TRUE or FALSE.  
  
## Syntax  
  
```  
ISNUMBER(<value>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**value**|The value you want to test.|  
  
## Property Value/Return Value  
TRUE if the value is numeric; otherwise FALSE.  
  
## Example  
The following three samples show the behavior of ISNUMBER.  
  
```  
//RETURNS: Is number  
=IF(ISNUMBER(0), "Is number", "Is Not number")  
  
//RETURNS: Is number  
=IF(ISNUMBER(3.1E-1),"Is number", "Is Not number")  
  
//RETURNS: Is Not number  
=IF(ISNUMBER("123"), "Is number", "Is Not number")  
```  
  
## See Also  
[Information Functions &#40;DAX&#41;](../DAX/information-functions-dax.md)  
  
