---
title: "Number.Log10 | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Number.Log10

## Syntax

<pre>
Number.Log10(<b>number</b> as nullable number) as nullable number
</pre>

## About  
Returns the base 10 logarithm of a number, `number`. If `number` is null `Number.Log10` returns null.

## Example 1
Get the base 10 logarithm of 2.

```powerquery-m
Number.Log10(2)
```

`0.3010299956639812`
