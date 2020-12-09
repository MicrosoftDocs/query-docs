---
title: "Number.RoundAwayFromZero | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Number.RoundAwayFromZero

## Syntax

<pre>
Number.RoundAwayFromZero(<b>number</b> as nullable number, optional <b>digits</b> as nullable number) as nullable number 
</pre>
  
## About  
Returns the result of rounding `number` based on the sign of the number. This function will round positive numbers up and negative numbers down. If `digits` is specified, `number` is rounded to the `digits` number of decimal digits. 

## Example 1
Round the number -1.2 away from zero.

```powerquery-m
Number.RoundAwayFromZero(-1.2)
```

`-2`

## Example 2
Round the number 1.2 away from zero.

```powerquery-m
Number.RoundAwayFromZero(1.2)
```

`2`

## Example 3
Round the number -1.234 to two decimal places away from zero.

```powerquery-m
Number.RoundAwayFromZero(-1.234, 2)
```

`-1.24`
