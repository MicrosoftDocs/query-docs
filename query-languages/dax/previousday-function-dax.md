---
title: "PREVIOUSDAY Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# PREVIOUSDAY Function (DAX)
Returns a table that contains a column of all dates representing the day that is previous to the first date in the **dates** column, in the current context.  
  
## Syntax  
  
```  
PREVIOUSDAY(<dates>)  
```  
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|**dates**|A column containing dates.|  
  
## Return Value  
A table containing a single column of date values.  
  
## Remarks  
This function determines the first date in the input parameter, and then returns all dates corresponding to the day previous to that first date. For example, if the first date in the **dates** argument refers to June 10, 2009; this function returns all dates equal to June 9, 2009.  
  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column.  
  
-   A table expression that returns a single column of date/time values.  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE Function &#40;DAX&#41;](calculate-function-dax.md).  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the 'previous day sales' for the Internet sales.  
  
To see how this works, create a PivotTable and add the fields, CalendarYear and MonthNumberOfYear, to the **Row Labels** area of the PivotTable. Then add a measure, named **Previous Day Sales**, using the formula defined in the code section, to the **Values** area of the PivotTable.  
  
```  
=CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), PREVIOUSDAY('DateTime'[DateKey]))  
```  
  
## See Also  
[Time Intelligence Functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[PREVIOUSMONTH Function &#40;DAX&#41;](previousmonth-function-dax.md)  
[PREVIOUSQUARTER Function &#40;DAX&#41;](previousquarter-function-dax.md)  
[PREVIOUSYEAR Function &#40;DAX&#41;](previousyear-function-dax.md)  
  
