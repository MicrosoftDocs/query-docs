---
description: "Learn more about: List.Times"
title: "List.Times | Microsoft Docs"
ms.date: 3/9/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.Times

## Syntax

<pre>
List.Times(<b>start</b> as time, <b>count</b> as number, <b>step</b> as duration) as list
</pre>

## About

Returns a list of `time` values of size `count`, starting at `start`. The given increment, `step`, is a `duration` value that is added to every value.

## Example 1

Create a list of 4 values starting from noon (#time(12, 0, 0)) incrementing by one hour (#duration(0, 1, 0, 0)).

**Usage**

```powerquery-m
List.Times(#time(12, 0, 0), 4, #duration(0, 1, 0, 0))
```

**Output**

```powerquery-m
{
    #time(12, 0, 0),
    #time(13, 0, 0),
    #time(14, 0, 0),
    #time(15, 0, 0)
}
```
