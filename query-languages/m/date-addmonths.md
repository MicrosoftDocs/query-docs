---
description: "Learn more about: Date.AddMonths"
title: "Date.AddMonths"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Date.AddMonths

## Syntax

<pre>
Date.AddMonths(<b>dateTime</b> as any, <b>numberOfMonths</b> as number) as any
</pre>
  
## About

Returns the `date`, `datetime`, or `datetimezone` result from adding `numberOfMonths` months to the `datetime` value `dateTime`.

* `dateTime`: The `date`, `datetime`, or `datetimezone` value to which months are being added.
* `numberOfMonths`: The number of months to add.

## Example 1

Add 5 months to the `date`, `datetime`, or `datetimezone` value representing the date 5/14/2011.

**Usage**

```powerquery-m
Date.AddMonths(#date(2011, 5, 14), 5)
```

**Output**

`#date(2011, 10, 14)`

## Example 2

Add 18 months to the `date`, `datetime`, or `datetimezone` value representing the date and time of 5/14/2011 08:15:22 AM.

**Usage**

```powerquery-m
Date.AddMonths(#datetime(2011, 5, 14, 8, 15, 22), 18)
```

**Output**

`#datetime(2012, 11, 14, 8, 15, 22)`
