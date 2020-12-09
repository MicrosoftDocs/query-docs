---
title: "DateTimeZone.RemoveZone | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# DateTimeZone.RemoveZone

## Syntax

<pre>
DateTimeZone.RemoveZone(<b>dateTimeZone</b> as nullable datetimezone) as nullable datetime
</pre>
  
## About  
Returns a #datetime value from `dateTimeZone` with timezone information removed.

## Example 1
Remove timezone information from the value #datetimezone(2011, 12, 31, 9, 15, 36, -7, 0).

```powerquery-m
DateTimeZone.RemoveZone(#datetimezone(2011, 12, 31, 9, 15, 36, -7, 0))
```

`#datetime(2011, 12, 31, 9, 15, 36)`

