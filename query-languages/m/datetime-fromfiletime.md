---
description: "Learn more about: DateTime.FromFileTime"
title: "DateTime.FromFileTime | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# DateTime.FromFileTime

## Syntax

<pre>
DateTime.FromFileTime(<b>fileTime</b> as nullable number) as nullable datetime
</pre>
  
## About

Creates a `datetime` value from the `fileTime` value and converts it to the local time zone. The filetime is a Windows file time value that represents the number of 100-nanosecond intervals that have elapsed since 12:00 midnight, January 1, 1601 A.D. (C.E.) Coordinated Universal Time (UTC).

## Example 1

Convert `129876402529842245` into a datetime value.

**Usage**

```powerquery-m
DateTime.FromFileTime(129876402529842245)
```

**Output**

`#datetime(2012, 7, 24, 14, 50, 52.9842245)`
