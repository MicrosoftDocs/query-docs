---
title: "Number.RandomBetween | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Number.RandomBetween

## Syntax

<pre>
Number.RandomBetween(<b>bottom</b> as number, <b>top</b> as number) as number
</pre>
  
## About  
Returns a random number between `bottom` and `top`.

## Example 1
Get a random number between 1 and 5.

```powerquery-m
Number.RandomBetween(1, 5)
```

`2.546797`
