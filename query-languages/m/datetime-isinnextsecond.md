---
description: "Learn more about: DateTime.IsInNextSecond"
title: "DateTime.IsInNextSecond"
ms.date: 3/11/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# DateTime.IsInNextSecond

## Syntax

<pre>
DateTime.IsInNextSecond(<b>dateTime</b> as any) as nullable logical
</pre>
  
## About

Indicates whether the given datetime value `dateTime` occurs during the next second, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current second.

* `dateTime`: A `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the second after the current system time is in the next second.

**Usage**

```powerquery-m
DateTime.IsInNextSecond(DateTime.FixedLocalNow() + #duration(0, 0, 0, 1))
```

**Output**

`true`
