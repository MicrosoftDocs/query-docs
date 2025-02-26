---
description: "Learn more about: Date.EndOfWeek"
title: "Date.EndOfWeek"
ms.subservice: m-source
---
# Date.EndOfWeek

## Syntax

<pre>
Date.EndOfWeek(<b>dateTime</b> as any, optional <b>firstDayOfWeek</b> as nullable number) as any  
</pre>
  
## About

Returns the end of the week that contains `dateTime`. This function takes an optional `Day`, `firstDayOfWeek`, to set as the first day of the week for this relative calculation. The default value is [Day.Sunday](/powerquery-m/day-type).

* `dateTime`: A `date`, `datetime`, or `datetimezone` value from which the last day of the week is calculated
* `firstDayOfWeek`: _[Optional]_ A [Day.Type](/powerquery-m/day-type) value representing the first day of the week. Possible values are `Day.Sunday`, `Day.Monday`, `Day.Tuesday`, `Day.Wednesday`, `Day.Thursday`, `Day.Friday` and `Day.Saturday`. The default value is `Day.Sunday`.

## Example 1

Get the end of the week for 5/14/2011.

**Usage**

```powerquery-m
Date.EndOfWeek(#date(2011, 5, 14))
```

**Output**

`#date(2011, 5, 14)`

## Example 2

Get the end of the week for 5/17/2011 05:00:00 PM -7:00, with Sunday as the first day of the week.

**Usage**

```powerquery-m
Date.EndOfWeek(#datetimezone(2011, 5, 17, 5, 0, 0, -7, 0), Day.Sunday)
```

**Output**

`#datetimezone(2011, 5, 21, 23, 59, 59.9999999, -7, 0)`
