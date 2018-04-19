---
title: "List.Times | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Times
<code>List.Times(**start** as time, **count** as number, **step** as duration) as list</code>

## About
Returns a list of <code>time</code> values of size <code>count</code>, starting at <code>start</code>. The given increment, <code>step</code>, is a <code>duration</code> value that is added to every value.

## Example 1
Create a list of 4 values starting from noon (#time(12, 0, 0)) incrementing by one hour (#duration(0, 1, 0, 0)).


```
List.Times(#time(12, 0, 0), 4, #duration(0, 1, 0, 0))
```

<table> <tr><td>12:00:00</td></tr> <tr><td>13:00:00</td></tr> <tr><td>14:00:00</td></tr> <tr><td>15:00:00</td></tr> </table>


  
