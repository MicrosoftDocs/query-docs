---
description: "Learn more about: DATEADD"
title: "DATEADD function (DAX)"
---
# DATEADD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

If input is date column, returns a table that contains a column of dates, shifted either forward or backward in time by the specified number of intervals from the dates in the current context.  
If input is calendar, returns primary tagged columns shifted either forward or backward in time by the specified number of intervals, from the dates in the current context, based on the calendar.

## Syntax

```
DATEADD(<dates> or <calendar>, <number_of_intervals>, <interval>[,<Extension>],[,<Truncation>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates or calendar`|A column that contains dates or a calendar reference.|
|`number_of_intervals`|An integer that specifies the number of intervals to add to or subtract from the dates.|
|`interval`|The interval by which to shift the dates. The value for interval can be one of the following: `year`, `quarter`, `month`, `day`|
|`extension`|Only applies when using a calendar. Define behavior when the original time period has fewer dates than the resulting time period. Valid values are: EXTENDING, PRECISE.|
|`truncation`|Only applies when using a calendar. Define behavior when the original time period has more dates than the resulting time period. Valid values are: ANCHORED, BLANKS.|

## Return value

For date column input, a table containing a single column of date values.  
For calendar input, a table that contains all the tagged column for the shifted periods, in the current context.

## Remarks

The `dates` argument can be any of the following:

- A reference to a date/time column,

- A table expression that returns a single column of date/time values,

- A Boolean expression that defines a single-column table of date/time values.

    > [!NOTE]
    > Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).

- If the number specified for `number_of_intervals` is positive, the dates in `dates` are moved forward in time; if the number is negative, the dates in `dates` are shifted back in time.

- The `interval` parameter is an enumeration, not a set of strings; therefore values should not be enclosed in quotation marks. Also, the values: `year`, `quarter`, `month`, `day` should be spelled in full when using them.

- The result table includes only dates that exist in the `dates` column.

- When input is date column, there is contiguous check. In other words, if the dates in the current context do not form a contiguous interval, the function returns an error.

When input is calendar, below algorithm is executed when selection is on date level and shift by month:
- Firstly, index of current window is identified. For example, current dates are 3rd-10th of month.
- Secondly, month is shifted.
- Thirdly, 3rd-10th date of new month is returned.

In calendar scenario, the extension parameter controls behavior when it shift from small month to big month. Extending will get current dates toward the end of month. Precise will gets current dates only. Truncation enum controls behavior when big month goes to small month. Anchored will capture last date of month. For example, March 31 will go to Feb 28. For blanks, March 31 will get blank when it shifts to Feb.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example - Shifting a set of dates

The following formula calculates dates that are one year before the dates in the current context.

```dax
= DATEADD ( DateTime[DateKey], -1, YEAR )
```

## Special behavior when input is date column

When the selection includes the last two days of month, DATEADD will use "extension" semantics and will include the days till the end of month. For example, when Feb 27 and 28 of 2013 are included in the selection and a month is added, DATEADD will return March 27 to 31.

This behavior only happens when last two days of month are included in the selection. If only Feb 27 is selected, it will go to March 27.

```dax
= DATEADD(DateTime[DateKey], 1, month)
```

Calendar based time intelligence provides more control by two specific enums. Please check above remarks.

## Example for calendar based time intelligence
The following formula calculates dates that are one year before the dates in the current context.

```dax
DATEADD ( FiscalCalendar, -1, YEAR )
```

## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)
[Date and time functions](date-and-time-functions-dax.md)
