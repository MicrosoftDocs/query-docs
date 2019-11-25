---
title: "Date.Month | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Date.Month

## Syntax

<pre>
Date.Month(<b>dateTime</b> as any) as nullable number
</pre>
  
## About  
Returns the month component of the provided `datetime` value, `dateTime`.

## Example 1
Find the month in #datetime(2011, 12, 31, 9, 15, 36).

```powerquery-m
Date.Month(#datetime(2011, 12, 31, 9, 15, 36))
```

`12`
