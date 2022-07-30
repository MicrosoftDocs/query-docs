---
description: "Learn more about: Time.StartOfHour"
title: "Time.StartOfHour"
ms.date: 3/14/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Time.StartOfHour

## Syntax

<pre>
Time.StartOfHour(<b>dateTime</b> as any) as any
</pre>
  
## About

Returns the first value of the hour given a `time`, `datetime` or `datetimezone` type.

## Example 1

Find the start of the hour for October 10th, 2011, 8:10:32AM (`#datetime(2011, 10, 10, 8, 10, 32)`).

**Usage**

```powerquery-m
Time.StartOfHour(#datetime(2011, 10, 10, 8, 10, 32))
```

**Output**

`#datetime(2011, 10, 10, 8, 0, 0)`
