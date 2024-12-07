---
description: "Learn more about: HOUR"
title: "HOUR function (DAX) | Microsoft Docs"
---
# HOUR

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the hour as a number from 0 (12:00 A.M.) to 23 (11:00 P.M.).  
  
## Syntax  
  
```dax
HOUR(<datetime>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`datetime`|A `datetime` value, such as 16:48:00 or 4:48 PM.|  
  
## Return value

An integer number from 0 to 23.  

## Remarks

- The HOUR function takes as argument the time that contains the hour you want to find. You can supply the time by using a date/time function, an expression that returns a `datetime`, or by typing the value directly in one of the accepted time formats. Times can also be entered as any accepted text representation of a time.  
  
- When the `datetime` argument is a text representation of the date and time, the function uses the locale and date/time settings of the client computer to understand the text value in order to perform the conversion. Most locales use the colon (:) as the time separator and any input text using colons as time separators will parse correctly. Review your locale settings to understand your results.  
  
## Example 1

The following example returns the hour from the **TransactionTime** column of a table named **Orders**.  
  
```dax
= HOUR('Orders'[TransactionTime])  
```
  
## Example 2

The following example returns 15, meaning the hour corresponding to 3 PM in a 24-hour clock. The text value is automatically parsed and converted to a date/time value.  
  
```dax
= HOUR("March 3, 2008 3:00 PM")  
```
  
## Related content

[Date and time functions](date-and-time-functions-dax.md)  
[MINUTE function](minute-function-dax.md)  
[YEAR function](year-function-dax.md)  
[SECOND function](second-function-dax.md)  
