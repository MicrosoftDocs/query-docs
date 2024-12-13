---
description: "Learn more about: CALENDAR"
title: "CALENDAR function (DAX)"
---
# CALENDAR

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]
  
Returns a table with a single column named "Date" that contains a contiguous set of dates. The range of dates is from the specified start date to the specified end date, inclusive of those two dates.  
  
## Syntax  
  
```dax
CALENDAR(<start_date>, <end_date>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`start_date`|Any DAX expression that returns a datetime value.|  
|`end_date`|Any DAX expression that returns a datetime value.|  
  
## Return value

Returns a table with a single column named "Date" containing a contiguous set of dates. The range of dates is from the specified start date to the specified end date, inclusive of those two dates.  
  
## Remarks

- An error is returned if start_date is greater than end_date.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Examples

The following formula returns a table with dates between January 1st, 2015 and December 31st, 2021.  
  
```dax
= CALENDAR (DATE (2015, 1, 1), DATE (2021, 12, 31))
```
  
For a data model which includes actual sales data and future sales forecasts, the following expression returns a date table covering the range of dates in both the Sales and Forecast tables.  
  
```dax
= CALENDAR (MINX (Sales, [Date]), MAXX (Forecast, [Date]))
```  
