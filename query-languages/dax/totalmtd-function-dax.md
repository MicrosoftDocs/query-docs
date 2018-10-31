---
title: "TOTALMTD Function (DAX) | Microsoft Docs"
ms.prod: powerbi 
ms.technology: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# TOTALMTD Function (DAX)
Evaluates the value of the **expression** for the month to date, in the current context.  
  
## Syntax  
  
```dax
TOTALMTD(<expression>,<dates>[,<filter>])  
```
  
#### Parameters  
  
|Parameter|Definition|  
|-------------|--------------|  
|**expression**|An expression that returns a scalar value.|  
|**dates**|A column that contains dates.|  
|**filter**|(optional) An expression that specifies a filter to apply to the current context.|  
  
## Return Value  
A scalar value that represents the **expression** evaluated for the dates in the current month-to-date, given the dates in **dates**.  
  
## Remarks  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column.  
  
-   A table expression that returns a single column of date/time values.  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE Function &#40;DAX&#41;](calculate-function-dax.md).  
  
> [!NOTE]  
> The **filter** expression has restrictions described in the topic, [CALCULATE Function &#40;DAX&#41;](calculate-function-dax.md).  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [https://go.microsoft.com/fwlink/?LinkId=219172](https://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the 'month running total' or 'month running sum' for the Internet sales.  
  
To see how this works, create a PivotTable and add the fields, CalendarYear, MonthNumberOfYear and DayNumberOfMonth, to the **Row Labels** area of the PivotTable. Then add a measure, named **Month-to-date Total**, using the formula defined in the code section, to the **Values** area of the PivotTable.  
  
## Code  
  
```dax
=TOTALMTD(SUM(InternetSales_USD[SalesAmount_USD]),DateTime[DateKey])  
```
  
## See Also  
[ALL Function &#40;DAX&#41;](all-function-dax.md)  
[CALCULATE Function &#40;DAX&#41;](calculate-function-dax.md)  
[TOTALYTD Function &#40;DAX&#41;](totalytd-function-dax.md)  
[TOTALQTD Function &#40;DAX&#41;](totalqtd-function-dax.md)  
[Get Sample Data](https://go.microsoft.com/fwlink/?LinkId=164474)  
  
