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
|`interval`|The interval by which to shift the dates. The value for interval can be one of the following: `year`, `quarter`, `month`, `week`, `day`. The week enum is only applicable when a calendar reference is provided.|
|`extension`|Only applicable when a calendar reference is provided. Define behavior when the original time period has fewer dates than the resulting time period. Valid values are: EXTENDING (Default), PRECISE. |
|`truncation`|Only applicable when a calendar reference is provided. Define behavior when the original time period has more dates than the resulting time period. Valid values are: BLANKS (Default), Anchored.|

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

## Behavior for calendar based DateAdd when selection is at a finer grain than the shift level

When calendar reference is used and the selection is at a finer grain than the shift level, an index-based approach is taken. To illustrate this behavior, let's consider the scenario where the selection is at the date level and DATEADD() is shifting by month. Here is what DateAdd will do:

- Determine the positions of the current selection within the month.  
For example, if the current selection spans March 3–10, the positions are from the 3rd to the 10th day of the month.

- Shift the month
Apply the month shift — e.g., a shift of +1 changes March to April.

- Return the same relative positions in the shifted month
Retrieve the 3rd to the 10th of the new month (e.g., April 3–10).

## Parameters for calendar based DateAdd when selection is at a finer grain than the shift level

When the selection granularity is **finer** than the shift unit (e.g., selecting individual dates while shifting by month), the **index-based behavior** can lead to **ambiguities**, especially across months of varying lengths. To handle these edge cases, two parameters are introduced:

### Extension parameter (for small → large month shifts):

Controls how the function behaves when the destination month is **longer** than the current one.

- **`Precise`**: Keeps the original date range strictly.  
  → `Feb 25–28` → `March 25–28`

- **`Extended`**: Allows the window to expand toward the **end of the month** if needed.  
  → `Feb 25–28` → `March 25–31`

### Truncation Parameter (for large → small month shifts)

Controls how the function behaves when the destination month is **shorter** than the current one.

- **`Anchored`**: Anchors the result to the **last valid date** of the smaller month.  
  → `March 31` → `Feb 28`

- **`Blank`**: Returns **blank** when the shifted date doesn't exist.  
  → `March 31` → _(blank)_ (since February doesn't have 31st)

## Example for calendar based time intelligence
The following formula calculates dates that are one year before the dates in the current context.

```dax
DATEADD ( FiscalCalendar, -1, YEAR )
```

## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)
[Date and time functions](date-and-time-functions-dax.md)
