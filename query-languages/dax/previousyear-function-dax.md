---
title: "PREVIOUSYEAR function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# PREVIOUSYEAR

Returns a table that contains a column of all dates from the previous year, given the last date in the **dates** column, in the current context.  
  
## Syntax  
  
```dax
PREVIOUSYEAR(<dates>[,<year_end_date>])  
```
  
### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|dates|A column containing dates.|  
|year_end_date|(optional) A literal string with a date that defines the year-end date. The default is December 31.|  
  
## Return value

A table containing a single column of date values.  
  
## Remarks

- This function returns all dates from the previous year given the latest date in the input parameter. For example, if the latest date in the **dates** argument refers to the year 2009, then this function returns all dates for the year of 2008, up to the specified **year_end_date**.  
  
- The **dates** argument can be any of the following:  
  - A reference to a date/time column.
  - A table expression that returns a single column of date/time values.
  - A Boolean expression that defines a single-column table of date/time values.  
  
- Constraints on Boolean expressions are described in the topic, [CALCULATE](calculate-function-dax.md).  
  
- The **year_end_date** parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is ignored.  
  
- This function is not optimized for use in DirectQuery mode. To learn more, see  [DAX formula compatibility in DirectQuery mode](https://go.microsoft.com/fwlink/?LinkId=219172).
  
## Example

The following sample formula creates a measure that calculates the previous year sales for Internet sales.  
  
```dax
= CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), PREVIOUSYEAR('DateTime'[DateKey]))  
```
  
## See also

[Time intelligence functions](time-intelligence-functions-dax.md)  
[Date and time functions](date-and-time-functions-dax.md)  
[PREVIOUSMONTH](previousmonth-function-dax.md)  
[PREVIOUSDAY](previousday-function-dax.md)  
[PREVIOUSQUARTER](previousquarter-function-dax.md)  
