---
title: "Date.AddWeeks | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Date.AddWeeks

## Syntax

<pre>
Date.AddWeeks(<b>dateTime</b> as any, <b>numberOfWeeks</b> as number) as any
</pre>
  
## About  
Returns the `date`, `datetime`, or `datetimezone` result from adding `numberOfWeeks` weeks to the `datetime` value `dateTime`. <ul> <li><code>dateTime</code>: The <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to which weeks are being added.</li> <li><code>numberOfWeeks</code>: The number of weeks to add.</li> </ul>

## Example 1
Add 2 weeks to the `date`, `datetime`, or `datetimezone` value representing the date 5/14/2011.

```powerquery-m
Date.AddWeeks(#date(2011, 5, 14), 2)
```

`#date(2011, 5, 28)`
