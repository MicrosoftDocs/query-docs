---
title: "DATESYTD function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# DATESYTD

Returns a table that contains a column of the dates for the year to date, in the current context.  
  
## Syntax  
  
```dax
DATESYTD(<dates> [,<year_end_date>])  
```
  
### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|dates|A column that contains dates.|  
|year_end_date|(optional) A literal string with a date that defines the year-end date. The default is December 31.|  
  
## Return value

A table containing a single column of date values.  
  
## Remarks

The **dates** argument can be any of the following:  
  
- A reference to a date/time column,  
  
- A table expression that returns a single column of date/time values,  
  
- A Boolean expression that defines a single-column table of date/time values.  
  
    > [!NOTE]  
    > Constraints on Boolean expressions are described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
- The **year_end_date** parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is ignored.  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following sample formula creates a measure that calculates the 'Running Total' for Internet sales.  
  
```dax
= CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), DATESYTD(DateTime[DateKey]))  
```
  
## See also

[Time intelligence functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[DATESMTD function &#40;DAX&#41;](datesmtd-function-dax.md)  
[DATESQTD function &#40;DAX&#41;](datesqtd-function-dax.md)