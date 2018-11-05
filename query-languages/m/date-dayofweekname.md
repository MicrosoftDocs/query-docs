---
title: "Date.DayOfWeekName | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.DayOfWeekName

## Syntax

<pre>  
Date.DayOfWeekName(**date** as any, optional **culture** as nullable text)
</pre>

## About
Returns the day of the week name for the provided `date` and, optionally, a culture `culture`.

## Example
Get the day of the week name.

```powerquery-m
Date.DayOfWeekName(#date(2011, 12, 31), "en-US")
```

`"Saturday"`


  
