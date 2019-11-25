---
title: "Date.DayOfWeekName | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Date.DayOfWeekName

## Syntax

<pre>
Date.DayOfWeekName(<b>date</b> as any, optional <b>culture</b> as nullable text)
</pre>

## About
Returns the day of the week name for the provided `date` and, optionally, a culture `culture`.

## Example 1
Get the day of the week name.

```powerquery-m
Date.DayOfWeekName(#date(2011, 12, 31), "en-US")
```

`"Saturday"`


  
