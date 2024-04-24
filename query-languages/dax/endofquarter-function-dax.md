---
description: "Learn more about: ENDOFQUARTER"
title: "ENDOFQUARTER function (DAX) | Microsoft Docs"
---
# ENDOFQUARTER

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns the last date of the quarter in the current context for the specified column of dates.  
  
## Syntax  
  
```dax
ENDOFQUARTER(<dates>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|   
|dates|A column that contains dates.|  
  
## Return value

A table containing a single column and single row with a date value.  
  
## Remarks

- The **dates** argument can be any of the following:  
  - A reference to a date/time column,  
  - A table expression that returns a single column of date/time values,  
  - A Boolean expression that defines a single-column table of date/time values.  
  
- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following sample formula creates a measure that returns the end of the quarter, for the current context.  
  
```dax
= ENDOFQUARTER(DateTime[DateKey])  
```
  
## Related content

[Date and time functions](date-and-time-functions-dax.md)  
[Time intelligence functions](time-intelligence-functions-dax.md)  
[ENDOFYEAR function](endofyear-function-dax.md)  
[ENDOFMONTH function](endofmonth-function-dax.md)  
