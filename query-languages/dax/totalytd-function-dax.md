---
title: "TOTALYTD function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/26/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# TOTALYTD
Evaluates the year-to-date value of the **expression** in the current context.  
  
## Syntax  
  
```dax
TOTALYTD(<expression>,<dates>[,<filter>][,<year_end_date>])  
```
  
### Parameters  
  
|Parameter|Definition|  
|-------------|--------------|  
|expression|An expression that returns a scalar value.|  
|dates|A column that contains dates.|  
|filter|(optional) An expression that specifies a filter to apply to the current context.|  
|year_end_date|(optional) A literal string with a date that defines the year-end date. The default is December 31.|  
  
## Return value  
A scalar value that represents the **expression** evaluated for the current year-to-date **dates**.  
  
## Remarks  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column,  
  
-   A table expression that returns a single column of date/time values,  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
> [!NOTE]  
> The **filter** expression has restrictions described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
The **year_end_date** parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is not required and is ignored.  
  
For example, the following formula specifies a (fiscal) year_end_date of 6/30 in an EN-US locale workbook.  
  
```dax
=TOTALYTD(SUM(InternetSales_USD[SalesAmount_USD]),DateTime[DateKey], ALL(‘DateTime’), “6/30”)  
```

In this example, year_end_date can be specified as “6/30”, “Jun 30”, “30 June”, or any string that resolves to a month/day. However, it is recommended you specify year_end_date using “month/day” (as shown) to ensure the string resolves to a date.  
  
This function is not optimized for use in DirectQuery mode. To learn more, see  [DAX formula compatibility in DirectQuery mode](https://go.microsoft.com/fwlink/?LinkId=219172).   
  
## Example  
The following sample formula creates a measure that calculates the 'year running total' or 'year running sum' for Internet sales.  
  
```dax
=TOTALYTD(SUM(InternetSales_USD[SalesAmount_USD]),DateTime[DateKey])  
```
  
## See also  
[ALL function &#40;DAX&#41;](all-function-dax.md)  
[CALCULATE function &#40;DAX&#41;](calculate-function-dax.md)  
[DATESYTD function &#40;DAX&#41;](datesytd-function-dax.md)  
[TOTALMTD function &#40;DAX&#41;](totalmtd-function-dax.md)  
[TOTALQTD function &#40;DAX&#41;](totalqtd-function-dax.md)  
 
  
