---
title: "DateTime.IsInCurrentSecond | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInCurrentSecond

## Syntax

<pre>
DateTime.IsInCurrentSecond(<b>dateTime</b> as any) as nullable logical
</pre>
  
## About  
Indicates whether the given datetime value `dateTime` occurs during the current second, as determined by the current date and time on the system. <ul> <li><code>dateTime</code>: A <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>

## Example 1
Determine if the current system time is in the current second.

```powerquery-m
DateTime.IsInCurrentSecond(DateTime.FixedLocalNow())
```

`true`
