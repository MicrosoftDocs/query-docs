---
description: "Learn more about: DateTimeZone.ToLocal"
title: "DateTimeZone.ToLocal"
ms.date: 3/11/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
DateTimeZone.ToLocal(#datetimezone(2010, 12, 31, 11, 56, 02, 7, 30))
```

**Output**

`#datetimezone(2010, 12, 31, 12, 26, 2, -8, 0)`

