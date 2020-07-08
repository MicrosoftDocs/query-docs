---
title: "NEXTDAY function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# NEXTDAY

Returns a table that contains a column of all dates from the next day, based on the first date specified in the **dates** column in the current context.  
  
## Syntax  
  
```dax
NEXTDAY(<dates>)  
```
  
### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|dates|A column containing dates.|  
  
## Return value

A table containing a single column of date values.  
  
## Remarks

- This function returns all dates from the next day to the first date in the input parameter. For example, if the first date in the **dates** argument refers to June 10, 2009; then this function returns all dates equal to June 11, 2009.  
  
- The **dates** argument can be any of the following:  
  - A reference to a date/time column.  
  - A table expression that returns a single column of date/time values.  
  - A Boolean expression that defines a single-column table of date/time values.  

- Constraints on Boolean expressions are described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
- This function is not optimized for use in DirectQuery mode. To learn more, see  [DAX formula compatibility in DirectQuery mode](https://go.microsoft.com/fwlink/?LinkId=219172). 
  
## Example

The following sample formula creates a measure that calculates the 'next day sales' of Internet sales.  
  
```dax
= CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), NEXTDAY('DateTime'[DateKey]))  
```
  
## See also

[Time intelligence functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[NEXTQUARTER function &#40;DAX&#41;](nextquarter-function-dax.md)  
[NEXTMONTH function &#40;DAX&#41;](nextmonth-function-dax.md)  
[NEXTYEAR function &#40;DAX&#41;](nextyear-function-dax.md)  
