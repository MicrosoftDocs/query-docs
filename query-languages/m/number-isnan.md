---
title: "Number.IsNaN | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.IsNaN

## Syntax

<pre>
Number.IsNaN(<b>number</b> as number) as logical
</pre>
  
## About  
Indicates if the value is NaN (Not a number). Returns `true` if `number` is equivalent to `Number.IsNaN`, `false` otherwise.

## Example 1
Check if 0 divided by 0 is NaN.

```powerquery-m
Number.IsNaN(0/0)
```

`true`

## Example 2
Check if 1 divided by 0 is NaN.

```powerquery-m
Number.IsNaN(1/0)
```

`false`

