---
title: "VALUE Function (DAX) | Microsoft Docs"
ms.prod: powerbi 
ms.technology: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# VALUE Function (DAX)
Converts a text string that represents a number to a number.  
  
## Syntax  
  
```dax
VALUE(<text>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**text**|The text to be converted.|  
  
## Return Value  
The converted number in decimal data type.  
  
## Remarks  
The value passed as the **text** parameter can be in any of the constant, number, date, or time formats recognized by Microsoft Excel and the Power Pivot Add-in. If **text** is not in one of these formats, an error is returned. For more information about Power Pivot data types, see [Data Types Supported (SSAS Tabular)](https://msdn.microsoft.com/en-us/92993f7b-7243-4aec-906d-0b0379798242).  
  
You do not generally need to use the VALUE function in a formula because the Power Pivot add-in implicitly converts text to numbers as necessary.  
  
You can also use column references. For example, if you have a column that contains mixed number types, VALUE can be used to convert all values to a single numeric data type. However, if you use the VALUE function with a column that contains mixed numbers and text, the entire column is flagged with an error, because not all values in all rows can be converted to numbers.  
  
## Example  
The following formula converts the typed string, "3", into the numeric value 3.  
  
```dax
=VALUE("3")  
```
  
## See Also  
[Text Functions &#40;DAX&#41;](text-functions-dax.md)  
  
