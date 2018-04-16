---
title: "SAMEPERIODLASTYEAR Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: Minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# SAMEPERIODLASTYEAR Function (DAX)
Returns a table that contains a column of dates shifted one year back in time from the dates in the specified **dates** column, in the current context.  
  
## Syntax  
  
```  
SAMEPERIODLASTYEAR(<dates>)  
```  
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|**dates**|A column containing dates.|  
  
## Property Value/Return Value  
A single-column table of date values.  
  
## Remarks  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column,  
  
-   A table expression that returns a single column of date/time values,  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE Function &#40;DAX&#41;](calculate-function-dax.md).  
  
The dates returned are the same as the dates returned by this equivalent formula:  
  
`DATEADD(dates, -1, year)`  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the previous year sales of the Reseller sales.  
  
To see how this works, create a PivotTable and add the fields, CalendarYear to the **Row Labels** area of the PivotTable. Then add a measure, named **Previous Year Sales**, using the formula defined in the code section, to the **Values** area of the PivotTable.  
  
```  
=CALCULATE(SUM(ResellerSales_USD[SalesAmount_USD]), SAMEPERIODLASTYEAR(DateTime[DateKey]))  
```  
  
## See Also  
[Time Intelligence Functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[PREVIOUSYEAR Function &#40;DAX&#41;](previousyear-function-dax.md)  
[PARALLELPERIOD Function &#40;DAX&#41;](parallelperiod-function-dax.md)  
  
