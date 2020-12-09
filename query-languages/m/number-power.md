---
title: "Number.Power | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Number.Power
  
## Syntax

<pre>
Number.Power(<b>number</b> as nullable number, <b>power</b> as nullable number) as nullable number 
</pre>
  
## About  
Returns the result of raising `number` to the power of `power`. If `number` or `power` are null, `Number.Power` returns null. <ul> <li><code>number</code>: The base.</li> <li><code>power</code>: The exponent.</li> </ul>

## Example 1
Find the value of 5 raised to the power of 3 (5 cubed).

```powerquery-m
Number.Power(5, 3)
```

`125`
