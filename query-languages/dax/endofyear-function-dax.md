---
title: "ENDOFYEAR function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/26/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ENDOFYEAR
Returns the last date of the year in the current context for the specified column of dates.  
  
## Syntax  
  
```dax
ENDOFYEAR(<dates> [,<year_end_date>])  
```
  
### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|dates|A column that contains dates.|  
|year_end_date|(optional) A literal string with a date that defines the year-end date. The default is December 31.|  
  
## Return value  
A table containing a single column and single row with a date value.  
  
## Remarks  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column,  
  
-   A table expression that returns a single column of date/time values,  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
The **year_end_date** parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is ignored.  
  
This function is not optimized for use in DirectQuery mode. To learn more, see  [DAX formula compatibility in DirectQuery mode](https://go.microsoft.com/fwlink/?LinkId=219172). 
  
## Example  
The following sample formula creates a measure that returns the end of the fiscal year that ends on June 30, for the current context.  

```dax
=ENDOFYEAR(DateTime[DateKey],"06/30/2004")  
```
  
## See also  
[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[Time-intelligence functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[ENDOFMONTH function &#40;DAX&#41;](endofmonth-function-dax.md)  
[ENDOFQUARTER function &#40;DAX&#41;](endofquarter-function-dax.md)  
  
