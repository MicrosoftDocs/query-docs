---
description: "Learn more about: Durations in Power Query M"
title: "Durations in Power Query M"
ms.date: 8/6/2025
ms.topic: language-reference
ms.custom: "nonautomated-date"
ms.subservice: m-background
---

# Duration support in Power Query M

A duration in Power Query M represents the difference between two points in time, expressed in days, hours, minutes, and seconds. Whether you're calculating the time between customer interactions, filtering records based on elapsed time, or building dynamic time-based logic, durations are essential for creating robust and intelligent data models.

This article explores the structure, creation, and manipulation of durations in Power Query M. It includes practical examples and shares tips to help you use durations effectively in your own data workflows.

## Create a duration

A duration is defined by the `#duration(<days>, <hours>, <minutes>, <seconds>)` function. For example, `#duration(2, 3, 0, 0)` represents a duration of 2 days and 3 hours. Power Query M provides several ways to create a duration, depending on the context and the level of precision required.

### Use the #duration function

The most direct way to create a duration is with the `#duration(<days>, <hours>, <minutes>, <seconds>)` syntax. Each argument must be a number, and the result is a duration value.

`#duration(2, 5, 30, 0)  // 2 days, 5 hours, 30 minutes`

This function supports fractional seconds as well:

`#duration(0, 0, 0, 1.75)  // 1.75 seconds`

### Create durations from date and time values

Durations can also be created by subtracting one date and time value from another. The result is a duration representing the time span between the two.

```powerquery-m
let
    Source = 
    {
        #date(2025, 7, 24) - #date(2025, 7, 23),
        // Result: #duration(1, 0, 0, 0)
        #time(12, 0, 0) - #time(11, 30, 30),
        // Result: #duration(0, 0, 29, 30)
        #datetime(2025, 7, 24, 12, 0, 0) - #datetime(2025, 7, 23, 12, 0, 0),
        // Result: #duration(1, 0, 0, 0)
        #datetimezone(2025, 7, 24, 12, 0, 0, 7, 0) - #datetimezone(2025, 7, 23, 10, 30, 0, 4, 0),
        // Result: #duration(0, 22, 30, 0)
        #datetime(2025, 7, 24, 12, 0, 0) - DateTime.From(#date(2025, 7, 23))
        // Result: #duration(1, 12, 0, 0)
    }
in
    Source
```

> [!NOTE]
> Subtracting one date and time type from a different date and time type (for example, subtracting a `date` value from a `datetime` value) results in an error. If you must use different date and time types to determine a duration, use the [Date.From](date-from.md), [DateTime.From](datetime-from.md), [DateTimeZone.From](datetimezone-from.md), or [Time.From](time-from.md) functions to explicitly change one of the date and time types.

### Convert from compatible values

The [Duration.From](duration-from.md) function can convert compatible values into durations. For more information, go to [Duration.From(value)](#durationfromvalue).

## Work with durations

Once a duration is created in Power Query M, it can be manipulated using various operations and functions. These capabilities make durations highly versatile for time-based logic and calculations.

### Arithmetic operations

Durations support standard arithmetic operations:

* Addition and subtraction: Add or subtract durations to or from each other or from date and time values.

  ```powerquery-m
  let
      Source = {
          #duration(1, 2, 0, 0) + #duration(0, 3, 30, 0),
          // Result: #duration(1, 5, 30, 0)
          #duration(1, 2, 0, 0) - #duration(0, 3, 30, 0),
          // Result: #duration(0, 22, 30, 0)
          #datetime(2025, 7, 24, 12, 0, 0) + #duration(0, 2, 0, 0),
          // Result: #datetime(2025, 7, 24, 14, 0, 0)
          #datetime(2025, 7, 24, 12, 0, 0) - #duration(0, 2, 0, 0),
          // Result: #datetime(2025, 7, 24, 10, 0, 0)
          #time(12, 0, 0) - #duration(0, 3, 30, 0)
          // Result: #time(8, 30, 0)
      }
  in
      Source
  ```

* Negation: A duration can be negated to reverse its direction.

  ```powerquery-m
  let
      Source = {
          #datetime(2025, 7, 24, 12, 0, 0) + -#duration(0, 2, 0, 0),
          // Result (subtracts two hours): #datetime(2025, 7, 24, 10, 0, 0)
          #datetime(2025, 7, 23, 12, 0, 0) - #datetime(2025, 7, 24, 12, 0, 0)
          // Result: -#duration(1, 0, 0, 0)
      }
  in
      Source
  ```

### Multiplication and division

Durations can be multiplied or divided by numeric values:

```powerquery-m
let
    Source = {
        #duration(0, 2, 0, 0) * 2,
        // Result (4 hours): #duration(0, 4, 0, 0)
        #duration(1, 0, 0, 0) / 2
        // Result (12 hours): #duration(0, 12, 0, 0)
    }
in
    Source
```

This calculation is useful for scaling durations or averaging time intervals.

### Comparisons

Durations can be compared using standard comparison operators:

```powerquery-m
let
    Source = #duration(1, 0, 0, 0) > #duration(0, 23, 59, 59)
        // Result: true
in
    Source
```

This calculation allows durations to be used in conditional logic, such as filtering rows based on elapsed time.

### Type compatibility

Durations are compatible with date and time values in arithmetic expressions but not interchangeable with them. For example, subtracting two date and time values yields a `duration`, but adding two date and time values is invalid.

```powerquery-m
let
    Source = 
    {
        #datetime(2025, 7, 24, 12, 0, 0) - #datetime(2025, 7, 23, 12, 0, 0),
        // Result: #duration(1, 0, 0, 0)
        #datetime(2025, 7, 24, 12, 0, 0) + #datetime(2025, 7, 23, 12, 0, 0)
        // Result: Error
    }
in
    Source
```

## Duration functions in M

Power Query M includes a set of built-in functions for working with durations. These functions allow for conversion, extraction of components, and aggregation of duration values, making them essential tools for time-based transformations.

### Duration.From(value)

The [Duration.From](duration-from.md) function converts a compatible value into a duration. Compatible values consist of either a number that's interpreted as a fraction of a day or a textual representation of a duration. Go to [Duration.FromText](duration-fromtext.md) for information about the textual representation formats.

```powerquery-m
let
    Source =
    {
        Duration.From(1.5),
        // Result: 1.5 days = #duration(1, 12, 0, 0)
        Duration.From("2.05:55:20.242")
        // Result: #duration(2, 5, 55, 20.242)
    }
in
    Source
```

### Component accessors

These functions extract specific parts of a duration:

* `Duration.Days(<duration>)`

  Returns the number of whole days in the duration.

* `Duration.Hours(<duration>)`

  Returns the number of hours beyond the whole days.

* `Duration.Minutes(<duration>)`

  Returns the number of minutes beyond the whole hours.

* `Duration.Seconds(<duration>)`

  Returns the number of seconds beyond the whole minutes.

```powerquery-m
let
    Source = #duration(2, 5, 30, 45),
    TextFormat = Text.Format(
        "Duration = #{0} days, #{1} hours, #{2} minutes, and #{3} seconds.",
        {
            Duration.Days(Source), 
            Duration.Hours(Source), 
            Duration.Minutes(Source), 
            Duration.Seconds(Source)
        }
    )
    // Results: "Duration = 2 days, 5 hours, 30 minutes, and 45 seconds."
in
    TextFormat
```

### Total value functions

These functions return the total value of a duration in a single unit, including fractional parts:

* `Duration.TotalDays(<duration>)`
* `Duration.TotalHours(<duration>)`
* `Duration.TotalMinutes(<duration>)`
* `Duration.TotalSeconds(<duration>)`

```powerquery-m
let
    Source = 
    {
        Duration.TotalDays(#duration(1, 12, 0, 0)),    // 1.5 days
        Duration.TotalHours(#duration(1, 12, 0, 0)),   // 36 hours
        Duration.TotalMinutes(#duration(1, 12, 0, 0)), // 2160 minutes
        Duration.TotalSeconds(#duration(1, 12, 0, 0))  // 129600 seconds
    }
in
    Source
```

## Duration normalization

In most cases, duration is composed of days, hours (maximum 23 hours), minutes (maximum 59 minutes), and seconds (maximum 59.9999999 seconds). However, in some cases you might exceed the maximum values in the duration parameters. In this case, Power Query M automatically normalizes these values:

* Seconds overflow into minutes
* Minutes overflow into hours
* Hours overflow into days

For example, suppose you have a column that provides the start date and time for a running process. In addition, you have a column that shows how long it took for the process to complete, in seconds. You want to create a third column that shows the date and time that the process completes.

```powerquery-m
let
    Source = #table(type table[StartTime = datetime, Seconds = Int64.Type],
    {
        {#datetime(2025, 7, 25, 8, 0, 0), 5400},
        {#datetime(2025, 7, 25, 13, 15, 0), 86400},
        {#datetime(2025, 7, 24, 22, 30, 0), 172800}
    }),
    AddSeconds = Table.AddColumn(
        Source, 
        "EndTime", 
        each [StartTime] + #duration(0, 0, 0, [Seconds]), 
        type datetime
    )
in
    AddSeconds
```

The following table is the result of these calculations.

:::image type="content" source="media/durations/add-seconds-for-duration.png" alt-text="Screenshot of the table containing the end date and time column derived from the start time and duration in seconds.":::

So, even though you only had the number of seconds that a process took place, Power Query M rolls that duration value up into minutes, hours, and days when the result is evaluated.

## Represent weeks, months, and years

Since durations are based on fixed units (days, hours, minutes, seconds), there's no native concept of weeks, months, or years, which vary in length. A `duration` type in Power Query M is a fixed structure that doesn’t account for calendar rules. For accurate duration spans over months or years, subtract one date and time from another instead of using fixed durations. This approach correctly handles leap years, varying month lengths, and daylight savings time (DST). However, also note that some date and time behavior might differ depending on whether the query runs locally (on Power Query Desktop) or online (on Power Query Online). For details, go to [Local, fixed, and UTC variants of current date and time](m-local-fixed-utc-variants.md). In general, avoid relying on fixed durations for long-term calculations.
