---
title: "RIGHT Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# RIGHT Function (DAX)
RIGHT returns the last character or characters in a text string, based on the number of characters you specify.  
  
## Syntax  
  
```dax
RIGHT(<text>, <num_chars>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**text**|The text string that contains the characters you want to extract, or a reference to a column that contains text.|  
|**num_chars**|(optional) The number of characters you want RIGHT to extract; is omitted, 1. You can also use a reference to a column that contains numbers.|  
  
If the column reference does not contain text, it is implicitly cast as text.  
  
## Property Value/Return Value  
A text string containing the specified right-most characters.  
  
## Remarks  
RIGHT always counts each character, whether single-byte or double-byte, as 1, no matter what the default language setting is.  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see [http://go.microsoft.com/fwlink/?LinkId=219171](http://go.microsoft.com/fwlink/?LinkId=219171)  
  
## Example: Returning a Fixed Number of Characters  
  
### Description  
The following formula returns the last two digits of the product code in the New Products table.  
  
### Code  
  
```dax
=RIGHT('New Products'[ProductCode],2)  
```
  
## Example: Using a Column Reference to Specify Character Count  
  
### Description  
The following formula returns a variable number of digits from the product code in the New Products table, depending on the number in the column, MyCount. If there is no value in the column, MyCount, or the value is a blank, RIGHT also returns a blank.  
  
### Code  
  
```dax
=RIGHT('New Products'[ProductCode],[MyCount])  
```
  
## See Also  
[Text Functions &#40;DAX&#41;](text-functions-dax.md)  
[LEFT Function &#40;DAX&#41;](left-function-dax.md)  
[MID Function &#40;DAX&#41;](mid-function-dax.md)  
  
