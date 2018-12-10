---
title: "NEXTQUARTER function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# NEXTQUARTER
Returns a table that contains a column of all dates in the next quarter, based on the first date specified in the **dates** column, in the current context.  
  
## Syntax  
  
```dax
NEXTQUARTER(<dates>)  
```
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|dates|A column containing dates.|  
  
## Return value  
A table containing a single column of date values.  
  
## Remarks  
This function returns all dates in the next quarter, based on the first date in the input parameter. For example, if the first date in the **dates** column refers to June 10, 2009, this function returns all dates for the quarter July to September, 2009.  
  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column.  
  
-   A table expression that returns a single column of date/time values.  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [https://go.microsoft.com/fwlink/?LinkId=219172](https://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the 'next quarter sales' for the Internet sales.  
  
To see how this works, create a PivotTable and add the fields, CalendarYear and CalendarQuarter, to the **Row Labels** area of the PivotTable. Then add a measure, named **Next Quarter Sales**, using the formula defined in the code section to the **Values** area of the PivotTable.  
  
```dax
=CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), NEXTQUARTER('DateTime'[DateKey]))  
```
  
## See also  
[Time-intelligence functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[NEXTDAY function &#40;DAX&#41;](nextday-function-dax.md)  
[NEXTMONTH function &#40;DAX&#41;](nextmonth-function-dax.md)  
[NEXTYEAR function &#40;DAX&#41;](nextyear-function-dax.md)  
[Get Sample Data](https://go.microsoft.com/fwlink/?LinkId=164474)  
  
