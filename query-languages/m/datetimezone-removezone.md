---
title: "DateTimeZone.RemoveZone | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
DateTimeZone.RemoveZone( #datetimezone(2011, 12, 31, 9, 15, 36,-7, 0))
```

`#datetime(2011, 12, 31, 9, 15, 36)`

