---
description: "Learn more about: DATESYTD"
title: "DATESYTD function (DAX) | Microsoft Docs"
---
# DATESYTD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table that contains a column of the dates for the year to date, in the current context.  
  
## Syntax  
  
```dax
DATESYTD(<dates> [,<year_end_date>])  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|dates|A column that contains dates.|  
|year_end_date|(optional) A literal string with a date that defines the year-end date. The default is December 31.|  
  
## Return value

A table containing a single column of date values.  
  
## Remarks

The **dates** argument can be any of the following:  
  
- A reference to a date/time column,  
  
- A table expression that returns a single column of date/time values,  
  
- A Boolean expression that defines a single-column table of date/time values.  
  
    > [!NOTE]  
    > Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).  
  
- The **year_end_date** parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is ignored.  Depending on locale, the format might be something like "m-dd" or "dd-m".
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following sample formula creates a measure that calculates the 'Running Total' for Internet sales.  
  
```dax
= CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), DATESYTD(DateTime[DateKey]))  
```

The following sample formula creates a measure that calculates the 'Fiscal Year Running Total' for Internet sales, using a US Locale for the Date format.  
  
```dax
= CALCULATE(
    SUM(InternetSales_USD[SalesAmount_USD]), 
    DATESYTD(DateTime[DateKey],
        "6-30"
        )
)
```
  
## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)  
[Date and time functions](date-and-time-functions-dax.md)  
[DATESMTD function](datesmtd-function-dax.md)  
[DATESQTD function](datesqtd-function-dax.md)
