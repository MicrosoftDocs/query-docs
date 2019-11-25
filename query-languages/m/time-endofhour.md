---
title: "Time.EndOfHour | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Time.EndOfHour

## Syntax

<pre>
Time.EndOfHour(<b>dateTime</b> as any) as any
</pre>
  
## About  
Returns a `time`, `datetime`, or `datetimezone` value representing the end of the hour in `dateTime`, including fractional seconds. Time zone information is preserved. <ul> <li><code>dateTime</code>: A <code>time</code>, <code>datetime</code>, or <code>datetimezone</code> value from which the end of the hour is calculated.</li> </ul>

## Example 1
Get the end of the hour for 5/14/2011 05:00:00 PM.

```powerquery-m
Time.EndOfHour(#datetime(2011, 5, 14, 17, 0, 0))
```

`#datetime(2011, 5, 14, 17, 59, 59.9999999)`

## Example 2
Get the end of the hour for 5/17/2011 05:00:00 PM -7:00.

```powerquery-m
Time.EndOfHour(#datetimezone(2011, 5, 17, 5, 0, 0, -7, 0))
```

`#datetimezone(2011, 5, 17, 5, 59, 59.9999999, -7, 0)`
