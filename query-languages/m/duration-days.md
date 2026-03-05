---
description: "Learn more about: Duration.Days"
title: "Duration.Days"
ms.subservice: m-source
ms.topic: reference
---
# Duration.Days

## Syntax

<pre>
Duration.Days(<b>duration</b> as nullable duration) as nullable number
</pre>

## About

Returns the days portion of `duration`.

## Example 1

Extract the number of days between two dates.

**Usage**

```powerquery-m
Duration.Days(#date(2022, 3, 4) - #date(2022, 2, 25))
```

**Output**

`7`
