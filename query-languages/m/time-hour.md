---
description: "Learn more about: Time.Hour"
title: "Time.Hour | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
Time.Hour(#datetime(2011, 12, 31, 9, 15, 36))
```

**Output**

`9`
