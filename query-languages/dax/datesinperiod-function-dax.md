---
description: "Learn more about: DATESINPERIOD"
title: "DATESINPERIOD function (DAX) | Microsoft Docs"
---
# DATESINPERIOD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table that contains a column of dates that begins with a specified start date and continues for the specified number and type of date intervals.

This function is suited to pass as a filter to the [CALCULATE](calculate-function-dax.md) function. Use it to filter an expression by standard date intervals such as days, months, quarters, or years.

## Syntax

```dax
DATESINPERIOD(<dates>, <start_date>, <number_of_intervals>, <interval>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|dates|A date column.|
|start_date|A date expression.|
|number_of_intervals|An integer that specifies the number of intervals to add to, or subtract from, the dates.|
|interval|The interval by which to shift the dates. The value for interval can be one of the following: `DAY`, `MONTH`, `QUARTER`, and `YEAR`|

## Return value

A table containing a single column of date values.

## Remarks

- In the most common use case, **dates** is a reference to the date column of a marked date table.

- If the number specified for **number_of_intervals** is positive, dates are moved forward in time; if the number is negative, dates are shifted backward in time.

- The **interval** parameter is an enumeration. Valid values are `DAY`, `MONTH`, `QUARTER`, and `YEAR`. Because it's an enumeration, values aren't passed in as strings. So don't enclose them within quotation marks.

- The returned table can only contain dates stored in the **dates** column. So, for example, if the **dates** column starts from July 1, 2017, and the **start_date** value is July 1, 2016, the returned table will start from July 1, 2017.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following **Sales** table measure definition uses the DATESINPERIOD function to calculate revenue for the prior year (PY).

Notice the formula uses the [MAX](max-function-dax.md) function. This function returns the latest date that's in the filter context. So, the DATESINPERIOD function returns a table of dates beginning from the latest date for the last year.

[!INCLUDE [power-bi-dax-sample-model](includes/power-bi-dax-sample-model.md)]

```dax
Revenue PY =
CALCULATE(
    SUM(Sales[Sales Amount]),
    DATESINPERIOD(
        'Date'[Date],
        MAX('Date'[Date]),
        -1,
        YEAR
    )
)
```

Consider that the report is filtered by the month of June 2020. The MAX function returns June 30, 2020. The DATESINPERIOD function then returns a date range from July 1, 2019 until June 30, 2020. It's a year of date values starting from June 30, 2020 for the last year.

## Related content

[Time intelligence functions (DAX)](time-intelligence-functions-dax.md)  
[Date and time functions (DAX)](date-and-time-functions-dax.md)  
[DATESBETWEEN function (DAX)](datesbetween-function-dax.md)  
