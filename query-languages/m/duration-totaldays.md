---
title: "Duration.TotalDays | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Duration.TotalDays

## Syntax

<pre>
Duration.TotalDays(<b>duration</b> as nullable duration) as nullable number
</pre>
  
## About  
Returns the total days spanned by the provided `duration` value, `duration`.

## Example 1
Find the total days spanned in #duration(5, 4, 3, 2).

```powerquery-m
Duration.TotalDays(#duration(5, 4, 3, 2))
```

`5.1687731481481478`
