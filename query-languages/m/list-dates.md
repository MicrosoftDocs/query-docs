---
title: "List.Dates | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

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

```powerquery-m
List.Dates(#date(2011, 12, 31), 5, #duration(1, 0, 0, 0))
```

<table> <tr><td>12/31/2011 12:00:00 AM</td></tr> <tr><td>1/1/2012 12:00:00 AM</td></tr> <tr><td>1/2/2012 12:00:00 AM</td></tr> <tr><td>1/3/2012 12:00:00 AM</td></tr> <tr><td>1/4/2012 12:00:00 AM</td></tr> </table>

