---
title: "Date.AddMonths | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Date.AddMonths

## Syntax

<pre>
Date.AddMonths(<b>dateTime</b> as any, <b>numberOfMonths</b> as number) as any
</pre> 
  
## About  
Returns the `date`, `datetime`, or `datetimezone` result from adding `numberOfMonths` months to the `datetime` value `dateTime`. <ul> <li><code>dateTime</code>: The <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to which months are being added.</li> <li><code>numberOfMonths</code>: The number of months to add.</li> </ul>

## Example 1
Add 5 months to the `date`, `datetime`, or `datetimezone` value representing the date 5/14/2011.

```powerquery-m
Date.AddMonths(#date(2011, 5, 14), 5)
```

`#date(2011, 10, 14)`

## Example 2
Add 18 months to the `date`, `datetime`, or `datetimezone` value representing the date and time of 5/14/2011 08:15:22 AM.

```powerquery-m
Date.AddMonths(#datetime(2011, 5, 14, 8, 15, 22), 18)
```

`#datetime(2012, 11, 14, 8, 15, 22)`
