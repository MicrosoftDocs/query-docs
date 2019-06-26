---
title: "YEAR function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/26/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# YEAR
Returns the year of a date as a four digit integer in the range 1900-9999.  
  
## Syntax  
  
```dax
YEAR(<date>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|date|A date in **datetime** or text format, containing the year you want to find.|  
  
## Return value  
An integer in the range 1900-9999.  
  
## Remarks  
In contrast to Microsoft Excel, which stores dates as serial numbers, DAX uses a **datetime** data type to work with dates and times.  
  
Dates should be entered by using the DATE function, or as results of other formulas or functions. You can also enter dates in accepted text representations of a date, such as March 3, 2007, or Mar-3-2003.  
  
Values returned by the YEAR, MONTH, and DAY functions will be Gregorian values regardless of the display format for the supplied date value. For example, if the display format of the supplied date uses the Hijri calendar, the returned values for the YEAR, MONTH, and DAY functions will be values associated with the equivalent Gregorian date.  
  
When the date argument is a text representation of the date, the function uses the locale and date time settings of the client computer to understand the text value in order to perform the conversion. Errors may arise if the format of strings is incompatible with the current locale settings. For example, if your locale defines dates to be formatted as month/day/year, and the date is provided as day/month/year, then 25/1/2009 will not be interpreted as January 25th of 2009 but as an invalid date.  
  
## Example  
The following example returns 2007.  
  
```dax
=YEAR("March 2007")  
```  
  
## Example - Date as result of expression  
  
### Description  
The following example returns the year for today's date.  
  
```dax
=YEAR(TODAY())  
```  
  
## See also  
[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[HOUR function &#40;DAX&#41;](hour-function-dax.md)  
[MINUTE function &#40;DAX&#41;](minute-function-dax.md)  
[YEAR function &#40;DAX&#41;](year-function-dax.md)  
[SECOND function &#40;DAX&#41;](second-function-dax.md)  
  
