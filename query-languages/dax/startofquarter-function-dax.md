---
title: "STARTOFQUARTER function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/26/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# STARTOFQUARTER
Returns the first date of the quarter in the current context for the specified column of dates.  
  
## Syntax  
  
```dax
STARTOFQUARTER(<dates>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|dates|A column that contains dates.|  
  
## Return value  
A table containing a single column and single row with a date value.  
  
## Remarks  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column.  
  
-   A table expression that returns a single column of date/time values.  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [https://go.microsoft.com/fwlink/?LinkId=219172](https://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that returns the start of the quarter, for the current context.  
  
```dax
=STARTOFQUARTER(DateTime[DateKey])  
```
  
## See also  
[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[Time-intelligence functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[STARTOFYEAR function &#40;DAX&#41;](startofyear-function-dax.md)  
[STARTOFMONTH function &#40;DAX&#41;](startofmonth-function-dax.md)  
  
