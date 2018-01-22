---
title: "YEAR Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.YEAR.f1"
helpviewer_keywords: 
  - "YEAR function"
ms.assetid: 7ec0e0da-e209-4d7a-9f91-83540b43fb03
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# YEAR Function (DAX)
Returns the year of a date as a four digit integer in the range 1900-9999.  
  
## Syntax  
  
```  
YEAR(<date>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**date**|A date in **datetime** or text format, containing the year you want to find.|  
  
## Return Value  
An integer in the range 1900-9999.  
  
## Remarks  
In contrast to Microsoft Excel, which stores dates as serial numbers, DAX uses a **datetime** data type to work with dates and times.  
  
Dates should be entered by using the DATE function, or as results of other formulas or functions. You can also enter dates in accepted text representations of a date, such as March 3, 2007, or Mar-3-2003.  
  
Values returned by the YEAR, MONTH, and DAY functions will be Gregorian values regardless of the display format for the supplied date value. For example, if the display format of the supplied date uses the Hijri calendar, the returned values for the YEAR, MONTH, and DAY functions will be values associated with the equivalent Gregorian date.  
  
When the date argument is a text representation of the date, the function uses the locale and date time settings of the client computer to understand the text value in order to perform the conversion. Errors may arise if the format of strings is incompatible with the current locale settings. For example, if your locale defines dates to be formatted as month/day/year, and the date is provided as day/month/year, then 25/1/2009 will not be interpreted as January 25th of 2009 but as an invalid date.  
  
## Example  
The following example returns 2007.  
  
```  
=YEAR("March 2007")  
```  
  
## Example: Date as Result of Expression  
  
### Description  
The following example returns the year for today's date.  
  
### Code  
  
```  
=YEAR(TODAY())  
```  
  
## See Also  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[HOUR Function &#40;DAX&#41;](hour-function-dax.md)  
[MINUTE Function &#40;DAX&#41;](minute-function-dax.md)  
[YEAR Function &#40;DAX&#41;](year-function-dax.md)  
[SECOND Function &#40;DAX&#41;](second-function-dax.md)  
  
