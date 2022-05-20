---
description: "Learn more about: Date.AddYears"
title: "Date.AddYears | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Date.AddYears

## Syntax

<pre>
Date.AddYears(<b>dateTime</b> as any, <b>numberOfYears</b> as number) as any
</pre>
  
## About

Returns the `date`, `datetime`, or `datetimezone` result of adding `numberOfYears` to a `datetime` value `dateTime`.

* `dateTime`: The `date`, `datetime`, or `datetimezone` value to which years are added.
* `numberOfYears`: The number of years to add.

## Example 1

Add 4 years to the `date`, `datetime`, or `datetimezone` value representing the date 5/14/2011.

**Usage**

```powerquery-m
Date.AddYears(#date(2011, 5, 14), 4)
```

**Output**

`#date(2015, 5, 14)`

## Example 2

Add 10 years to the `date`, `datetime`, or `datetimezone` value representing the date and time of 5/14/2011 08:15:22 AM.

**Usage**

```powerquery-m
Date.AddYears(#datetime(2011, 5, 14, 8, 15, 22), 10)
```

**Output**

`#datetime(2021, 5, 14, 8, 15, 22)`
