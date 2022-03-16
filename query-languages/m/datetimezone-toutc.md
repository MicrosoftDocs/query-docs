---
description: "Learn more about: DateTimeZone.ToUtc"
title: "DateTimeZone.ToUtc | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# DateTimeZone.ToUtc

## Syntax

<pre>
DateTimeZone.ToUtc(<b>dateTimeZone</b> as nullable datetimezone) as nullable datetimezone
</pre>
  
## About

Changes timezone information of the datetime value `dateTimeZone` to the UTC or Universal Time timezone information. If `dateTimeZone` does not have a timezone component, the UTC timezone information is added.

## Example 1

Change timezone information for #datetimezone(2010, 12, 31, 11, 56, 02, 7, 30) to UTC timezone.

**Usage**

```powerquery-m
DateTimeZone.ToUtc(#datetimezone(2010, 12, 31, 11, 56, 02, 7, 30))
```

**Output**

`#datetimezone(2010, 12, 31, 4, 26, 2, 0, 0)`
