---
description: "Learn more about: PREVIOUSDAY"
title: "PREVIOUSDAY function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# PREVIOUSDAY
Returns a table that contains a column of all dates representing the day that is previous to the first date in the **dates** column, in the current context.  
  
## Syntax  
  
```dax
PREVIOUSDAY(<dates>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|dates|A column containing dates.|  
  
## Return value

A table containing a single column of date values.  
  
## Remarks

- This function determines the first date in the input parameter, and then returns all dates corresponding to the day previous to that first date. For example, if the first date in the **dates** argument refers to June 10, 2009; this function returns all dates equal to June 9, 2009.  
  
- The **dates** argument can be any of the following:  
  - A reference to a date/time column.  
  - A table expression that returns a single column of date/time values.  
  - A Boolean expression that defines a single-column table of date/time values.  
  
- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following sample formula creates a measure that calculates the 'previous day sales' for Internet sales.  
  
```dax
= CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), PREVIOUSDAY('DateTime'[DateKey]))  
```
  
## See also

[Time intelligence functions](time-intelligence-functions-dax.md)  
[Date and time functions](date-and-time-functions-dax.md)  
[PREVIOUSMONTH function](previousmonth-function-dax.md)  
[PREVIOUSQUARTER function](previousquarter-function-dax.md)  
[PREVIOUSYEAR function](previousyear-function-dax.md)  
  
