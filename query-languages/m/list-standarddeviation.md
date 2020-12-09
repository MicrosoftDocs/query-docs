---
title: "List.StandardDeviation | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.StandardDeviation

## Syntax

<pre>
List.StandardDeviation(<b>numbersList</b> as list) as nullable number
</pre>
  
## About  
Returns a sample based estimate of the standard deviation of the values in the list, `numbersList`. If `numbersList` is a list of numbers, a number is returned. An exception is thrown on an empty list or a list of items that is not type `number`.

## Example 1
Find the standard deviation of the numbers 1 through 5.

```powerquery-m
List.StandardDeviation({1..5})
```

`1.5811388300841898`
