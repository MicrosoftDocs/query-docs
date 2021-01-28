---
description: "Learn more about: EXACT"
title: "EXACT function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# EXACT

Compares two text strings and returns TRUE if they are exactly the same, FALSE otherwise. EXACT is case-sensitive but ignores formatting differences. You can use EXACT to test text being entered into a document.  
  
## Syntax  
  
```dax
EXACT(<text1>,<text2>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|text1|The first text string or column that contains text.|  
|text2|The second text string or column that contains text.|  
  
## Return value

True or false. (Boolean)  
  
## Example

The following formula checks the value of Column1 for the current row against the value of Column2 for the current row, and returns TRUE if they are the same, and returns FALSE if they are different.  
  
```dax
= EXACT([Column1],[Column2])  
```
  
## See also

[Text functions](text-functions-dax.md)  
