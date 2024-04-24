---
description: "Learn more about: DATESMTD"
title: "DATESMTD function (DAX) | Microsoft Docs"
---
# DATESMTD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table that contains a column of the dates for the month to date, in the current context.  
  
## Syntax  
  
```dax
DATESMTD(<dates>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|dates|A column that contains dates.|  
  
## Return value

A table containing a single column of date values.  
  
## Remarks

The **dates** argument can be any of the following:  
  
- A reference to a date/time column.  
  
- A table expression that returns a single column of date/time values.  
  
- A Boolean expression that defines a single-column table of date/time values.  
  
    > [!NOTE]  
    > Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following sample formula creates a measure that calculates the 'Month To Date Total' for Internet Sales.  
  
```dax
= CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), DATESMTD(DateTime[DateKey]))  
```
  
## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)  
[Date and time functions](date-and-time-functions-dax.md)  
[DATESYTD function](datesytd-function-dax.md)  
[DATESQTD function](datesqtd-function-dax.md)
