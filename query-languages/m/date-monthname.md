---
description: "Learn more about: Date.MonthName"
title: "Date.MonthName"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Date.MonthName

## Syntax

<pre>
Date.MonthName(<b>date</b> as any, optional <b>culture</b> as nullable text) as nullable text
</pre>

## About

Returns the name of the month component for the provided `date`. An optional `culture` may also be provided (for example, "en-US").

## Example 1

Get the month name.

**Usage**

```powerquery-m
Date.MonthName(#datetime(2011, 12, 31, 5, 0, 0), "en-US")
```

**Output**

`"December"`
