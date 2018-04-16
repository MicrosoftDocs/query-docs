---
title: "DAY Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DAY Function (DAX)
Returns the day of the month, a number from 1 to 31.  
  
## Syntax  
  
```  
DAY(<date>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**date**|A date in **datetime** format, or a text representation of a date.|  
  
## Return Value  
An integer number indicating the day of the month.  
  
## Remarks  
The DAY function takes as an argument the date of the day you are trying to find. Dates can be provided to the function by using another date function, by using an expression that returns a date, or by typing a date in a **datetime** format. You can also type a date in one of the accepted string formats for dates.  
  
Values returned by the YEAR, MONTH and DAY functions will be Gregorian values regardless of the display format for the supplied date value. For example, if the display format of the supplied date is Hijri, the returned values for the YEAR, MONTH and DAY functions will be values associated with the equivalent Gregorian date.  
  
When the date argument is a text representation of the date, the day function uses the locale and date/time settings of the client computer to understand the text value in order to perform the conversion. If the current date/time settings represent dates in the format of Month/Day/Year, then the string, "1/8/2009", is interpreted as a **datetime** value equivalent to January 8th of 2009, and the function returns 8. However, if the current date/time settings represent dates in the format of Day/Month/Year, the same string would be interpreted as a **datetime** value equivalent to August 1st of 2009, and the function returns 1.  
  
## Example: Getting the Day from a Date Column  
  
### Description  
The following formula returns the day from the date in the column, [Birthdate].  
  
### Code  
  
```  
=DAY([Birthdate])  
```  
  
## Example: Getting the Day from a String Date  
  
### Description  
The following formulas return the day, 4, using dates that have been supplied as strings in an accepted text format.  
  
### Code  
  
```  
=DAY("3-4-1007")  
=DAY("March 4 2007")  
```  
  
## Example: Using a Day Value as a Condition  
  
### Description  
The following expression returns the day that each sales order was placed, and flags the row as a promotional sale item if the order was placed on the 10th of the month.  
  
### Code  
  
```  
=IF( DAY([SalesDate])=10,"promotion","")  
```  
  
## See Also  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[TODAY Function &#40;DAX&#41;](today-function-dax.md)  
[DATE Function &#40;DAX&#41;](date-function-dax.md)  
  
