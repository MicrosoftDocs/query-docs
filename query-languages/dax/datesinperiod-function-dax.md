---
title: "DATESINPERIOD Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 9/25/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DATESINPERIOD Function (DAX)
Returns a table that contains a column of dates that begins with the **start_date** and continues for the specified **number_of_intervals**.  
  
## Syntax  
  
```dax
DATESINPERIOD(<dates>,<start_date>,<number_of_intervals>,<interval>)  
```
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|**dates**|A column that contains dates.|  
|**start_date**|A date expression.|  
|**number_of_intervals**|An integer that specifies the number of intervals to add to or subtract from the dates.|  
|**interval**|The interval by which to shift the dates. The value for interval can be one of the following: `year`, `quarter`, `month`, `day`|  
  
## Return Value  
A table containing a single column of date values.  
  
## Remarks  
The **dates** argument can be a reference to a date/time column.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE Function &#40;DAX&#41;](calculate-function-dax.md).  
  
If the number specified for **number_of_intervals** is positive, the dates are moved forward in time; if the number is negative, the dates are shifted back in time.  
  
The **interval** parameter is an enumeration, not a set of strings; therefore values should not be enclosed in quotation marks. Also, the values: `year`, `quarter`, `month`, `day` should be spelled in full when using them.  
  
The result table includes only dates that appear in the values of the underlying table column.  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following formula returns the Internet sales for the 21 days prior to August 24, 2007.  
  
```dax
= CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]),DATESINPERIOD(DateTime[DateKey],DATE(2007,08,24),-21,day))  
```
  
## See Also  
[Time Intelligence Functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[DATESBETWEEN Function &#40;DAX&#41;](datesbetween-function-dax.md)  
[Get Sample Data](http://go.microsoft.com/fwlink/?LinkId=164474)  
  
