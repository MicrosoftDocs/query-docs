---
description: "Learn more about: Duration.FromText"
title: "Duration.FromText"
ms.subservice: m-source
---
# Duration.FromText

## Syntax

<pre>
Duration.FromText(<b>text</b> as nullable text) as nullable duration
</pre>
  
## About

Returns a duration value from the specified text, `text`. The following formats can be parsed by this function:

* (-)hh:mm(:ss(.ff))
* (-)ddd(.hh:mm(:ss(.ff)))

(All ranges are inclusive)

* ddd: Number of days.
* hh: Number of hours, between 0 and 23.
* mm: Number of minutes, between 0 and 59.
* ss: Number of seconds, between 0 and 59.
* ff: Fraction of seconds, between 0 and 9999999.

## Example 1

Convert `"2.05:55:20"` into a `duration` value.

**Usage**

```powerquery-m
Duration.FromText("2.05:55:20")
```

**Output**

`#duration(2, 5, 55, 20)`
