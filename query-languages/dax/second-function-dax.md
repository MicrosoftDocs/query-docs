---
description: "Learn more about: SECOND"
title: "SECOND function (DAX) | Microsoft Docs"
---
# SECOND

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the seconds of a time value, as a number from 0 to 59.  
  
## Syntax  
  
```dax
SECOND(<time>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|time|A time in **datetime** format, such as 16:48:23 or 4:48:47 PM.|  
  
## Return value

An integer number from 0 to 59.  
  
## Remarks

- In contrast to Microsoft Excel, which stores dates and times as serial numbers, DAX uses a **datetime** format when working with dates and times. If the source data is not in this format, DAX implicitly converts the data. You can use formatting to display the dates and times as a serial number of you need to.  
  
- The date/time value that you supply as an argument to the SECOND function can be entered as a text string within quotation marks (for example, "6:45 PM"). You can also provide a time value as the result of another expression, or as a reference to a column that contains times.  
  
- If you provide a numeric value of another data type, such as 13.60, the value is interpreted as a serial number and is represented as a **datetime** data type before extracting the value for seconds. To make it easier to understand your results, you might want to represent such numbers as dates before using them in the SECOND function. For example, if you use SECOND with a column that contains a numeric value such as, **25.56**, the formula returns 24. That is because, when formatted as a date, the value 25.56 is equivalent to January 25, 1900, 1:26:24 PM.  
  
- When the **time** argument is a text representation of a date and time, the function uses the locale and date/time settings of the client computer to understand the text value in order to perform the conversion. Most locales use the colon (:) as the time separator and any input text using colons as time separators will parse correctly. Review your locale settings to understand your results.  
  
## Example 1

The following formula returns the number of seconds in the time contained in the **TransactionTime** column of a table named **Orders**.  
  
```dax
= SECOND('Orders'[TransactionTime])  
```
  
## Example 2

The following formula returns 3, which is the number of seconds in the time represented by the value, **March 3, 2008 12:00:03**.  
  
```dax
= SECOND("March 3, 2008 12:00:03")  
```
  
## Related content

[Date and time functions](date-and-time-functions-dax.md)  
[HOUR](hour-function-dax.md)  
[MINUTE](minute-function-dax.md)  
[YEAR](year-function-dax.md)  
