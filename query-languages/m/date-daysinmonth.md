---
title: "Date.DaysInMonth | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Date.DaysInMonth

## Syntax

<pre>
Date.DaysInMonth(<b>dateTime</b> as any) as nullable number 
</pre> 
  
## About  
Returns the number of days in the month in the `date`, `datetime`, or `datetimezone` value `dateTime`. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value for which the number of days in the month is returned.</li> </ul>

## Example 1
Number of days in the month December as represented by `#date(2011, 12, 01)`.

```powerquery-m
Date.DaysInMonth(#date(2011, 12, 01))
```

`31`