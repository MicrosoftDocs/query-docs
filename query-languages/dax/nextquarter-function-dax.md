---
description: "Learn more about: NEXTQUARTER"
title: "NEXTQUARTER function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# NEXTQUARTER

Returns a table that contains a column of all dates in the next quarter, based on the first date specified in the **dates** column, in the current context.  
  
## Syntax  
  
```dax
NEXTQUARTER(<dates>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|dates|A column containing dates.|  
  
## Return value

A table containing a single column of date values.  
  
## Remarks

- This function returns all dates in the next quarter, based on the first date in the input parameter. For example, if the first date in the **dates** column refers to June 10, 2009, this function returns all dates for the quarter July to September, 2009.  
  
- The **dates** argument can be any of the following:  
  - A reference to a date/time column.  
  - A table expression that returns a single column of date/time values.  
  - A Boolean expression that defines a single-column table of date/time values.  
  
- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)] 
  
## Example

The following sample formula creates a measure that calculates the 'next quarter sales' for Internet sales.  
  
```dax
= CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), NEXTQUARTER('DateTime'[DateKey]))  
```
  
## See also

[Time intelligence functions](time-intelligence-functions-dax.md)  
[Date and time functions](date-and-time-functions-dax.md)  
[NEXTDAY function](nextday-function-dax.md)  
[NEXTMONTH function](nextmonth-function-dax.md)  
[NEXTYEAR function](nextyear-function-dax.md)  
