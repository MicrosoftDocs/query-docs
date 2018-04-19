---
title: "UPPER Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# UPPER Function (DAX)
Converts a text string to all uppercase letters  
  
## Syntax  
  
```  
UPPER (<text>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**text**|The text you want converted to uppercase, or a reference to a column that contains text.|  
  
## Property Value/Return Value  
Same text, in uppercase.  
  
## Example  
The following formula converts the string in the column, [ProductCode], to all uppercase. Non-alphabetic characters are not affected.  
  
```  
=UPPER(['New Products'[Product Code])  
```  
  
## See Also  
[Text Functions &#40;DAX&#41;](text-functions-dax.md)  
[LOWER Function &#40;DAX&#41;](lower-function-dax.md)  
  
