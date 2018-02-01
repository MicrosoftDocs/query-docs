---
title: "REPLACE Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.REPLACE.f1"
helpviewer_keywords: 
  - "REPLACE function"
ms.assetid: 32f42385-8f18-45c8-abb9-04a889b1f75f
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# REPLACE Function (DAX)
REPLACE replaces part of a text string, based on the number of characters you specify, with a different text string.  
  
## Syntax  
  
```  
REPLACE(<old_text>, <start_num>, <num_chars>, <new_text>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**old_text**|The string of text that contains the characters you want to replace, or a reference to a column that contains text.|  
|**start_num**|The position of the character in **old_text** that you want to replace with **new_text**.|  
|**num_chars**|The number of characters that you want to replace. **Warning:** If the argument, *num_chars*, is a blank or references a column that evaluates to a blank, the string for *new_text* is inserted at the position, *start_num*, without replacing any characters. This is the same behavior as in Excel.|  
|**new_text**|The replacement text for the specified characters in **old_text**.|  
  
## Property Value/Return Value  
A text string.  
  
## Remarks  
Whereas Microsoft Excel has different functions for use with single-byte and double-byte character languages, DAX uses Unicode and therefore stores all characters as the same length.  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see  [http://go.microsoft.com/fwlink/?LinkId=219171](http://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example  
The following formula creates a new calculated column that replaces the first two characters of the product code in column, [ProductCode], with a new two-letter code, OB.  
  
```  
=REPLACE('New Products'[Product Code],1,2,"OB")  
```  
  
## See Also  
[Text Functions &#40;DAX&#41;](text-functions-dax.md)  
[SUBSTITUTE Function &#40;DAX&#41;](substitute-function-dax.md)  
  
