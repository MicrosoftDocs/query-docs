---
title: "Number.Abs | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Number.Abs

## Syntax

<pre>
Number.Abs(<b>number</b> as nullable number) as nullable number
</pre> 
  
## About  
Returns the absolute value of `number`. If `number` is null, `Number.Abs` returns null. <ul> <li><code>number</code>: A <code>number</code> for which the absolute value is to be calculated.</li> </ul>

## Example 1
Absolute value of -3.

```powerquery-m
Number.Abs(-3)
```

`3`
