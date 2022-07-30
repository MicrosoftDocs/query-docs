---
description: "Learn more about: List.DateTimeZones"
title: "List.DateTimeZones"
ms.date: 3/8/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.DateTimeZones

## Syntax

<pre>
List.DateTimeZones(<b>start</b> as datetimezone, <b>count</b> as number, <b>step</b> as duration) as list 
</pre>
  
## About

Returns a list of `datetimezone` values of size `count`, starting at `start`. The given increment, `step`, is a `duration` value that is added to every value.

## Example 1

Create a list of 10 values starting from 5 minutes before New Year's Day (#datetimezone(2011, 12, 31, 23, 55, 0, -8, 0)) incrementing by 1 minute (#duration(0, 0, 1, 0)).

**Usage**

```powerquery-m
List.DateTimeZones(#datetimezone(2011, 12, 31, 23, 55, 0, -8, 0), 10, #duration(0, 0, 1, 0))
```

**Output**

```powerquery-m
{
    #datetimezone(2011, 12, 31, 23, 55, 0, -8, 0),
    #datetimezone(2011, 12, 31, 23, 56, 0, -8, 0),
    #datetimezone(2011, 12, 31, 23, 57, 0, -8, 0),
    #datetimezone(2011, 12, 31, 23, 58, 0, -8, 0),
    #datetimezone(2011, 12, 31, 23, 59, 0, -8, 0),
    #datetimezone(2012, 1, 1, 0, 0, 0, -8, 0),
    #datetimezone(2012, 1, 1, 0, 1, 0, -8, 0),
    #datetimezone(2012, 1, 1, 0, 2, 0, -8, 0),
    #datetimezone(2012, 1, 1, 0, 3, 0, -8, 0),
    #datetimezone(2012, 1, 1, 0, 4, 0, -8, 0)
}
```
