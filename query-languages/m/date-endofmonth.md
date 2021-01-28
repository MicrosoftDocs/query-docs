---
description: "Learn more about: Date.EndOfMonth"
title: "Date.EndOfMonth | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.EndOfMonth

## Syntax

<pre>
Date.EndOfMonth(<b>dateTime</b> as any) as any 
</pre>
  
## About  
Returns the last day of the month in `dateTime`. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value from which the end of the month is calculated</li> </ul>

## Example 1
Get the end of the month for 5/14/2011.

```powerquery-m
Date.EndOfMonth(#date(2011, 5, 14))
```

`#date(2011, 5, 31)`

## Example 2
Get the end of the month for 5/17/2011 05:00:00 PM -7:00.

```powerquery-m
Date.EndOfMonth(#datetimezone(2011, 5, 17, 5, 0, 0, -7, 0))
```

`#datetimezone(2011, 5, 31, 23, 59, 59.9999999, -7, 0)`
