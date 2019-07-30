---
title: "Date.AddQuarters | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.AddQuarters

## Syntax

<pre>
Date.AddQuarters(<b>dateTime</b> as any, <b>numberOfQuarters</b> as number) as any  
</pre>
  
## About  
Returns the `date`, `datetime`, or `datetimezone` result from adding `numberOfQuarters` quarters to the `datetime` value `dateTime`. <ul> <li><code>dateTime</code>: The <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to which quarters are being added.</li> <li><code>numberOfQuarters</code>: The number of quarters to add.</li> </ul>

## Example 1
Add 1 quarter to the `date`, `datetime`, or `datetimezone` value representing the date 5/14/2011.

```powerquery-m
Date.AddQuarters(#date(2011, 5, 14), 1)
```

`#date(2011, 8, 14)`
