---
description: "Learn more about: Date.IsInCurrentDay"
title: "Date.IsInCurrentDay"
ms.date: 3/11/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Date.IsInCurrentDay

## Syntax

<pre>
Date.IsInCurrentDay(<b>dateTime</b> as any) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the current day, as determined by the current date and time on the system.

- `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example

Determine if the current system time is in the current day.

**Usage**

```powerquery-m
Date.IsInCurrentDay(DateTime.FixedLocalNow())
```

**Output**

`true`
