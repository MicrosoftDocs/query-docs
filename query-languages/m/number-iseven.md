---
title: "Number.IsEven | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.IsEven

## Syntax

<pre>
Number.IsEven(<b>number</b> as number) as logical 
</pre>
  
## About  
Indicates if the value, `number`, is even by returning `true` if it is even, `false` otherwise.

## Example 1
Check if 625 is an even number.

```powerquery-m
Number.IsEven(625)
```

`false`

## Example 2
Check if 82 is an even number.

```powerquery-m
Number.IsEven(82)
```

`true`
