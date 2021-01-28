---
description: "Learn more about: List.Durations"
title: "List.Durations | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.Durations

## Syntax

<pre>
List.Durations(<b>start</b> as duration, <b>count</b> as number, <b>step</b> as duration) as list
</pre>

## About
Returns a list of `count` `duration` values, starting at `start` and incremented by the given `duration` `step`.

## Example
Create a list of 5 values starting 1 hour and incrementing by an hour.

```powerquery-m
List.Durations(#duration(0, 1, 0, 0), 5, #duration(0, 1, 0, 0))
```

<table> <tr><td>01:00:00</td></tr> <tr><td>02:00:00</td></tr> <tr><td>03:00:00</td></tr> <tr><td>04:00:00</td></tr> <tr><td>05:00:00</td></tr> </table>
