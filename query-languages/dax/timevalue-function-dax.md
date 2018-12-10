---
title: "TIMEVALUE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# TIMEVALUE function
Converts a time in text format to a time in datetime format.  
  
## Syntax  
  
```dax
TIMEVALUE(time_text)  
```
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|time_text|A text string that that represents a certain time of the day. Any date information included in the **time_text** argument is ignored.|  
  
## Return value  
A date (**datetime**).  
  
## Remarks  
Time values are a portion of a date value and represented by a decimal number. For example, 12:00 PM is represented as 0.5 because it is half of a day.  
  
When the **time_text** argument is a text representation of the date and time, the function uses the locale and date/time settings of the client computer to understand the text value in order to perform the conversion. Most locales use the colon (:) as the time separator, and any input text using colons as time separators will parse correctly. Review your locale settings to understand your results.  
  
## Example  
  
```dax
=TIMEVALUE("20:45:30")  
```
  
## See also  
[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
  
