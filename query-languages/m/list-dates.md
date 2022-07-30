---
description: "Learn more about: List.Dates"
title: "List.Dates | Microsoft Docs"
ms.date: 3/8/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.Dates

## Syntax

<pre>
List.Dates(<b>start</b> as date, <b>count</b> as number, <b>step</b> as duration) as list
</pre>

## About

Returns a list of `date` values of size `count`, starting at `start`. The given increment, `step`, is a `duration` value that is added to every value.

## Example 1

Create a list of 5 values starting from New Year's Eve (#date(2011, 12, 31)) incrementing by 1 day(#duration(1, 0, 0, 0)).

**Usage**

```powerquery-m
List.Dates(#date(2011, 12, 31), 5, #duration(1, 0, 0, 0))
```

**Output**

```powerquery-m
{
    #date(2011, 12, 31),
    #date(2012, 1, 1),
    #date(2012, 1, 2),
    #date(2012, 1, 3),
    #date(2012, 1, 4)
}
```
