---
title: "List.Average | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Average

## Syntax

<pre>
List.Average(<b>list</b> as list, optional <b>precision</b> as nullable number) as any 
</pre>
  
## About  
Returns the average value for the items in the list, `list`. The result is given in the same datatype as the values in the list. Only works with number, date, time, datetime, datetimezone and duration values. If the list is empty null is returned.

## Example 1
Find the average of the list of numbers, `{3, 4, 6}`.

```powerquery-m
List.Average({3, 4, 6})
```

`4.333333333333333`

## Example 2
Find the average of the date values January 1, 2011, January 2, 2011 and January 3, 2011.

```powerquery-m
List.Average({#date(2011, 1, 1), #date(2011, 1, 2), #date(2011, 1, 3)})
```

`#date(2011, 1, 2)`
