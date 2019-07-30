---
title: "DateTimeZone.FromFileTime | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTimeZone.FromFileTime

## Syntax

<pre>
DateTimeZone.FromFileTime(<b>fileTime</b> as nullable number) as nullable datetimezone  
</pre>
  
## About  
Creates a `datetimezone` value from the `fileTime` value and converts it to the local time zone. The filetime is a Windows file time value that represents the number of 100-nanosecond intervals that have elapsed since 12:00 midnight, January 1, 1601 A.D. (C.E.) Coordinated Universal Time (UTC). 

## Example 1
Convert `129876402529842245` into a datetimezone value.

```powerquery-m
DateTimeZone.FromFileTime(129876402529842245)
```

`#datetimezone(2012, 7, 24, 14, 50, 52.9842245, -7, 0)`
