---
title: "Duration.FromText | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Duration.FromText

## Syntax

<pre>
Duration.FromText(<b>text</b> as nullable text) as nullable duration
</pre>
  
## About  
Returns a duration value from the specified text, `text`. The following formats can be parsed by this function: <ul> <li>(-)hh:mm(:ss(.ff)) </li> <li>(-)ddd(.hh:mm(:ss(.ff))) </li> </ul> <br> (All ranges are inclusive)<br> ddd: Number of days.<br> hh: Number of hours, between 0 and 23.<br> mm: Number of minutes, between 0 and 59.<br> ss: Number of seconds, between 0 and 59.<br> ff: Fraction of seconds, between 0 and 9999999.

## Example 1
Convert `"2.05:55:20"` into a `duration` value.

```powerquery-m
Duration.FromText("2.05:55:20")
```

`#duration(2, 5, 55, 20)`

