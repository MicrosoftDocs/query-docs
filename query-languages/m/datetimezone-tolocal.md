---
description: "Learn more about: DateTimeZone.ToLocal"
title: "DateTimeZone.ToLocal | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# DateTimeZone.ToLocal

## Syntax

<pre>
DateTimeZone.ToLocal(<b>dateTimeZone</b> as nullable datetimezone) as nullable datetimezone
</pre>
  
## About  
Changes timezone information of the datetimezone value `dateTimeZone` to the local timezone information. If `dateTimeZone` does not have a timezone component, the local timezone information is added.

## Example 1
Change timezone information for #datetimezone(2010, 12, 31, 11, 56, 02, 7, 30) to local timezone (assuming PST).

```powerquery-m
DateTimeZone.ToLocal(#datetimezone(2010, 12, 31, 11, 56, 02, 7, 30))
```

`#datetimezone(2010, 12, 31, 12, 26, 2, -8, 0)`

