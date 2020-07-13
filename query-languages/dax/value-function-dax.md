---
title: "VALUE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/13/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# VALUE

Converts a text string that represents a number to a number.  
  
## Syntax  
  
```dax
VALUE(<text>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|text|The text to be converted.|  
  
## Return value

The converted number in decimal data type.  
  
## Remarks

- The value passed as the **text** parameter can be in any of the constant, number, date, or time formats recognized by the application or services you are using. If **text** is not in one of these formats, an error is returned. 
  
- You do not generally need to use the VALUE function in a formula because the engine implicitly converts text to numbers as necessary.  
  
- You can also use column references. For example, if you have a column that contains mixed number types, VALUE can be used to convert all values to a single numeric data type. However, if you use the VALUE function with a column that contains mixed numbers and text, the entire column is flagged with an error, because not all values in all rows can be converted to numbers.  
  
## Example

The following formula converts the typed string, "3", into the numeric value 3.  
  
```dax
= VALUE("3")  
```
  
## See also

[Text functions](text-functions-dax.md)  
