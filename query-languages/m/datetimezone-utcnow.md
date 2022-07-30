---
description: "Learn more about: DateTimeZone.UtcNow"
title: "DateTimeZone.UtcNow"
ms.date: 3/11/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# DateTimeZone.UtcNow

## Syntax

<pre>
DateTimeZone.UtcNow() as datetimezone
</pre>
  
## About

Returns the current date and time in UTC (the GMT timezone).

## Example 1

Get the current date & time in UTC.

**Usage**

```powerquery-m
DateTimeZone.UtcNow()
```

**Output**

`#datetimezone(2011, 8, 16, 23, 34, 37.745, 0, 0)`
