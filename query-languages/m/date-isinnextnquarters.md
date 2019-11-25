---
title: "Date.IsInNextNQuarters | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Date.IsInNextNQuarters

## Syntax

<pre>
Date.IsInNextNQuarters(<b>dateTime</b> as any, <b>quarters</b> as number) as nullable logical
</pre>

## About
Indicates whether the given datetime value `dateTime` occurs during the next number of quarters, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current quarter. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> <li><code>quarters</code>: The number of quarters.</li> </ul>

## Example 1
Determine if the quarter after the current system time is in the next two quarters.

```powerquery-m
Date.IsInNextNQuarters(Date.AddQuarters(DateTime.FixedLocalNow(), 1), 2)
```

`true`
