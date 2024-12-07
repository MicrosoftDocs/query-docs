---
description: "Learn more about: TIMEVALUE"
title: "TIMEVALUE function (DAX) | Microsoft Docs"
---
# TIMEVALUE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Converts a time in text format to a time in datetime format.  
  
## Syntax  
  
```dax
TIMEVALUE(time_text)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`time_text`|A text string that that represents a certain time of the day. Any date information included in the `time_text` argument is ignored.|  
  
## Return value

A date (`datetime`).  
  
## Remarks

- Time values are a portion of a date value and represented by a decimal number. For example, 12:00 PM is represented as 0.5 because it is half of a day.  
  
- When the `time_text` argument is a text representation of the date and time, the function uses the locale and date/time settings of the model to understand the text value in order to perform the conversion. Most locales use the colon (:) as the time separator, and any input text using colons as time separators will parse correctly. Review your locale settings to understand your results.  

- Date and datetime can also be specified as a literal in the format `dt"YYYY-MM-DD"`, `dt"YYYY-MM-DDThh:mm:ss"`, or `dt"YYYY-MM-DD hh:mm:ss"`. When specified as a literal, using the TIMEVALUE function in the expression is not necessary. To learn more, see [DAX Syntax | Date and time](dax-syntax-reference.md#date-and-time).
  
## Example  
  
```dax
= TIMEVALUE("20:45:30")  
```
  
## Related content

[Date and time functions](date-and-time-functions-dax.md)  
