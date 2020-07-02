---
title: "FIRSTDATE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/26/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# FIRSTDATE
Returns the first date in the current context for the specified column of dates.  
  
## Syntax  
  
```dax
FIRSTDATE(<dates>)  
```
  
### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|dates|A column that contains dates.|  
  
## Return value  
A table containing a single column and single row with a date value.  
  
## Remarks  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column.  
  
-   A table expression that returns a single column of date/time values,.  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
When the current context is a single date, the date returned by the FIRSTDATE and LASTDATE functions will be equal.  
  
The Return value is a table that contains a single column and single value. Therefore, this function can be used as an argument to any function that requires a table in its arguments. Also, the returned value can be used whenever a date value is required.  
  
This function is not optimized for use in DirectQuery mode. To learn more, see  [DAX formula compatibility in DirectQuery mode](https://go.microsoft.com/fwlink/?LinkId=219172). 
  
## Example  
The following sample formula creates a measure that obtains the first date when a sale was made in the Internet sales channel for the current context.  
  
```dax
=FIRSTDATE('InternetSales_USD'[SaleDateKey])  
```
  
## See also  
[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[Time-intelligence functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[LASTDATE function &#40;DAX&#41;](lastdate-function-dax.md)  
[FIRSTNONBLANK function &#40;DAX&#41;](firstnonblank-function-dax.md)  
 
  
