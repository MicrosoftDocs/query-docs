---
title: "Date.MonthName | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.MonthName

## Syntax

<pre>
Date.MonthName(**date** as any, optional **culture** as nullable text)
</pre>

## About
Returns the name of the month component for the provided `date` and, optionally, a culture `culture`.

## Example
Get the month name.

```powerquery-m
Date.MonthName(#datetime(2011, 12, 31, 5, 0, 0), "en-US")
```

`"December"`

  
