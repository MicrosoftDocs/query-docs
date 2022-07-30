---
description: "Learn more about: Number.Ln"
title: "Number.Ln | Microsoft Docs"
ms.date: 3/9/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Number.Ln

## Syntax

<pre>
Number.Ln(<b>number</b> as nullable number) as nullable number
</pre>
  
## About

Returns the natural logarithm of a number, `number`. If `number` is null `Number.Ln` returns null.

## Example 1

Get the natural logarithm of 15.

**Usage**

```powerquery-m
Number.Ln(15)
```

**Output**

`2.70805020110221`
