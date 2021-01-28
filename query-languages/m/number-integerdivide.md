---
description: "Learn more about: Number.IntegerDivide"
title: "Number.IntegerDivide | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Number.IntegerDivide

## Syntax

<pre>
Number.IntegerDivide(<b>number1</b> as nullable number, <b>number2</b> as nullable number, optional <b>precision</b> as nullable number) as nullable number 
</pre>
  
## About  
Returns the integer portion of the result from dividing a number, `number1`, by another number, `number2`. If `number1` or `number2` are null, `Number.IntegerDivide` returns null. <ul> <li><code>number1</code>: The dividend.</li> <li><code>number2</code>: The divisor.</li> </ul>

## Example 1
Divide 6 by 4.

```powerquery-m
Number.IntegerDivide(6, 4)
```

`1`

## Example 2
Divide 8.3 by 3.

```powerquery-m
Number.IntegerDivide(8.3, 3)
```

`2`
