---
title: "PREVIOUSQUARTER function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/26/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# PREVIOUSQUARTER
Returns a table that contains a column of all dates from the previous quarter, based on the first date in the **dates** column, in the current context.  
  
## Syntax  
  
```dax
PREVIOUSQUARTER(<dates>)  
```
  
### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|dates|A column containing dates.|  
  
## Return value  
A table containing a single column of date values.  
  
## Remarks  
This function returns all dates from the previous quarter, using the first date in the input column. For example, if the first date in the **dates** argument refers to June 10, 2009,  this function returns all dates for the quarter January to March, 2009.  
  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column.  
  
-   A table expression that returns a single column of date/time values.  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [https://go.microsoft.com/fwlink/?LinkId=219172](https://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the 'previous quarter sales' for Internet sales.  
  
```dax
=CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), PREVIOUSQUARTER('DateTime'[DateKey]))  
```
  
## See also  
[Time-intelligence functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[PREVIOUSMONTH function &#40;DAX&#41;](previousmonth-function-dax.md)  
[PREVIOUSDAY function &#40;DAX&#41;](previousday-function-dax.md)  
[PREVIOUSYEAR function &#40;DAX&#41;](previousyear-function-dax.md)  
 
  
