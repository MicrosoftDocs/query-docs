---
title: "TOTALQTD function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/26/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# TOTALQTD
Evaluates the value of the **expression** for the dates in the quarter to date, in the current context.  
  
## Syntax  
  
```dax
TOTALQTD(<expression>,<dates>[,<filter>])  
```
  
### Parameters  
  
|Parameter|Definition|  
|-------------|--------------|  
|expression|An expression that returns a scalar value.|  
|dates|A column that contains dates.|  
|filter|(optional) An expression that specifies a filter to apply to the current context.|  
  
## Return value  
A scalar value that represents the **expression** evaluated for all dates in the current quarter to date, given the dates in **dates**.  
  
## Remarks  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column.  
  
-   A table expression that returns a single column of date/time values.  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
> [!NOTE]  
> The **filter** expression has restrictions described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
>   
> This function is not optimized for use in DirectQuery mode. To learn more, see  [DAX formula compatibility in DirectQuery mode](https://go.microsoft.com/fwlink/?LinkId=219172).   
  
## Example  
The following sample formula creates a measure that calculates the 'quarter running total' or 'quarter running sum' for Internet sales.  
  
```dax
=TOTALQTD(SUM(InternetSales_USD[SalesAmount_USD]),DateTime[DateKey])  
```
  
## See also  
[ALL function &#40;DAX&#41;](all-function-dax.md)  
[CALCULATE function &#40;DAX&#41;](calculate-function-dax.md)  
[TOTALYTD function &#40;DAX&#41;](totalytd-function-dax.md)  
[TOTALMTD function &#40;DAX&#41;](totalmtd-function-dax.md)  
 
  
