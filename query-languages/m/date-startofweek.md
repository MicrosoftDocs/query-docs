---
description: "Learn more about: Date.StartOfWeek"
title: "Date.StartOfWeek"
ms.subservice: m-source
---
# Date.StartOfWeek

## Syntax

<pre>
Date.StartOfWeek(<b>dateTime</b> as any, optional <b>firstDayOfWeek</b> as nullable number) as any
</pre>
  
## About

Returns the start of the week that contains `dateTime`. `dateTime` must be a `date`, `datetime`, or `datetimezone` value.

## Example 1

Find the start of the week for Tuesday, October 11th, 2011.

**Usage**

```powerquery-m
Date.StartOfWeek(#datetime(2011, 10, 11, 8, 10, 32))
```

**Output**

```powerquery-m
// Sunday, October 9th, 2011
#datetime(2011, 10, 9, 0, 0, 0)
```

## Example 2

Find the start of the week for Tuesday, October 11th, 2011, using Monday as the start of the week.

**Usage**

```powerquery-m
Date.StartOfWeek(#datetime(2011, 10, 11, 8, 10, 32), Day.Monday)
```

**Output**

```powerquery-m
// Monday, October 10th, 2011
#datetime(2011, 10, 10, 0, 0, 0)
```
