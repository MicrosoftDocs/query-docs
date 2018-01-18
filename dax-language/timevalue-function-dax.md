---
title: "TIMEVALUE Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.TIMEVALUE.f1"
helpviewer_keywords: 
  - "TIMEVALUE function"
ms.assetid: fdb6bd3f-0403-4093-8837-ad8cf0bc87e5
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# TIMEVALUE Function (DAX)
Converts a time in text format to a time in datetime format.  
  
## Syntax  
  
```  
TIMEVALUE(time_text)  
```  
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|**time_text**|A text string that that represents a certain time of the day. Any date information included in the **time_text** argument is ignored.|  
  
## Return Value  
A date (**datetime**).  
  
## Remarks  
Time values are a portion of a date value and represented by a decimal number. For example, 12:00 PM is represented as 0.5 because it is half of a day.  
  
When the **time_text** argument is a text representation of the date and time, the function uses the locale and date/time settings of the client computer to understand the text value in order to perform the conversion. Most locales use the colon (:) as the time separator, and any input text using colons as time separators will parse correctly. Review your locale settings to understand your results.  
  
## Example  
  
```  
=TIMEVALUE("20:45:30")  
```  
  
## See Also  
[Date and Time Functions &#40;DAX&#41;](../DAX/date-and-time-functions-dax.md)  
  
