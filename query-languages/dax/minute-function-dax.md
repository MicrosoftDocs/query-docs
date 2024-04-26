---
description: "Learn more about: MINUTE"
title: "MINUTE function (DAX) | Microsoft Docs"
---
# MINUTE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the minute as a number from 0 to 59, given a date and time value.  
  
## Syntax  
  
```dax
MINUTE(<datetime>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|datetime|A **datetime** value or text in an accepted time format, such as 16:48:00 or 4:48 PM.|  
  
## Return value

An integer number from 0 to 59.  
  
## Remarks

- In contrast to Microsoft Excel, which stores dates and times in a serial numeric format, DAX uses a **datetime** data type for dates and times. You can provide the **datetime** value to the MINUTE function by referencing a column that stores dates and times, by using a date/time function, or by using an expression that returns a date and time.  
  
- When the **datetime** argument is a text representation of the date and time, the function uses the locale and date/time settings of the client computer to understand the text value in order to perform the conversion. Most locales use the colon (:) as the time separator and any input text using colons as time separators will parse correctly. Verify your locale settings to understand your results.  
  
## Example 1

The following example returns the minute from the value stored in the **TransactionTime** column of the **Orders** table.  
  
```dax
= MINUTE(Orders[TransactionTime])  
```
  
## Example 2

The following example returns 45, which is the number of minutes in the time 1:45 PM.  
  
```dax
= MINUTE("March 23, 2008 1:45 PM")  
```
  
## Related content

[Date and time functions](date-and-time-functions-dax.md)  
[HOUR function](hour-function-dax.md)  
[YEAR function](year-function-dax.md)  
[SECOND function](second-function-dax.md)  
