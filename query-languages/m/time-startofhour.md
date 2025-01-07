---
description: "Learn more about: Time.StartOfHour"
title: "Time.StartOfHour"
ms.subservice: m-source
---
# Time.StartOfHour

## Syntax

<pre>
Time.StartOfHour(<b>dateTime</b> as any) as any
</pre>
  
## About

Returns the start of the hour represented by `dateTime`. `dateTime` must be a `time`, `datetime` or `datetimezone` value.

## Example 1

Find the start of the hour for October 10th, 2011, 8:10:32AM.

**Usage**

```powerquery-m
Time.StartOfHour(#datetime(2011, 10, 10, 8, 10, 32))
```

**Output**

`#datetime(2011, 10, 10, 8, 0, 0)`
