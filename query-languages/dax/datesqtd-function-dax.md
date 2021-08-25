---
description: "Learn more about: DATESQTD"
title: "DATESQTD function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# DATESQTD

Returns a table that contains a column of the dates for the quarter to date, in the current context.  
  
## Syntax  
  
```dax
DATESQTD(<dates>)  
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

The following sample formula creates a measure that calculates the 'Quarterly Running Total' of Internet Sales.  
  
```dax
= CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), DATESQTD(DateTime[DateKey]))  
```
  
## See also

[Time intelligence functions](time-intelligence-functions-dax.md)  
[Date and time functions](date-and-time-functions-dax.md)  
[DATESYTD function](datesytd-function-dax.md)  
[DATESMTD function](datesmtd-function-dax.md)
