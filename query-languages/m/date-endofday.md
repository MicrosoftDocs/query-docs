---
title: "Date.EndOfDay | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.EndOfDay

<pre>
Date.EndOfDay(<b>dateTime</b> as any) as any
</pre>
  
## About  
Returns a `date`, `datetime`, or `datetimezone` value representing the end of the day in `dateTime`. Time zone information is preserved. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value from from which the end of the day is calculated.</li> </ul>

## Example 1
Get the end of the day for 5/14/2011 05:00:00 PM.

```powerquery-m
Date.EndOfDay(#datetime(2011, 5, 14, 17, 0, 0))
```

```powerquery-m
#datetime(2011, 5, 14, 23, 59, 59.9999999)
```

## Example 2
Get the end of the day for 5/17/2011 05:00:00 PM -7:00.

```powerquery-m
Date.EndOfDay(#datetimezone(2011, 5, 17, 5, 0, 0, -7, 0))
```

```powerquery-m
#datetimezone(2011, 5, 17, 23, 59, 59.9999999, -7, 0)
```
