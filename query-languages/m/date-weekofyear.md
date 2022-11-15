---
description: "Learn more about: Date.WeekOfYear"
title: "Date.WeekOfYear"
ms.date: 11/14/2022
---
# Date.WeekOfYear

## Syntax

<pre>
Date.WeekOfYear(<b>dateTime</b> as any, optional <b>firstDayOfWeek</b> as nullable number) as nullable number
</pre>

## About

Returns a number from 1 to 54 indicating which week of the year the date, `dateTime`, falls in.

- `dateTime`: A `datetime` value for which the week-of-the-year is determined.

- `firstDayOfWeek`: An optional [Day.Type](day-type.md) value that indicates which day is considered the start of a new week (for example, `Day.Sunday`). If unspecified, a culture-dependent default is used.

## Example 1

Determine which week of the year contains March 27th, 2011.

**Usage**

```powerquery-m
Date.WeekOfYear(#date(2011, 03, 27))
```

**Output**

`14`

## Example 2

Determine which week of the year contains March 27th, 2011, using Monday as the start of the week.

**Usage**

```powerquery-m
Date.WeekOfYear(#date(2011, 03, 27), Day.Monday)
```

**Output**

`13`
