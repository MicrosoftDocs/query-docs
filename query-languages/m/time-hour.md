---
title: "Time.Hour | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Time.Hour

## Syntax

<pre>
Time.Hour(<b>dateTime</b> as any) as nullable number
</pre>
  
## About  
Returns the hour component of the provided `time`, `datetime`, or `datetimezone` value, `dateTime`.

## Example 1
Find the hour in #datetime(2011, 12, 31, 9, 15, 36).

```powerquery-m
Time.Hour(#datetime(2011, 12, 31, 9, 15, 36))
```

`9`
