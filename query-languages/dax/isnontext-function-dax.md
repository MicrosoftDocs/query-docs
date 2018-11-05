---
title: "ISNONTEXT Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ISNONTEXT Function (DAX)
Checks if a value is not text (blank cells are not text), and returns TRUE or FALSE.  
  
## Syntax  
  
```dax
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
  
```dax
//RETURNS: Is Non-Text  
=IF(ISNONTEXT(1), "Is Non-Text", "Is Text")  
  
//RETURNS: Is Non-Text  
=IF(ISNONTEXT(BLANK()), "Is Non-Text", "Is Text")  
  
//RETURNS: Is Text  
=IF(ISNONTEXT(""), "Is Non-Text", "Is Text")  
```
  
## See Also  
[Information Functions &#40;DAX&#41;](information-functions-dax.md)  
  
