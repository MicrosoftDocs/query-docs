---
title: "ISTEXT Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.ISTEXT.f1"
helpviewer_keywords: 
  - "ISTEXT function"
ms.assetid: 308af2eb-425c-4305-b3a7-323cc53198af
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# ISTEXT Function (DAX)
Checks if a value is text, and returns TRUE or FALSE.  
  
## Syntax  
  
```  
ISTEXT(<value>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**value**|The value you want to check.|  
  
## Property Value/Return Value  
TRUE if the value is text; otherwise FALSE  
  
## Example  
The following examples show the behavior of the ISTEXT function.  
  
```  
//RETURNS: Is Text  
=IF(ISTEXT("text"), "Is Text", "Is Non-Text")  
  
//RETURNS: Is Text  
=IF(ISTEXT(""), "Is Text", "Is Non-Text")  
  
//RETURNS: Is Non-Text  
=IF(ISTEXT(1), "Is Text", "Is Non-Text")  
  
//RETURNS: Is Non-Text  
=IF(ISTEXT(BLANK()), "Is Text", "Is Non-Text")  
```  
  
## See Also  
[Information Functions &#40;DAX&#41;](information-functions-dax.md)  
  
