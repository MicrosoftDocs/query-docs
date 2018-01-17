---
title: "TRIM Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.TRIM.f1"
helpviewer_keywords: 
  - "TRIM function"
ms.assetid: 75ebaccc-d758-4989-abf7-2149dfccc50f
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# TRIM Function (DAX)
Removes all spaces from text except for single spaces between words.  
  
## Syntax  
  
```  
TRIM(<text>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**text**|The text from which you want spaces removed, or a column that contains text.|  
  
## Property Value/Return Value  
The string with spaces removed.  
  
## Remarks  
Use TRIM on text that you have received from another application that may have irregular spacing.  
  
The TRIM function was originally designed to trim the 7-bit ASCII space character (value 32) from text. In the Unicode character set, there is an additional space character called the nonbreaking space character that has a decimal value of 160. This character is commonly used in Web pages as the HTML entity, &amp;nbsp;. By itself, the TRIM function does not remove this nonbreaking space character. For an example of how to trim both space characters from text, see Remove spaces and nonprinting characters from text.  
  
## Example  
The following formula creates a new string that does not have trailing white space.  
  
```  
=TRIM("A column with trailing spaces.   ")  
```  
When you create the formula, the formula is propagated through the row just as you typed it, so that you see the original string in each formula and the results are not apparent. However, when the formula is evaluated the string is trimmed.  
  
You can verify that the formula produces the correct result by checking the length of the calculated column created by the previous formula, as follows:  
  
```  
=LEN([Calculated Column 1])  
```  
  
## See Also  
[Text Functions &#40;DAX&#41;](../DAX/text-functions-dax.md)  
  
