---
description: "Learn more about: Number.IsNaN"
title: "Number.IsNaN | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Number.IsNaN

## Syntax

<pre>
Number.IsNaN(<b>number</b> as number) as logical
</pre>
  
## About

Indicates if the value is NaN (Not a number). Returns `true` if `number` is equivalent to **Number.IsNaN**, `false` otherwise.

## Example 1

Check if 0 divided by 0 is NaN.

**Usage**

```powerquery-m
Number.IsNaN(0/0)
```

**Output**

`true`

## Example 2

Check if 1 divided by 0 is NaN.

**Usage**

```powerquery-m
Number.IsNaN(1/0)
```

**Output**

`false`
