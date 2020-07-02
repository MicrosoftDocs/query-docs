---
title: "DATESBETWEEN function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/26/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# DATESBETWEEN
Returns a table that contains a column of dates that begins with the **start_date** and continues until the **end_date**.  
  
## Syntax  
  
```dax
DATESBETWEEN(<dates>,<start_date>,<end_date>)  
```
  
### Parameters  
  
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
  
This function is not optimized for use in DirectQuery mode. To learn more, see  [DAX formula compatibility in DirectQuery mode](https://go.microsoft.com/fwlink/?LinkId=219172). 
  
## Example  
The following sample formula creates a measure that calculates the 'Summer 2007 sales' for Internet Sales.  
  
```dax
=CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), DATESBETWEEN(DateTime[DateKey],  
    DATE(2007,6,1),  
    DATE(2007,8,31)  
  ))  
```
  
## See also  
[Time-intelligence functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[DATESINPERIOD function &#40;DAX&#41;](datesinperiod-function-dax.md)  
  
