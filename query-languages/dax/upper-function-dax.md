---
title: "UPPER function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# UPPER
Converts a text string to all uppercase letters.  
  
## Syntax  
  
```dax
UPPER (<text>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|text|The text you want converted to uppercase, or a reference to a column that contains text.|  
  
## Property Value/Return value  
Same text, in uppercase.  
  
## Example  
The following formula converts the string in the column, [ProductCode], to all uppercase. Non-alphabetic characters are not affected.  
  
```dax
=UPPER(['New Products'[Product Code])  
```
  
## See also  
[Text functions &#40;DAX&#41;](text-functions-dax.md)  
[LOWER function &#40;DAX&#41;](lower-function-dax.md)  
  
