---
title: "PREVIOUSQUARTER Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# PREVIOUSQUARTER Function (DAX)
Returns a table that contains a column of all dates from the previous quarter, based on the first date in the **dates** column, in the current context.  
  
## Syntax  
  
```dax
PREVIOUSQUARTER(<dates>)  
```
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|**dates**|A column containing dates.|  
  
## Return Value  
A table containing a single column of date values.  
  
## Remarks  
This function returns all dates from the previous quarter, using the first date in the input column. For example, if the first date in the **dates** argument refers to June 10, 2009,  this function returns all dates for the quarter January to March, 2009.  
  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column.  
  
-   A table expression that returns a single column of date/time values.  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE Function &#40;DAX&#41;](calculate-function-dax.md).  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [https://go.microsoft.com/fwlink/?LinkId=219172](https://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the 'previous quarter sales' for Internet sales.  
  
To see how this works, create a PivotTable and add the fields, CalendarYear and CalendarQuarter, to the **Row Labels** area of the PivotTable. Then add a measure, named **Previous Quarter Sales**, using the formula defined in the code section, to the **Values** area of the PivotTable.  
  
```dax
=CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), PREVIOUSQUARTER('DateTime'[DateKey]))  
```
  
## See Also  
[Time Intelligence Functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[PREVIOUSMONTH Function &#40;DAX&#41;](previousmonth-function-dax.md)  
[PREVIOUSDAY Function &#40;DAX&#41;](previousday-function-dax.md)  
[PREVIOUSYEAR Function &#40;DAX&#41;](previousyear-function-dax.md)  
[Get Sample Data](https://go.microsoft.com/fwlink/?LinkId=164474)  
  
