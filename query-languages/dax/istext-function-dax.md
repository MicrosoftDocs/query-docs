---
title: "ISTEXT function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ISTEXT

Checks if a value is text, and returns TRUE or FALSE.  
  
## Syntax  
  
```dax
ISTEXT(<value>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|value|The value you want to check.|  
  
## Return value

TRUE if the value is text; otherwise FALSE  
  
## Example

The following examples show the behavior of the ISTEXT function.  
  
```dax
//RETURNS: Is Text  
= IF(ISTEXT("text"), "Is Text", "Is Non-Text")  
  
//RETURNS: Is Text  
= IF(ISTEXT(""), "Is Text", "Is Non-Text")  
  
//RETURNS: Is Non-Text  
= IF(ISTEXT(1), "Is Text", "Is Non-Text")  
  
//RETURNS: Is Non-Text  
= IF(ISTEXT(BLANK()), "Is Text", "Is Non-Text")  
```
  
## See also

[Information functions &#40;DAX&#41;](information-functions-dax.md)  
