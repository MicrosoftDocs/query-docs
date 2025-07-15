---
description: "Learn more about: DATESBETWEEN"
title: "DATESBETWEEN function (DAX)"
---
# DATESBETWEEN

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

For date column input, returns a table that contains a column of dates that begins with a specified start date and continues until a specified end date.

For calendar input, returns a table that contains all primary tagged columns that begins with a specified start date and continues until a specified end date.

This function is suited to pass as a filter to the [CALCULATE](calculate-function-dax.md) function. Use it to filter an expression by a custom date range.

> [!NOTE]
> If you're working with standard date intervals such as days, months, quarters, or years,  it's recommended you use the better suited [DATESINPERIOD](datesinperiod-function-dax.md) function.

## Syntax

```dax
DATESBETWEEN(<dates> or <calendar>, <StartDate>, <EndDate>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates or calendar`|A column that contains dates or a calendar reference|
|`StartDate`|A date/day expression. For calendar, please use the same data type and string format as column that is tagged by Day.|
|`EndDate`|A date/day expression. For calendar, please use the same data type and string format as column that is tagged by Day.|

## Return value

For date column input, a table containing a single column of date values.
For calendar input, a table that contains all the tagged column for the dates between, in the current context.

## Remarks

- In the most common use case, `dates` is a reference to the date column of a marked date table.

- If `StartDate` is BLANK, then `StartDate` will be the earliest value in the `dates` column. For calendar, it will be the first value in column that is tagged as day.

- If `EndDate` is BLANK, then `EndDate` will be the latest value in the `dates` column. For calendar, it will be the last value in column that is tagged as day.

- Dates used as the `StartDate` and `EndDate` are inclusive. So, for example, if the `StartDate` value is July 1, 2019, then that date will be included in the returned table (providing the date exists in the `dates` column).

- For date column input, the returned table can only contain dates stored in the `Dates` column. So, for example, if the `Dates` column starts from July 1, 2017, and the `StartDate` value is July 1, 2016, the returned table will start from July 1, 2017.

- For calendar input, if the input date is not found in tagged day column, it will be treated as BLANK and thus the first/last value will be used.

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

## Example for calendar based time intelligence
The following **Sales** table measure definition uses the DATESBETWEEN function to produce a _life-to-date_ (LTD) calculation. Life-to-date represents the accumulation of a measure over time since the very beginning of time.

Notice that the formula uses the [MAX](max-function-dax.md) function. This function returns the max datekey that's in the filter context. So, the DATESBETWEEN function returns a table of dates beginning from the earliest date until the latest date being reported.The example use datekey as example to show that calendar could tag on column other than date type.

```dax
Customers LTD =
CALCULATE(
    DISTINCTCOUNT(Sales[CustomerKey]),
    DATESBETWEEN(
        FiscalCalendar,
        BLANK(),
        MAX('Date'[DateKey])
    )
)
```

## Related content

- [Time intelligence functions (DAX)](time-intelligence-functions-dax.md)
- [Date and time functions (DAX)](date-and-time-functions-dax.md)
- [DATESINPERIOD function (DAX)](datesinperiod-function-dax.md)
