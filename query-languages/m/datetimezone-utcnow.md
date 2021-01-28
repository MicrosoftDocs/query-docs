---
description: "Learn more about: DateTimeZone.UtcNow"
title: "DateTimeZone.UtcNow | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

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

```powerquery-m
DateTimeZone.UtcNow()
```

`#datetimezone(2011, 8, 16, 23, 34, 37.745, 0, 0)`
