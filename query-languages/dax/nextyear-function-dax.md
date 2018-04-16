---
title: "NEXTYEAR Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# NEXTYEAR Function (DAX)
Returns a table that contains a column of all dates in the next year, based on the first date in the **dates** column, in the current context.  
  
## Syntax  
  
```  
NEXTYEAR(<dates>[,<year_end_date>])  
```  
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|**dates**|A column containing dates.|  
|**year_end_date**|(optional) A literal string with a date that defines the year-end date. The default is December 31.|  
  
## Return Value  
A table containing a single column of date values.  
  
## Remarks  
This function returns all dates in the next year, based on the first date in the input column. For example, if the first date in the **dates** column refers to the year 2007, this function returns all dates for the year 2008.  
  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column.  
  
-   A table expression that returns a single column of date/time values.  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE Function &#40;DAX&#41;](calculate-function-dax.md).  
  
The **year_end_date** parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is ignored.  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the 'next year sales' for the Internet sales.  
  
To see how this works, create a PivotTable and add the fields, CalendarYear and CalendarQuarter, to the **Row Labels** area of the PivotTable. Then add a measure, named **Next Year Sales**, using the formula defined in the code section, to the **Values** area of the PivotTable.  
  
```  
=CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), NEXTYEAR('DateTime'[DateKey]))  
```  
  
## See Also  
[Time Intelligence Functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[NEXTDAY Function &#40;DAX&#41;](nextday-function-dax.md)  
[NEXTQUARTER Function &#40;DAX&#41;](nextquarter-function-dax.md)  
[NEXTMONTH Function &#40;DAX&#41;](nextmonth-function-dax.md)  
[Get Sample Data](http://go.microsoft.com/fwlink/?LinkId=164474)  
  
