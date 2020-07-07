---
title: "SAMEPERIODLASTYEAR function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/26/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# SAMEPERIODLASTYEAR
Returns a table that contains a column of dates shifted one year back in time from the dates in the specified **dates** column, in the current context.  
  
## Syntax  
  
```dax
SAMEPERIODLASTYEAR(<dates>)  
```
  
### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|**dates**|A column containing dates.|  
  
## Property Value/Return value  
A single-column table of date values.  
  
## Remarks  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column,  
  
-   A table expression that returns a single column of date/time values,  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
The dates returned are the same as the dates returned by this equivalent formula:  
  
`DATEADD(dates, -1, year)`  
  
This function is not optimized for use in DirectQuery mode. To learn more, see  [DAX formula compatibility in DirectQuery mode](https://go.microsoft.com/fwlink/?LinkId=219172). 
  
## Example  
The following sample formula creates a measure that calculates the previous year sales of Reseller sales.  

```dax
=CALCULATE(SUM(ResellerSales_USD[SalesAmount_USD]), SAMEPERIODLASTYEAR(DateTime[DateKey]))  
```
  
## See also  
[Time intelligence functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[PREVIOUSYEAR function &#40;DAX&#41;](previousyear-function-dax.md)  
[PARALLELPERIOD function &#40;DAX&#41;](parallelperiod-function-dax.md)  
  
