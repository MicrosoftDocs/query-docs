---
title: "List.Product | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# List.Product

## Syntax

<pre>
List.Product(<b>numbersList</b> as list, optional <b>precision</b> as nullable number) as nullable number 
</pre>
  
## About  
Returns the product of the non-null numbers in the list, `numbersList`. Returns null if there are no non-null values in the list.

## Example 1
Find the product of the numbers in the list `{1, 2, 3, 3, 4, 5, 5}`.

```powerquery-m
List.Product({1, 2, 3, 3, 4, 5, 5})
```

`1800`
