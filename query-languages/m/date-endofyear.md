---
description: "Learn more about: Date.EndOfYear"
title: "Date.EndOfYear | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.EndOfYear

## Syntax

<pre>
Date.EndOfYear(<b>dateTime</b> as any) as any
</pre>
  
## About  
Returns a value representing the end of the year in `dateTime`, including fractional seconds. Time zone information is preserved. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value from which the end of the year is calculated.</li> </ul>

## Example 1
Get the end of the year for 5/14/2011 05:00:00 PM.

```powerquery-m
Date.EndOfYear(#datetime(2011, 5, 14, 17, 0, 0))
```

`#datetime(2011, 12, 31, 23, 59, 59.9999999)`

## Example 2
Get the end of hour for 5/17/2011 05:00:00 PM -7:00.

```powerquery-m
Date.EndOfYear(#datetimezone(2011, 5, 17, 5, 0, 0, -7, 0))
```

`#datetimezone(2011, 12, 31, 23, 59, 59.9999999, -7, 0)`
