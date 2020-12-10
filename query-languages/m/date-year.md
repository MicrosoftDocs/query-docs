---
title: "Date.Year | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.Year

<pre>
Date.Year(<b>dateTime</b> as any) as nullable number
</pre>
  
## About  
Returns the year component of the provided `datetime` value, `dateTime`.

## Example 1
Find the year in #datetime(2011, 12, 31, 9, 15, 36).

```powerquery-m
Date.Year(#datetime(2011, 12, 31, 9, 15, 36))
```

`2011`
