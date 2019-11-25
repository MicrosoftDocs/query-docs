---
title: "Number.Sqrt | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Number.Sqrt

## Syntax

<pre>
Number.Sqrt(<b>number</b> as nullable number) as nullable number
</pre>
  
## About  
Returns the square root of `number`. If `number` is null, `Number.Sqrt` returns null. If it is a negative value, `Number.NaN` is returned (Not a number).

## Example 1
Find the square root of 625.

```powerquery-m
Number.Sqrt(625)
```

`25`

## Example 2
Find the square root of 85.

```powerquery-m
Number.Sqrt(85)
```

`9.2195444572928871`
