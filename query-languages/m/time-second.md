---
title: "Time.Second | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Time.Second

## Syntax

<pre>
Time.Second(<b>dateTime</b> as any) as nullable number`
</pre>

## About
Returns the second component of the provided `time`, `datetime`, or `datetimezone` value, `dateTime`.

## Example 1
Find the second value from a datetime value.

```powerquery-m
Time.Second(#datetime(2011, 12, 31, 9, 15, 36.5))
```

`36.5`
