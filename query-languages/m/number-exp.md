---
description: "Learn more about: Number.Exp"
title: "Number.Exp | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Number.Exp

## Syntax

<pre>
Number.Exp(<b>number</b> as nullable number) as nullable number 
</pre>
  
## About  
Returns the result of raising e to the power of `number` (exponential function). <ul> <li><code>number</code>: A <code>number</code> for which the exponential function is to be calculated. If <code>number</code> is null, <code>Number.Exp</code> returns null. </li> </ul>

## Example 1
Raise e to the power of 3.

```powerquery-m
Number.Exp(3)
```

`20.085536923187668`

