---
description: "Learn more about: Number.IsEven"
title: "Number.IsEven | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
Number.IsEven(625)
```

**Output**

`false`

## Example 2

Check if 82 is an even number.

**Usage**

```powerquery-m
Number.IsEven(82)
```

**Output**

`true`
