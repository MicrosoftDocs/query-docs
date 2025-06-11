---
description: "Learn more about: Local, fixed, and UTC variants of current time functions"
title: "Local, fixed, and UTC variants of current time functions"
ms.topic: conceptual
ms.date: 6/11/2025
ms.custom: "nonautomated-date"
ms.subservice: m-background
---

# Local, fixed, and UTC variants of current time functions

When you work with Power Query in tools like Excel and Power BI, handling date and time values accurately is essential&mdash;especially when your data transformations depend on the current time. Power Query offers various functions to retrieve the current date and time:

* [DateTime.LocalNow](datetime-localnow.md)
* [DateTimeZone.LocalNow](datetimezone-localnow.md)
* [DateTime.FixedLocalNow](datetime-fixedlocalnow.md)
* [DateTimeZone.FixedLocalNow](datetimezone-fixedlocalnow.md)
* [DateTimeZone.UtcNow](datetimezone-utcnow.md)
* [DateTimeZone.FixedUtcNow](datetimezone-fixedutcnow.md).

This article explores the distinctions between these functions and clarifies when and why to use each one. In addition, it highlights a critical but often overlooked detail. Power Query Online always returns UTC time even when using a function labeled as "Local." Understanding these nuances can help you avoid unexpected results, especially when building time-sensitive reports or automating data updates in apps such as Power BI service or Power Apps.

## Differences between functions

Each of the current time functions have important differences. These functions vary in terms of time zone awareness, volatility (whether the value changes when called multiple times in the same query), and how they behave in different environments (desktop vs. online). The following table contains a breakdown of each function.

| Function                  | Returns         | Volatility | Desktop behavior                    | Online behavior       | Typical use case                                      |
|------------------------------|-----------------------------------------------|----------------|--------------------------------------------|--------------------------------------------------|-----------------------------------------------------------|
| `DateTime.LocalNow`          | A `datetime` representing the current local time          | Dynamic&mdash;returns a new value each time it's invoked during query evaluation       | Returns local machine time                 | Returns UTC time  | Quick local timestamp without time zone context          |
| `DateTimeZone.LocalNow`      | A `datetimezone` value representing the current local time with time zone offset     | Dynamic&mdash;returns a new value each time it's invoked during query evaluation       | Returns local time with offset             | Returns UTC time with `+00:00` offset            | Local time with time zone awareness                      |
| `DateTime.FixedLocalNow`     | A `datetime` value representing the local time when first invoked during query evaluation         | Fixed&mdash;returns the same value throughout a single query evaluation          | Captures local time when first called                | Captures UTC time when first called                        | Snapshot of local time without time zone                 |
| `DateTimeZone.FixedLocalNow` | A `datetimezone` value representing the local time with offset when first invoked during query evaluation     | Fixed&mdash;returns the same value throughout a single query evaluation          | Captures local time with offset when first called    | Captures UTC time with `+00:00` offset when first called   | Snapshot of local time with time zone                    |
| `DateTimeZone.UtcNow`        | A `datetimezone`  value representing the current UTC time     | Dynamic&mdash;returns a new value each time it's invoked during query evaluation        | Returns current UTC time                   | Returns current UTC time                         | Consistent UTC timestamp for dynamic scenarios           |
| `DateTimeZone.FixedUtcNow`   | A `datetimezone` value representing the UTC time when first invoked during query evaluation      | Fixed&mdash;returns the same value throughout a single query evaluation          | Captures UTC time when first called                  | Captures UTC time when first called                        | Fixed UTC timestamp for logging or auditing              |

In Power Query M, choosing between local time and UTC-based date and time functions is a critical design decision that affects the consistency, accuracy, and portability of your queries. Functions like `DateTime.LocalNow` and `DateTime.FixedLocalNow` are useful when your logic depends on the local system time, such as filtering for records that occurred "today" or generating timestamps for user-facing reports. These functions reflect the time zone of the environment in which the query is executed, making them suitable for Power Query Desktop scenarios where the local context is well-defined.

However, in distributed or cloud-based environments like Power Query Online, these same functions return UTC time, not the actual local time of the user. This discrepancy can lead to subtle inconsistencies if your logic assumes a local time context. In contrast, `DateTimeZone.UtcNow` and `DateTimeZone.FixedUtcNow` provide a time-zone-neutral reference point that is consistent across environments and unaffected by daylight saving time or regional settings. These UTC-based functions are the preferred choice for scenarios involving data integration, logging, auditing, or any logic that must behave identically regardless of where or when the query runs.

## Differences between the LocalNow and FixedLocalNow functions

Power Query M provides four functions for retrieving the current local time:

* `DateTime.LocalNow` returns the current local `datetime` each time the expression is evaluated.
* `DateTime.FixedLocalNow` returns the local `datetime` once per query evaluation, acting as a snapshot.
* `DateTimeZone.LocalNow` returns the current local `datetimezone` each time the expression is evaluated.
* `DateTimeZone.FixedLocal` now returns the local `datetimezone` once per query evaluation, acting as a snapshot

To demonstrate the difference, the following example generates a table with multiple rows. Each row captures a fresh `DateTime.LocalNow` value using a delay to ensure distinct timestamps, while each captured `DateTime.FixedLocalNow` value remains constant across all rows.

> [!NOTE]
>All the dates and times in the output of the examples in this article depend on when the functions are run. The dates and times shown in the output are for demonstration purposes only.

```powerquery-m
let
    // Create a table with LocalNow and FixedLocalNow columns 
    TableWithTimes = Table.FromList(
        {1..5},
        each {
            _,
            Function.InvokeAfter(() => DateTime.LocalNow(), #duration(0, 0, 0, 0.2)),
            Function.InvokeAfter(() => DateTime.FixedLocalNow(), #duration(0, 0, 0, 0.2))
        },
        {"Index", "LocalNow", "FixedLocalNow"}
    ),

    // Format both datetime columns
    FormatLocalNow = Table.TransformColumns(TableWithTimes, 
        {{"LocalNow", each DateTime.ToText(_, "yyyy-MM-ddThh:mm:ss.fff")}}),
    FormatFixedNow = Table.TransformColumns(FormatLocalNow, 
        {{"FixedLocalNow", each DateTime.ToText(_, "yyyy-MM-ddThh:mm:ss.fff")}}),

    // Change the table types
    FinalTable =  Table.TransformColumnTypes(FormatFixedNow, {{"Index", Int64.Type}, 
        {"LocalNow", type text}, {"FixedLocalNow", type text}})

in
    FinalTable
```

The output of this example is:

:::image type="content" source="media/localnow-vs-fixedlocalnow.png" alt-text="Screenshot of the table created by DateTime.LocalNow with dynamic dates and times and DateTime.FixedLocalNow with fixed dates and times.":::

If you look at the output, you might notice that even though the `DateTime.LocalNow` function appears first in the code, the value returned for `DateTime.FixedLocalNow` shows a time that occurs before the `DateTime.LocalTime` time. Even though `DateTime.LocalNow` is listed first in the table construction, the order of evaluation in Power Query M isn't guaranteed to follow the order of fields in a table. Instead, Power Query uses a lazy evaluation model. Using this model means that fields are only evaluated when needed and the engine determines the evaluation order, not the order in your code. In this case, the `DateTime.FixedLocalNow` function is evaluated first, so the first time returned for this function occurs before the first time returned for `DateTime.LocalNow`.

The following example shows how to produce similar results using `DateTimeZone.LocalNow` and `DateTimeZone.FixedLocalNow`.

```powerquery-m
let
    // Create a table with LocalNow and FixedLocalNow columns 
    TableWithTimes = Table.FromList(
        {1..5},
        each {
            _,
            Function.InvokeAfter(() => DateTimeZone.LocalNow(), #duration(0, 0, 0, 0.2)),
            Function.InvokeAfter(() => DateTimeZone.FixedLocalNow(), #duration(0, 0, 0, 0.2))
        },
        {"Index", "LocalNow", "FixedLocalNow"}
    ),

    // Format both datetimezone columns
    FormatLocalNow = Table.TransformColumns(TableWithTimes, 
        {{"LocalNow", each DateTimeZone.ToText(_, "yyyy-MM-ddThh:mm:ss.fff:zzz")}}),
    FormatFixedNow = Table.TransformColumns(FormatLocalNow, 
        {{"FixedLocalNow", each DateTimeZone.ToText(_, "yyyy-MM-ddThh:mm:ss.fff:zzz")}}),

    //  Change the table types
    FinalTable =  Table.TransformColumnTypes(FormatFixedNow, 
        {{"Index", Int64.Type}, {"LocalNow", type text}, {"FixedLocalNow", type text}})
in
    FinalTable
```

The output of this example in Power Query Desktop is:

:::image type="content" source="media/zone-localnow-vs-fixedlocalnow.png" alt-text="Screenshot of the table created by DateTimeZone.LocalNow with dynamic dates and times and DateTimeZone.FixedLocalNow with fixed dates and times.":::

> [!NOTE]
>If you run this example in Power Query Online, the time returned is always UTC time and the time zone portion of the returned values are always `+00:00`.

## Differences between the UtcNow and the FixedUtcNow functions

Power Query M provides two functions for retrieving the current UTC time:

* `DateTimeZone.UtcNow` returns the current UTC `datetimezone` each time the expression is evaluated.
* `DateTimeZone.FixedUtcNow` returns the local `datetimezone` once per query evaluation, acting as a snapshot.

The differences between these two functions are similar to the `LocalNow` and `FixedLocalNow` functions. However, whether the functions are run in Power Query Desktop or Power Query Online, the return values are always returned as UTC time. The following example demonstrates the differences between these two functions.

```powerquery-m
let
    // Create a table with UtcNow and FixedUtcNow columns 
    TableWithTimes = Table.FromList(
        {1..5},
        each {
            _,
            Function.InvokeAfter(() => DateTimeZone.UtcNow(), #duration(0, 0, 0, 0.2)),
            Function.InvokeAfter(() => DateTimeZone.FixedUtcNow(), #duration(0, 0, 0, 0.2))
        },
        {"Index", "UtcNow", "FixedUtcNow"}
    ),

    // Format both datetimezone columns
    FormatLocalNow = Table.TransformColumns(TableWithTimes, 
        {{"UtcNow", each DateTimeZone.ToText(_, "yyyy-MM-ddThh:mm:ss.fff:zzz")}}),
    FormatFixedNow = Table.TransformColumns(FormatLocalNow, 
        {{"FixedUtcNow", each DateTimeZone.ToText(_, "yyyy-MM-ddThh:mm:ss.fff:zzz")}}),

    //  Change the table types
    FinalTable =  Table.TransformColumnTypes(FormatFixedNow, 
        {{"Index", Int64.Type}, {"UtcNow", type text}, {"FixedUtcNow", type text}})
in
    FinalTable
```

The output of this example in both Power Query Desktop and Power Query Online is:

:::image type="content" source="media/zone-utcnow-vs-fixedutcnow.png" alt-text="Screenshot of the table created by DateTimeZone.UtcNow with dynamic dates and times and DateTimeZone.FixedUtcNow with fixed dates and times.":::

## Effects on other functions

Other Power Query M functions that depend on the current date and time can also be affected by how the local time is returned on either Power Query Desktop or Power Query Online. For example, if you use the [DateTimeZone.ToLocal](datetimezone-tolocal.md) function to convert UTC time to local time, it still returns the UTC time on Power Query Online.

Another example is any function that can use the current system time as a parameter. These functions include [Date.Month](date-month.md), [Date.DayOfYear](date-dayofyear.md), [DateTime.IsInCurrentYear](datetime-isincurrenthour.md ), [DateTimeZone.ZoneHours](datetimezone-zonehours.md), or any other function that can evaluate the current date and time.

In all of these functions, if your logic depends on whether a value falls within the current day, hour, month, or year, the results might differ between environments. These differences between environments are especially noticeable if the query runs near a boundary (for example, just before or after midnight, the start of a new month, or a new year). If consistency is crucial across different environments, use the `DateTimeZone.UtcNow` or `DateTimeZone.FixedUtcNow` functions to retrieve the date and time.

## Best practices and recommendations

Choosing the right time function in Power Query depends on your specific use case, the environment in which your query runs (desktop vs. online), and whether you need a dynamic or fixed timestamp. Here are some best practices to help guide your decision:

* **Be explicit about time zones**: Use the DateTimeZone functions instead of DateTime functions when time zone context matters. Use `DateTimeZone.UtcNow` or `DateTimeZone.FixedUtcNow` for consistency across environments, especially in cloud-based solutions like Power BI service.
* **Use fixed functions for repeatable results**: Use the fixed variants (such as `DateTimeZone.FixedUtcNow`) when you want the timestamp to remain constant across query evaluations. This method is especially useful for logging, auditing, or capturing the time of data ingestion.
* **Avoid local functions in Power Query Online**: Functions like `DateTime.LocalNow` and `DateTimeZone.LocalNow` return UTC time in cloud-based solutions like Power BI service, which can lead to confusion or incorrect assumptions. If you need actual local time in the service, consider adjusting UTC manually using known offsets (although this adjustment can be brittle, for example, due to daylight savings time or regional settings).
* **Test in both desktop and online environments**: Always test your queries in both Power Query Desktop and Power Query Online if your logic depends on current time. This testing helps catch discrepancies early, especially for scheduled refresh scenarios.
* **Document your time logic**: Clearly comment or document why a specific time function is used, especially if you're using a workaround for time zone handling. This information helps future collaborators understand the intent behind the logic.
* **Use UTC for scheduled workflows**: For scheduled refreshes or automated pipelines, UTC is the safest and most predictable choice. It avoids ambiguity caused by daylight saving time or regional time zone shifts.
* **Cache time values when needed**: If you need to use the same timestamp across multiple steps in a query, assign it to a variable at the top of your query using a fixed function. This variable ensures consistency throughout the transformation logic.
