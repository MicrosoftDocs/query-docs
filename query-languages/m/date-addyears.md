---
title: "Date.AddYears | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Date.AddYears

## Syntax

<pre>
Date.AddYears(<b>dateTime</b> as any, <b>numberOfYears</b> as number) as any
</pre> 
  
## About  
Returns the `date`, `datetime`, or `datetimezone` result of adding `numberOfYears` to a `datetime` value `dateTime`. <ul> <li><code>dateTime</code>: The <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to which years are added.</li> <li><code>numberOfYears</code>: The number of years to add.</li> </ul>

## Example 1
Add 4 years to the `date`, `datetime`, or `datetimezone` value representing the date 5/14/2011.

```powerquery-m
Date.AddYears(#date(2011, 5, 14), 4)
```

`#date(2015, 5, 14)`

## Example 2
Add 10 years to the `date`, `datetime`, or `datetimezone` value representing the date and time of 5/14/2011 08:15:22 AM.

```powerquery-m
Date.AddYears(#datetime(2011, 5, 14, 8, 15, 22), 10)
```

`#datetime(2021, 5, 14, 8, 15, 22)`
