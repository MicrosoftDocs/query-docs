---
description: "Learn more about: DATESBETWEEN"
title: "DATESBETWEEN function (DAX) | Microsoft Docs"
---
# DATESBETWEEN

Returns a table that contains a column of dates that begins with a specified start date and continues until a specified end date.

This function is suited to pass as a filter to the [CALCULATE](calculate-function-dax.md) function. Use it to filter an expression by a custom date range.

> [!NOTE]
> If you're working with standard date intervals such as days, months, quarters, or years,  it's recommended you use the better suited [DATESINPERIOD](datesinperiod-function-dax.md) function.

## Syntax

```dax
DATESBETWEEN(<Dates>, <StartDate>, <EndDate>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|Dates|A date column.|
|StartDate|A date expression.|
|EndDate|A date expression.|

## Return value

A table containing a single column of date values.

## Remarks

- In the most common use case, **Dates** is a reference to the date column of a marked date table.

- If **StartDate** is BLANK, then **StartDate** will be the earliest value in the **Dates** column.

- If **EndDate** is BLANK, then **EndDate** will be the latest value in the **Dates** column.

- Dates used as the **StartDate** and **EndDate** are inclusive. So, for example, if the **StartDate** value is July 1, 2019, then that date will be included in the returned table (providing the date exists in the **Dates** column).

- The returned table can only contain dates stored in the **Dates** column. So, for example, if the **Dates** column starts from July 1, 2017, and the **StartDate** value is July 1, 2016, the returned table will start from July 1, 2017.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following **Sales** table measure definition uses the DATESBETWEEN function to produce a _life-to-date_ (LTD) calculation. Life-to-date represents the accumulation of a measure over time since the very beginning of time.

Notice that the formula uses the [MAX](max-function-dax.md) function. This function returns the latest date that's in the filter context. So, the DATESBETWEEN function returns a table of dates beginning from the earliest date until the latest date being reported.

[!INCLUDE [power-bi-dax-sample-model](includes/power-bi-dax-sample-model.md)]

```dax
Customers LTD =
CALCULATE(
    DISTINCTCOUNT(Sales[CustomerKey]),
    DATESBETWEEN(
        'Date'[Date],  
        BLANK(),  
        MAX('Date'[Date])  
    )
)
```

Consider that the earliest date stored in the **Date** table is July 1, 2017. So, when a report filters the measure by the month of June 2020, the DATESBETWEEN function returns a date range from July 1, 2017 until June 30, 2020.

## See also

- [Time intelligence functions (DAX)](time-intelligence-functions-dax.md)
- [Date and time functions (DAX)](date-and-time-functions-dax.md)
- [DATESINPERIOD function (DAX)](datesinperiod-function-dax.md)
