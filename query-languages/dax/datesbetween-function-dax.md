---
title: "DATESBETWEEN Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DATESBETWEEN Function (DAX)
Returns a table that contains a column of dates that begins with the **start_date** and continues until the **end_date**.  
  
## Syntax  
  
```dax
DATESBETWEEN(<dates>,<start_date>,<end_date>)  
```
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|dates|A reference to a date/time column.|  
|start_date|A date expression.|  
|end_date|A date expression.|  
  
## Return value  
A table containing a single column of date values.  
  
## Remarks  
If **start_date** is a blank date value, then **start_date** will be the earliest value in the **dates** column.  
  
If **end_date** is a blank date value, then **end_date** will be the latest value in the **dates** column.  
  
The dates used as the **start_date** and **end_date** are inclusive: that is, if the sales occurred on September 1 and you use September 1 as the start date, sales on September 1 are counted.  
  
> [!NOTE]  
> The DATESBETWEEN function is provided for working with custom date ranges. If you are working with common date intervals such as months, quarters, and years, we recommend that you use the appropriate function, such as DATESINPERIOD.  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [https://go.microsoft.com/fwlink/?LinkId=219172](https://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the 'Summer 2007 sales' for the Internet sales.  
  
To see how this works, create a PivotTable and add the field, CalendarYear, to the **Row Labels** area of the PivotTable. Then add a measure, named **Summer 2007 Sales**, using the formula as defined in the code section, to the **Values** area of the PivotTable.  
  
```dax
=CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), DATESBETWEEN(DateTime[DateKey],  
    DATE(2007,6,1),  
    DATE(2007,8,31)  
  ))  
```
  
## See Also  
[Time Intelligence Functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[DATESINPERIOD Function &#40;DAX&#41;](datesinperiod-function-dax.md)  
  
