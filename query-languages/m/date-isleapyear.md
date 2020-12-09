---
title: "Date.IsLeapYear | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.IsLeapYear

## Syntax

<pre>  
Date.IsLeapYear(<b>dateTime</b> as any) as nullable logical 
</pre>
  
## About  
Indicates whether the given datetime value `dateTime` falls in is a leap year. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>

## Example 1
Determine if the year 2012, as represented by `#date(2012, 01, 01)` is a leap year.

```powerquery-m
Date.IsLeapYear(#date(2012, 01, 01))
```

`true`
