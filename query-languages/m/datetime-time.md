---
description: "Learn more about: DateTime.Time"
title: "DateTime.Time | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# DateTime.Time

## Syntax

<pre>
DateTime.Time(<b>dateTime</b> as any) as nullable time
</pre>
  
## About

Returns the time part of the given datetime value, `dateTime`.

## Example 1

Find the time value of #datetime(2010, 12, 31, 11, 56, 02).

**Usage**

```powerquery-m
DateTime.Time(#datetime(2010, 12, 31, 11, 56, 02))
```

**Output**

`#time(11, 56, 2)`
