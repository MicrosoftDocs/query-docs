---
description: "Learn more about: DATESINPERIOD"
title: "DATESINPERIOD function (DAX)"
ms.topic: reference
---
# DATESINPERIOD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

For date column input, returns a table that contains a column of dates that begins with a specified start date and continues for the specified number and type of date intervals.

For calendar input, returns a table that begins with a specified start date and continues for the specified number and type of date intervals. The table contains all primary tagged columns and all time related columns.

This function is suited to pass as a filter to the [CALCULATE](calculate-function-dax.md) function. Use it to filter an expression by standard date intervals such as days, months, quarters, or years.

## Syntax

```
DATESINPERIOD(<dates> or <calendar>, <start_date>, <number_of_intervals>, <interval>[, <endbehavior>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates or calendar`|A column that contains dates or a calendar reference|
|`start_date`|A date expression. If calendar syntax is used, please use the same data type as the primary column tagged to the Day category.|
|`number_of_intervals`|An integer that specifies the number of intervals to add to, or subtract from, the dates.|
|`interval`|The interval by which to shift the dates. The value for interval can be one of the following: `DAY`, `WEEK`, `MONTH`, `QUARTER`, and `YEAR`. Week could only be used with calendar.|
|`endbehavior`| Only applicable when a calendar reference is provided. Optional. Controls how the end date is aligned when the destination interval is longer than the source span. Valid values are: PRECISE (default) and ENDALIGNED.|

## Return value

For date column input, a table containing a single column of date values.  
For calendar input, a table that contains all primary tagged columns and all time related columns.

## Remarks

- In the most common use case, `dates` is a reference to the date column of a marked date table.

- If the number specified for `number_of_intervals` is positive, dates are moved forward in time; if the number is negative, dates are shifted backward in time.

- The `interval` parameter is an enumeration. Valid values are `DAY`, `WEEK`, `MONTH`, `QUARTER`, and `YEAR`. Because it's an enumeration, values aren't passed in as strings. So don't enclose them within quotation marks.

- When `endbehavior` is provided (calendar time intelligence only), DATESINPERIOD forwards the value to DATEADD's `Extension` parameter. See [Understanding endbehavior](#understanding-endbehavior-parameter-for-calendar-time-intelligence) for detailed examples.

- For date column input, the returned table can only contain dates stored in the `dates` column. So, for example, if the `dates` column starts from July 1, 2017, and the `start_date` value is July 1, 2016, the returned table will start from July 1, 2017.

- For calendar input, if the input date is not found in tagged day column, the result will be undefined. Please provide valid date input.

- For calendar input, use the same data type and format as the tagged day column for the start date. For example, if the column uses the format YYYY-Sn-Qn-Mnn-Wnn-Dnn (e.g., "2014-S2-Q4-M11-W45-D03"), the start date must follow the same format (e.g., "2015-S2-Q4-M11-W45-D03"). Otherwise, the behavior is undefined.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following **Sales** table measure definition uses the DATESINPERIOD function to calculate revenue for the prior year (PY).

Notice the formula uses the [MAX](max-function-dax.md) function. This function returns the latest date that's in the filter context. So, the DATESINPERIOD function returns a table of dates beginning from the latest date for the last year.

[!INCLUDE [power-bi-dax-sample-model](includes/power-bi-dax-sample-model.md)]

```dax
Revenue PY =
CALCULATE (
    SUM ( Sales[Sales Amount] ),
    DATESINPERIOD ( 'Date'[Date], MAX ( 'Date'[Date] ), -1, YEAR )
)
```

Consider that the report is filtered by the month of June 2020. The MAX function returns June 30, 2020. The DATESINPERIOD function then returns a date range from July 1, 2019 until June 30, 2020. It's a year of date values starting from June 30, 2020 for the last year.

## Example for calendar based time intelligence

The following **Sales** table measure definition uses the DATESINPERIOD function to calculate revenue for the prior year (PY).

Notice the formula uses the [MAX](max-function-dax.md) function. This function returns the latest date that's in the filter context. So, the DATESINPERIOD function returns primary columns beginning from latest date for the last year. DateKey is used as an example to show that the "Day" category can be tagged with a column that is not date-typed.

[!INCLUDE [power-bi-dax-sample-model](includes/power-bi-dax-sample-model.md)]

```dax
Revenue PY =
CALCULATE (
    SUM ( Sales[Sales Amount] ),
    DATESINPERIOD ( FiscalCalendar, MAX ( 'Date'[DateKey] ), -1, YEAR )
)
```

Consider that the report is filtered by the month of June 2020. The MAX function returns June 30, 2020. The DATESINPERIOD function then returns a range from July 1, 2019 until June 30, 2020. It's a year  starting from June 30, 2020 for the last year.

## Understanding endbehavior parameter for calendar time intelligence

Internally, DATESINPERIOD computes the ending boundary by calling DATEADD with the same interval, number of intervals, and `endbehavior` that were passed into DATESINPERIOD. When `number_of_intervals` is negative (common when rolling a window backward), the function returns the range `(endDate, startDate]`, where `endDate` is the date returned by DATEADD after it shifts the calendar context that ends on `startDate` by `<number_of_intervals>` `<interval>` using `<endbehavior>`. For positive values, the returned interval is `[startDate, endDate)`.

- `PRECISE` keeps the exact value returned by DATEADD.
- `ENDALIGNED` follows the DATEADD `EndAligned` semantics, moving the boundary to the end of the destination period when the source selection already reached its own end. This is useful when the filter context already ends on the last day of a period and you want a backward-looking window (for example, six months) to use the last day of the shifted period as its boundary.

### Example with EndAligned

```dax
EndAlignedTest =
    CALCULATE (
        COUNTROWS ( SUMMARIZE ( Sales, 'Date'[MonthName] ) ),
        DATESINPERIOD ( 'Gregorian Calendar', MAX ( 'Date'[Date] ), -6, MONTH, EndAligned )
    )
```

This measure counts the distinct month names in the last six months relative to the current context. With `EndAligned`, the window keeps the boundary at the end of the shifted month when the context already ends on a month boundary, preventing the additional trailing dates that `Precise` would include (for example, `Feb 28` would otherwise shift to `Aug 28`, pulling in `Aug 29–31` and effectively expanding the span to seven months). The `EndAligned` setting keeps the count at six in that scenario.

The following comparison assumes the current filter context ends on **February&nbsp;28, 2023** and the expression calls `DATESINPERIOD(..., -6, MONTH, <endbehavior>)`. The functional range is `(endDate, startDate]`, so the `endDate` returned by DATEADD is excluded while `startDate` is included.

| endbehavior | `DATEADD` endDate | DATESINPERIOD range | Month names returned by the measure |
|-------------|-------------------|---------------------|--------------------------------------|
| `Precise`   | 2022-08-28        | `(2022-08-28, 2023-02-28]` → Aug&nbsp;29&nbsp;2022 – Feb&nbsp;28&nbsp;2023 | Aug, Sep, Oct, Nov, Dec, Jan, Feb (7) |
| `EndAligned`| 2022-08-31        | `(2022-08-31, 2023-02-28]` → Sep&nbsp;1&nbsp;2022 – Feb&nbsp;28&nbsp;2023 | Sep, Oct, Nov, Dec, Jan, Feb (6) |

## Differences in behavior between classic and calendar time intelligence
Internally, DATESINPERIOD uses the same logic as DATEADD to determine the end date from the start date, and then calculates the range. Some scenarios may yield different results when comparing classic and calendar time intelligence. For example, in a lunar year, DATEADD produces different results at the date granularity, so the result of DATESINPERIOD will differ as well. In calendar-based time intelligence, shifting Feb 29 2008 back one year results in Mar 1 2007, because it is treated as the 60th day of the year. In classic time intelligence, the same shift returns Feb 28 2007. Because the end date differs, the output of DATESINPERIOD will also differ. The workaround is to use DATEADD(Calendar, -<number of a year>, month) to calculate end date. For example, if a year has 13 months in calendar, use DATEADD(Calendar, -13, month). This approach will shift by month so Feb 2008 will go to Feb 2007. Then, write a custom datesInPeriod based on the new end date.

## Related content

[Time intelligence functions (DAX)](time-intelligence-functions-dax.md)
[Date and time functions (DAX)](date-and-time-functions-dax.md)
[DATESBETWEEN function (DAX)](datesbetween-function-dax.md)
