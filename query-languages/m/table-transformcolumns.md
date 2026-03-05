---
description: "Learn more about: Table.TransformColumns"
title: "Table.TransformColumns"
ms.subservice: m-source
ms.topic: reference
---
# Table.TransformColumns

## Syntax

<pre>
Table.TransformColumns(
    <b>table</b> as table,
    <b>transformOperations</b> as list,
    optional <b>defaultTransformation</b> as nullable function,
    optional <b>missingField</b> as nullable number
) as table
</pre>
  
## About

Transforms the specified table by applying each column operation in a list.

* `table`: The table to transform.
* `transformOperations`: The transformations to make to the table. The format of this parameter is either { column name, transformation } or { column name, transformation, new column type }.
* `defaultTransformation`: (Optional) The default transformation applied to all columns not listed in `transformOperations`.
* `missingField`: (Optional) Specifies the expected action for missing values. If a column listed in `transformOperations` doesn't exist, an error is raised (`MissingField.Error`) unless this parameter specifies an alternative. Use one of the following values:
  * `MissingField.UseNull`: Any missing fields are included as `null` values.
  * `MissingField.Ignore`: Any missing fields are ignored.

## Example 1

Convert the text values in column [A] to number values, and the number values in column [B] to text values.

**Usage**

```powerquery-m
Table.TransformColumns(
    Table.FromRecords({
        [A = "1", B = 2],
        [A = "5", B = 10]
    }),
    {
        {"A", Number.FromText},
        {"B", Text.From}
    }
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [A = 1, B = "2"],
    [A = 5, B = "10"]
})
```

## Example 2

Convert the number values in missing column [X] to text values, defaulting to `null` on columns that don't exist.

**Usage**

```powerquery-m
Table.TransformColumns(
    Table.FromRecords({
        [A = "1", B = 2],
        [A = "5", B = 10]
    }),
    {"X", Number.FromText},
    null,
    MissingField.UseNull
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [A = "1", B = 2, X = null],
    [A = "5", B = 10, X = null]
})
```

## Example 3

Increment the number values in column [B] and convert them to text values, and convert all other columns to numbers.

**Usage**

```powerquery-m
Table.TransformColumns(
    Table.FromRecords({
        [A = "1", B = 2],
        [A = "5", B = 10]
    }),
    {"B", each Text.From(_ + 1), type text},
    Number.FromText
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [A = 1, B = "3"],
    [A = 5, B = "11"]
})
```

## Example 4

Move scheduled maintenance tasks that occur on a US holiday to the next day or, if the holiday occurs on a Friday, to the next Monday.

**Usage**

```powerquery-m
let
    MaintenanceSchedule = #table(type table [Task = text, Date = date],
    {
        {"HVAC Check", #date(2025, 7, 10)},         // Not a holiday
        {"Window Washing", #date(2025, 9, 1)},      // Labor Day
        {"Fire Drill", #date(2025, 9, 17)},         // Not a holiday
        {"Light Replacement", #date(2025, 11, 27)}  // Thanksgiving
    }),
    USHolidays = {
        #date(2025, 1, 1),   // New Year's Day
        #date(2025, 7, 4),   // Independence Day
        #date(2025, 9, 1),   // Labor Day
        #date(2025, 11, 27), // Thanksgiving
        #date(2025, 12, 25)  // Christmas
    },
    AdjustedSchedule = Table.TransformColumns(
        MaintenanceSchedule,
        {{"Date", each if List.Contains(USHolidays, _) then
            if Date.DayOfWeek(_, Day.Sunday) = 5 then
                Date.AddDays(_, 3)     // Friday to Monday
            else 
                Date.AddDays(_, 1)     // Other to next day
        else _, type date}}
    )
in
    AdjustedSchedule
```

**Output**

```powerquery-m
#table(type table[Task = text, Date = date],
{
    {"HVAC Check", #date(2025, 7, 10)},
    {"Window Washing", #date(2025, 9, 2)},
    {"Fire Drill", #date(2025, 9, 17)},
    {"Light Replacement", #date(2025, 11, 28)}
})
```
