---
title: "List.Times | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

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


```powerquery-m
List.Times(#time(12, 0, 0), 4, #duration(0, 1, 0, 0))
```

<table> <tr><td>12:00:00</td></tr> <tr><td>13:00:00</td></tr> <tr><td>14:00:00</td></tr> <tr><td>15:00:00</td></tr> </table>


  
