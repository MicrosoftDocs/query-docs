---
title: "Time.StartOfHour | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Time.StartOfHour

## Syntax

<pre>
Time.StartOfHour(<b>dateTime</b> as any) as any 
</pre>
  
## About  
Returns the first value of the hour given a `time`, `datetime` or `datetimezone` type.

## Example 1
Find the start of the hour for October 10th, 2011, 8:10:32AM (`#datetime(2011, 10, 10, 8, 10, 32)`).

```powerquery-m
Time.StartOfHour(#datetime(2011, 10, 10, 8, 10, 32))
```

`#datetime(2011, 10, 10, 8, 0, 0)`
