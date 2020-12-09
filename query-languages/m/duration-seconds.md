---
title: "Duration.Seconds | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Duration.Seconds

## Syntax

<pre>
Duration.Seconds(<b>duration</b> as nullable duration) as nullable number
</pre>
  
## About  
Returns the seconds component of the provided `duration` value, `duration`.

## Example 1
Find the seconds in #duration(5, 4, 3, 2).

```powerquery-m
Duration.Seconds(#duration(5, 4, 3, 2))
```

`2`
