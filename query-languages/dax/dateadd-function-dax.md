---
description: "Learn more about: DATEADD"
title: "DATEADD function (DAX) | Microsoft Docs"
---
# DATEADD

Returns a table that contains a column of dates, shifted either forward or backward in time by the specified number of intervals from the dates in the current context.  
  
## Syntax  
  
```dax
DATEADD(<dates>,<number_of_intervals>,<interval>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|dates|A column that contains dates.|  
|number_of_intervals|An integer that specifies the number of intervals to add to or subtract from the dates.|  
|interval|The interval by which to shift the dates. The value for interval can be one of the following: `year`, `quarter`, `month`, `day`|  
  
## Return value

A table containing a single column of date values.  
  
## Remarks

The **dates** argument can be any of the following:  
  
- A reference to a date/time column,  
  
- A table expression that returns a single column of date/time values,  
  
- A Boolean expression that defines a single-column table of date/time values.  
  
    > [!NOTE]  
    > Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).  
  
- If the number specified for **number_of_intervals** is positive, the dates in **dates** are moved forward in time; if the number is negative, the dates in **dates** are shifted back in time.  
  
- The **interval** parameter is an enumeration, not a set of strings; therefore values should not be enclosed in quotation marks. Also, the values: `year`, `quarter`, `month`, `day` should be spelled in full when using them.  
  
- The result table includes only dates that exist in the **dates** column.  

- If the dates in the current context do not form a contiguous interval, the function returns an error.
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example - Shifting a set of dates  
  
The following formula calculates dates that are one year before the dates in the current context.  

```dax
= DATEADD(DateTime[DateKey],-1,year)  
```
  
## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)  
[Date and time functions](date-and-time-functions-dax.md)
