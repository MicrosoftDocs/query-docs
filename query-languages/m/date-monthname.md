---
title: "Date.MonthName | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Date.MonthName

## Syntax

<pre>
Date.MonthName(<b>date</b> as any, optional <b>culture</b> as nullable text) as nullable text
</pre>

## About
Returns the name of the month component for the provided `date`. An optional `culture` may also be provided (for example, "en-US").

## Example
Get the month name.

```powerquery-m
Date.MonthName(#datetime(2011, 12, 31, 5, 0, 0), "en-US")
```

`"December"`

  
