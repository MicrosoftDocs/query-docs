---
description: "Learn more about: List.StandardDeviation"
title: "List.StandardDeviation | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
List.StandardDeviation({1..5})
```

**Outut**

`1.5811388300841898`
