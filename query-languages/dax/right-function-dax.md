---
title: "RIGHT Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.RIGHT.f1"
helpviewer_keywords: 
  - "RIGHT function"
ms.assetid: 2a2fee4f-eb07-4e9f-a01b-67a59bfbce93
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# RIGHT Function (DAX)
RIGHT returns the last character or characters in a text string, based on the number of characters you specify.  
  
## Syntax  
  
```  
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
  
```  
=RIGHT('New Products'[ProductCode],2)  
```  
  
## Example: Using a Column Reference to Specify Character Count  
  
### Description  
The following formula returns a variable number of digits from the product code in the New Products table, depending on the number in the column, MyCount. If there is no value in the column, MyCount, or the value is a blank, RIGHT also returns a blank.  
  
### Code  
  
```  
=RIGHT('New Products'[ProductCode],[MyCount])  
```  
  
## See Also  
[Text Functions &#40;DAX&#41;](text-functions-dax.md)  
[LEFT Function &#40;DAX&#41;](left-function-dax.md)  
[MID Function &#40;DAX&#41;](mid-function-dax.md)  
  
