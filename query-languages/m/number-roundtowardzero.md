---
title: "Number.RoundTowardZero | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Number.RoundTowardZero

## Syntax

<pre>
Number.RoundTowardZero(<b>number</b> as nullable number, optional <b>digits</b> as nullable number) as nullable number 
</pre>
  
## About  
Returns the result of rounding `number` based on the sign of the number. This function will round positive numbers down and negative numbers up. If `digits` is specified, `number` is rounded to the `digits` number of decimal digits. 
