---
title: "Number.Mod | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Number.Mod

## Syntax

<pre>
Number.Mod(<b>number</b> as nullable number, <b>divisor</b> as nullable number, optional <b>precision</b> as nullable number) as nullable number
</pre>
  
## About  
Returns the remainder resulting from the integer division of `number` by `divisor`. If `number` or `divisor` are null, `Number.Mod` returns null. <ul> <li><code>number</code>: The dividend.</li> <li><code>divisor</code>: The divisor.</li> </ul>

## Example 1
Find the remainder when you divide 5 by 3.

```powerquery-m
Number.Mod(5, 3)
```

`2`
