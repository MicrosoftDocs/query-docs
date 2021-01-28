---
description: "Learn more about: PREVIOUSMONTH"
title: "PREVIOUSMONTH function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# PREVIOUSMONTH

Returns a table that contains a column of all dates from the previous month, based on the first date in the **dates** column, in the current context.  
  
## Syntax  
  
```dax
PREVIOUSMONTH(<dates>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Dates|A column containing dates.|  
  
## Return value

A table containing a single column of date values.  
  
## Remarks

- This function returns all dates from the previous month, using the first date in the column used as input. For example, if the first date in the **dates** argument refers to June 10, 2009, this function returns all dates for the month of May, 2009.  
  
- The **dates** argument can be any of the following:  
  - A reference to a date/time column.  
  - A table expression that returns a single column of date/time values.  
  - A Boolean expression that defines a single-column table of date/time values.  
  
- Constraints on Boolean expressions are described in the topic, [CALCULATE](calculate-function-dax.md).  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following sample formula creates a measure that calculates the 'previous month sales' for Internet sales.  

```dax
= CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), PREVIOUSMONTH('DateTime'[DateKey]))  
```
  
## See also

[Time intelligence functions](time-intelligence-functions-dax.md)  
[Date and time functions](date-and-time-functions-dax.md)  
[PREVIOUSDAY](previousday-function-dax.md)  
[PREVIOUSQUARTER](previousquarter-function-dax.md)  
[PREVIOUSYEAR](previousyear-function-dax.md)  
