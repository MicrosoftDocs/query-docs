---
description: "Learn more about: Number.Power"
title: "Number.Power | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Number.Power
  
## Syntax

<pre>
Number.Power(<b>number</b> as nullable number, <b>power</b> as nullable number) as nullable number
</pre>
  
## About

Returns the result of raising `number` to the power of `power`. If `number` or `power` are null, **Number.Power** returns null.

* `number`: The base.
* `power`: The exponent.

## Example 1

Find the value of 5 raised to the power of 3 (5 cubed).

**Usage**

```powerquery-m
Number.Power(5, 3)
```

**Output**

`125`
