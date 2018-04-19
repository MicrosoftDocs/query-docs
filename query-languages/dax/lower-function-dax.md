---
title: "LOWER Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# LOWER Function (DAX)
Converts all letters in a text string to lowercase.  
  
## Syntax  
  
```  
LOWER(<text>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**text**|The text you want to convert to lowercase, or a reference to a column that contains text.|  
  
## Property Value/Return Value  
Text in lowercase.  
  
## Remarks  
Characters that are not letters are not changed. For example, the formula `=LOWER("123ABC")` returns **123abc**.  
  
## Example  
The following formula gets each row in the column, [ProductCode], and converts the value to all lowercase. Numbers in the column are not affected.  
  
```  
=LOWER('New Products'[ProductCode])  
```  
  
## See Also  
[Text Functions &#40;DAX&#41;](text-functions-dax.md)  
  
