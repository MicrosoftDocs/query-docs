---
title: "DATESQTD function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/26/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# DATESQTD

Returns a table that contains a column of the dates for the quarter to date, in the current context.  
  
## Syntax  
  
```dax
DATESQTD(<dates>)  
```
  
### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|dates|A column that contains dates.|  
  
## Return value

A table containing a single column of date values.  
  
## Remarks

The **dates** argument can be any of the following:  
  
- A reference to a date/time column.  
  
- A table expression that returns a single column of date/time values.  
  
- A Boolean expression that defines a single-column table of date/time values.  
  
    > [!NOTE]  
    > Constraints on Boolean expressions are described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
- This function is not optimized for use in DirectQuery mode. To learn more, see  [DAX formula compatibility in DirectQuery mode](https://go.microsoft.com/fwlink/?LinkId=219172).
  
## Example

The following sample formula creates a measure that calculates the 'Quarterly Running Total' of Internet Sales.  
  
```dax
= CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), DATESQTD(DateTime[DateKey]))  
```
  
## See also

[Time-intelligence functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[DATESYTD function &#40;DAX&#41;](datesytd-function-dax.md)  
[DATESMTD function &#40;DAX&#41;](datesmtd-function-dax.md)