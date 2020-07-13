---
title: "ENDOFQUARTER function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ENDOFQUARTER

Returns the last date of the quarter in the current context for the specified column of dates.  
  
## Syntax  
  
```dax
ENDOFQUARTER(<dates>)  
```
  
### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|dates|A column that contains dates.|  
  
## Return value

A table containing a single column and single row with a date value.  
  
## Remarks

- The **dates** argument can be any of the following:  
  - A reference to a date/time column,  
  - A table expression that returns a single column of date/time values,  
  - A Boolean expression that defines a single-column table of date/time values.  
  
- Constraints on Boolean expressions are described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following sample formula creates a measure that returns the end of the quarter, for the current context.  
  
```dax
= ENDOFQUARTER(DateTime[DateKey])  
```
  
## See also

[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[Time intelligence functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[ENDOFYEAR function &#40;DAX&#41;](endofyear-function-dax.md)  
[ENDOFMONTH function &#40;DAX&#41;](endofmonth-function-dax.md)  
