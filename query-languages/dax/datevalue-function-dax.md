---
description: "Learn more about: DATEVALUE"
title: "DATEVALUE function (DAX) | Microsoft Docs"
---
# DATEVALUE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Converts a date in text format to a date in datetime format.  
  
## Syntax  
  
```dax
DATEVALUE(date_text)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|date_text|Text that represents a date.|  
  
## Property Value/Return value  

A date in **datetime** format.  
  
## Remarks

- When converting, DATEVALUE uses the locale and date/time settings of the model to determine a date value. If the model date/time settings represent dates in the format of Month/Day/Year, then the string, "1/8/2009", is converted to a **datetime** value equivalent to January 8th of 2009. However, if the model date/time settings represent dates in the format of Day/Month/Year, the same string is converted as a **datetime** value equivalent to August 1st of 2009.  

- If conversion using the locale and date/time settings of the model fails, DATEVALUE will attempt to use other date formats. In this case, some rows may be converted using one format and other rows are converted using a different format. For example, "5/4/2018" may convert to May 4th of 2018, and "20/4/2018" may convert to April 20th. 
  
- If the year portion of the **date_text** argument is omitted, the DATEVALUE function uses the current year from your computer's built-in clock. Time information in the **date_text** argument is ignored.  

- Model locale and data/time settings are initially determined by the application and computer when the model is created.

- Date and datetime can also be specified as a literal in the format `dt"YYYY-MM-DD"`, `dt"YYYY-MM-DDThh:mm:ss"`, or `dt"YYYY-MM-DD hh:mm:ss"`. When specified as a literal, using the DATEVALUE function in the expression is not necessary. To learn more, see [DAX Syntax | Date and time](dax-syntax-reference.md#date-and-time).

## Example  

The following example returns a different **datetime** value depending on the model locale and settings for how dates and times are presented.  
  
- In date/time settings where the day precedes the month, the example returns a **datetime** value corresponding to January 8th of 2009.  
  
- In date/time settings where the month precedes the day, the example returns a **datetime** value corresponding to August 1st of 2009.  
  
```dax
= DATEVALUE("8/1/2009")  
```
  
## Related content

[Date and time functions](date-and-time-functions-dax.md)  
