---
title: "REPT Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.REPT.f1"
helpviewer_keywords: 
  - "REPT function"
ms.assetid: d5cacc42-1403-4bf7-bc6d-2f508e39f76f
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# REPT Function (DAX)
Repeats text a given number of times. Use REPT to fill a cell with a number of instances of a text string.  
  
## Syntax  
  
```  
REPT(<text>, <num_times>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**text**|The text you want to repeat.|  
|**num_times**|A positive number specifying the number of times to repeat text.|  
  
## Property Value/Return Value  
A string containing the changes.  
  
## Remarks  
If **number_times** is 0 (zero), REPT returns a blank.  
  
If **number_times** is not an integer, it is truncated.  
  
The result of the REPT function cannot be longer than 32,767 characters, or REPT returns an error.  
  
## Example: Repeating Literal Strings  
  
### Description  
The following example returns the string, 85, repeated three times.  
  
### Code  
  
```  
=REPT("85",3)  
```  
  
## Example: Repeating Column Values  
  
### Description  
The following example returns the string in the column, [MyText], repeated for the number of times in the column, [MyNumber]. Because the formula extends for the entire column, the resulting string depends on the text and number value in each row.  
  
### Code  
  
```  
=REPT([MyText],[MyNumber])  
```  
  
### Comments  
  
|MyText|MyNumber|CalculatedColumn1|  
|----------|------------|---------------------|  
|Text|2|TextText|  
|Number|0||  
|85|3|858585|  
  
## See Also  
[Text Functions &#40;DAX&#41;](../DAX/text-functions-dax.md)  
  
