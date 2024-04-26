---
description: "Learn more about: STARTOFMONTH"
title: "STARTOFMONTH function (DAX) | Microsoft Docs"
---
# STARTOFMONTH

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]
Returns the first date of the month in the current context for the specified column of dates.  
  
## Syntax  
  
```dax
STARTOFMONTH(<dates>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|dates|A column that contains dates.|  
  
## Return value

A table containing a single column and single row with a date value.  
  
## Remarks

- The **dates** argument can be any of the following:  
  - A reference to a date/time column.  
  - A table expression that returns a single column of date/time values.
  - A Boolean expression that defines a single-column table of date/time values.  
  
- Constraints on Boolean expressions are described in the topic, [CALCULATE](calculate-function-dax.md).  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following sample formula creates a measure that returns the start of the month, for the current context.  
  
```dax
= STARTOFMONTH(DateTime[DateKey])  
```
  
## Related content

[Date and time functions](date-and-time-functions-dax.md)  
[Time intelligence functions](time-intelligence-functions-dax.md)  
[STARTOFYEAR](startofyear-function-dax.md)  
[STARTOFQUARTER](startofquarter-function-dax.md)  
