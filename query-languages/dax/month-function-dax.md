---
title: "MONTH Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# MONTH Function (DAX)
Returns the month as a number from 1 (January) to 12 (December).  
  
## Syntax  
  
```dax
MONTH(<datetime>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**date**|A date in **datetime** or text format.|  
  
## Return Value  
An integer number from 1 to 12.  
  
## Remarks  
In contrast to Microsoft Excel, which stores dates as serial numbers, DAX uses a **datetime** format when working with dates. You can enter the date used as argument to the MONTH function by typing an accepted **datetime** format, by providing a reference to a column that contains dates, or by using an expression that returns a date.  
  
Values returned by the YEAR, MONTH and DAY functions will be Gregorian values regardless of the display format for the supplied date value. For example, if the display format of the supplied date is Hijri, the returned values for the YEAR, MONTH and DAY functions will be values associated with the equivalent Gregorian date.  
  
When the date argument is a text representation of the date, the function uses the locale and date time settings of the client computer to understand the text value in order to perform the conversion. If the current date time settings represent a date in the format of Month/Day/Year, then the following string "1/8/2009" is interpreted as a datetime value equivalent to January 8th of 2009, and the function yields a result of 1. However, if the current date time settings represent a date in the format of Day/Month/Year, then the same string would be interpreted as a datetime value equivalent to August 1st of 2009, and the function yields a result of 8.  
  
If the text representation of the date cannot be correctly converted to a datetime value, the function returns an error.  
  
## Example  
The following expression returns 3, which is the integer corresponding to March, the month in the **date** argument.  
  
```dax
=MONTH("March 3, 2008 3:45 PM")  
```
  
## Example  
The following expression returns the month from the date in the **TransactionDate** column of the **Orders** table.  
  
```dax
=MONTH(Orders[TransactionDate])  
```
  
## See Also  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[HOUR Function &#40;DAX&#41;](hour-function-dax.md)  
[MINUTE Function &#40;DAX&#41;](minute-function-dax.md)  
[YEAR Function &#40;DAX&#41;](year-function-dax.md)  
[SECOND Function &#40;DAX&#41;](second-function-dax.md)  
  
