---
title: "TOTALYTD Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# TOTALYTD Function (DAX)
Evaluates the year-to-date value of the **expression** in the current context.  
  
## Syntax  
  
```  
TOTALYTD(<expression>,<dates>[,<filter>][,<year_end_date>])  
```  
  
#### Parameters  
  
|Parameter|Definition|  
|-------------|--------------|  
|**expression**|An expression that returns a scalar value.|  
|**dates**|A column that contains dates.|  
|**filter**|(optional) An expression that specifies a filter to apply to the current context.|  
|**year_end_date**|(optional) A literal string with a date that defines the year-end date. The default is December 31.|  
  
## Return Value  
A scalar value that represents the **expression** evaluated for the current year-to-date **dates**.  
  
## Remarks  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column,  
  
-   A table expression that returns a single column of date/time values,  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE Function &#40;DAX&#41;](calculate-function-dax.md).  
  
> [!NOTE]  
> The **filter** expression has restrictions described in the topic, [CALCULATE Function &#40;DAX&#41;](calculate-function-dax.md).  
  
The **year_end_date** parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is not required and is ignored.  
  
For example, the following formula specifies a (fiscal) year_end_date of 6/30 in an EN-US locale workbook.  
  
```  
=TOTALYTD(SUM(InternetSales_USD[SalesAmount_USD]),DateTime[DateKey], ALL(‘DateTime’), “6/30”)  
```  
In this example, year_end_date can be specified as “6/30”, “Jun 30”, “30 June”, or any string that resolves to a month/day. However, it is recommended you specify year_end_date using “month/day” (as shown) to ensure the string resolves to a date.  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the 'year running total' or 'year running sum' for the Internet sales.  
  
To see how this works, create a PivotTable and add the fields, CalendarYear, CalendarQuarter, and MonthNumberOfYear, to the **Row Labels** area of the PivotTable. Then add a measure, named **Year-to-date Total**, using the formula defined in the code section, to the **Values** area of the PivotTable.  
  
## Code  
  
```  
=TOTALYTD(SUM(InternetSales_USD[SalesAmount_USD]),DateTime[DateKey])  
```  
  
## See Also  
[ALL Function &#40;DAX&#41;](all-function-dax.md)  
[CALCULATE Function &#40;DAX&#41;](calculate-function-dax.md)  
[DATESYTD Function &#40;DAX&#41;](datesytd-function-dax.md)  
[TOTALMTD Function &#40;DAX&#41;](totalmtd-function-dax.md)  
[TOTALQTD Function &#40;DAX&#41;](totalqtd-function-dax.md)  
[Get Sample Data](http://go.microsoft.com/fwlink/?LinkId=164474)  
  
