---
title: "PREVIOUSMONTH Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: Minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# PREVIOUSMONTH Function (DAX)
Returns a table that contains a column of all dates from the previous month, based on the first date in the **dates** column, in the current context.  
  
## Syntax  
  
```  
PREVIOUSMONTH(<dates>)  
```  
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|**Dates**|A column containing dates.|  
  
## Return Value  
A table containing a single column of date values.  
  
## Remarks  
This function returns all dates from the previous month, using the first date in the column used as input. For example, if the first date in the **dates** argument refers to June 10, 2009, this function returns all dates for the month of May, 2009.  
  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column.  
  
-   A table expression that returns a single column of date/time values.  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE Function &#40;DAX&#41;](calculate-function-dax.md).  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the 'previous month sales' for the Internet sales.  
  
To see how this works, create a PivotTable and add the fields, CalendarYear and MonthNumberOfYear, to the **Row Labels** area of the PivotTable. Then add a measure, named **Previous Month Sales**, using the formula defined in the code section, to the **Values** area of the PivotTable.  
  
```  
=CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), PREVIOUSMONTH('DateTime'[DateKey]))  
```  
  
## See Also  
[Time Intelligence Functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[PREVIOUSDAY Function &#40;DAX&#41;](previousday-function-dax.md)  
[PREVIOUSQUARTER Function &#40;DAX&#41;](previousquarter-function-dax.md)  
[PREVIOUSYEAR Function &#40;DAX&#41;](previousyear-function-dax.md)  
[Get Sample Data](http://go.microsoft.com/fwlink/?LinkId=164474)  
  
