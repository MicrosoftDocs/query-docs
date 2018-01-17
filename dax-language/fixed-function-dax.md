---
title: "FIXED Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.FIXED.f1"
helpviewer_keywords: 
  - "FIXED function"
ms.assetid: 2cb7aad2-5662-46bb-8040-329ab47abf9a
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# FIXED Function (DAX)
Rounds a number to the specified number of decimals and returns the result as text. You can specify that the result be returned with or without commas.  
  
## Syntax  
  
```  
FIXED(<number>, <decimals>, <no_commas>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|The number you want to round and convert to text, or a column containing a number.|  
|**decimals**|(optional) The number of digits to the right of the decimal point; if omitted, 2.|  
|**no_commas**|(optional) A logical value: if 1, do not display commas in the returned text; if 0 or omitted, display commas in the returned text.|  
  
## Property Value/Return Value  
A number represented as text.  
  
## Remarks  
If the value used for the **decimals** parameter is negative, **number** is rounded to the left of the decimal point.  
  
If you omit **decimals**, it is assumed to be 2.  
  
If **no_commas** is 0 or is omitted, then the returned text includes commas as usual.  
  
The major difference between formatting a cell containing a number by using a command and formatting a number directly with the FIXED function is that FIXED converts its result to text. A number formatted with a command from the formatting menu is still a number.  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following example gets the numeric value for the current row in column, PctCost, and returns it as text with 4 decimal places and no commas.  
  
```  
=FIXED([PctCost],3,1)  
```  
Numbers can never have more than 15 significant digits, but decimals can be as large as 127.  
  
## See Also  
[Text Functions &#40;DAX&#41;](../DAX/text-functions-dax.md)  
[Math and Trig Functions &#40;DAX&#41;](../DAX/math-and-trig-functions-dax.md)  
  
