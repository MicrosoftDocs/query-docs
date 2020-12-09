---
title: "Date.DayOfWeekName | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.DayOfWeekName

## Syntax

<pre>
Date.DayOfWeekName(<b>date</b> as any, optional <b>culture</b> as nullable text)
</pre>

## About
Returns the day of the week name for the provided `date`. An optional `culture` may also be provided (for example, "en-US").

## Example 1
Get the day of the week name.

```powerquery-m
Date.DayOfWeekName(#date(2011, 12, 31), "en-US")
```

`"Saturday"`


  
