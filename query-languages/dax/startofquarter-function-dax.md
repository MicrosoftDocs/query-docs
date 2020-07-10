---
title: "STARTOFQUARTER function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# STARTOFQUARTER

Returns the first date of the quarter in the current context for the specified column of dates.  
  
## Syntax  
  
```dax
STARTOFQUARTER(<dates>)  
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
  
- This function is not optimized for use in DirectQuery mode. To learn more, see  [DAX formula compatibility in DirectQuery mode](https://go.microsoft.com/fwlink/?LinkId=219172).
  
## Example

The following sample formula creates a measure that returns the start of the quarter, for the current context.  
  
```dax
= STARTOFQUARTER(DateTime[DateKey])  
```
  
## See also
[Date and time functions](date-and-time-functions-dax.md)  
[Time intelligence functions](time-intelligence-functions-dax.md)  
[STARTOFYEAR](startofyear-function-dax.md)  
[STARTOFMONTH](startofmonth-function-dax.md)  
