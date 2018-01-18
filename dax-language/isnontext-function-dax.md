---
title: "ISNONTEXT Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.ISNONTEXT.f1"
helpviewer_keywords: 
  - "ISNONTEXT function"
ms.assetid: 7b041fd9-4531-4dff-8932-254a6fb09cae
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# ISNONTEXT Function (DAX)
Checks if a value is not text (blank cells are not text), and returns TRUE or FALSE.  
  
## Syntax  
  
```  
ISNONTEXT(<value>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**value**|The value you want to check.|  
  
## Return Value  
TRUE if the value is not text or blank; FALSE if the value is text.  
  
## Remarks  
An empty string is considered text.  
  
## Example  
The following examples show the behavior of the ISNONTEXT function.  
  
```  
//RETURNS: Is Non-Text  
=IF(ISNONTEXT(1), "Is Non-Text", "Is Text")  
  
//RETURNS: Is Non-Text  
=IF(ISNONTEXT(BLANK()), "Is Non-Text", "Is Text")  
  
//RETURNS: Is Text  
=IF(ISNONTEXT(""), "Is Non-Text", "Is Text")  
```  
  
## See Also  
[Information Functions &#40;DAX&#41;](../DAX/information-functions-dax.md)  
  
