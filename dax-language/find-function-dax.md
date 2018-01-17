---
title: "FIND Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.FIND.f1"
helpviewer_keywords: 
  - "FIND function"
ms.assetid: ce86320e-f098-436b-8907-4f460090f8e3
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# FIND Function (DAX)
Returns the starting position of one text string within another text string. FIND is case-sensitive.  
  
## Syntax  
  
```  
FIND(<find_text>, <within_text>[, [<start_num>][, <NotFoundValue>]])  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**find_text**|The text you want to find. Use double quotes (empty text) to match the first character in **within_text**.<br /><br />You can use wildcard characters — the question mark (?) and asterisk (\*) — in **find_text**. A question mark matches any single character; an asterisk matches any sequence of characters. If you want to find an actual question mark or asterisk, type a tilde (~) before the character.|  
|**within_text**|The text containing the text you want to find.|  
|**start_num**|(optional) The character at which to start the search; if omitted, **start_num** = 1. The first character in **within_text** is character number 1.|  
|**NotFoundValue**|(optional) The value that should be returned when the operation does not find a matching substring, typically 0, -1, or BLANK().|  
  
## Property Value/Return Value  
Number that shows the starting point of the text string you want to find.  
  
## Remarks  
Whereas Microsoft Excel has multiple versions of the FIND function to accommodate single-byte character set (SBCS) and double-byte character set (DBCS) languages, DAX uses Unicode and counts each character the same way; therefore, you do not need to use a different version depending on the character type.  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see [http://go.microsoft.com/fwlink/?LinkId=219171](http://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example  
The following formula finds the position of the first letter of the product designation, BMX, in the string that contains the product description.  
  
```  
=FIND("BMX","line of BMX racing goods")  
```  
  
## See Also  
[Text Functions &#40;DAX&#41;](../DAX/text-functions-dax.md)  
  
