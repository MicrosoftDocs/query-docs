---
title: "DATESMTD Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DATESMTD Function (DAX)
Returns a table that contains a column of the dates for the month to date, in the current context.  
  
## Syntax  
  
```  
DATESMTD(<dates>)  
```  
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|**dates**|A column that contains dates.|  
  
## Property Value/Return Value  
A table containing a single column of date values.  
  
## Remarks  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column.  
  
-   A table expression that returns a single column of date/time values.  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE Function &#40;DAX&#41;](calculate-function-dax.md).  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the 'Month To Date Total' for the Internet sales.  
  
To see how this works, create a PivotTable and add the fields, CalendarYear, MonthNumberOfYear and DayNumberOfMonth, to the **Row Labels** area of the PivotTable. Then add a measure, named **Month To Date Total**, using the formula defined in the code section, to the **Values** area of the PivotTable.  
  
```  
=CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), DATESMTD(DateTime[DateKey]))  
```  
  
## See Also  
[Time Intelligence Functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[DATESYTD Function &#40;DAX&#41;](datesytd-function-dax.md)  
[DATESQTD Function &#40;DAX&#41;](datesqtd-function-dax.md)  
[Get Sample Data](http://go.microsoft.com/fwlink/?LinkId=164474)  
  
