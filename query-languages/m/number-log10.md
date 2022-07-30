---
description: "Learn more about: Number.Log10"
title: "Number.Log10"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Number.Log10

## Syntax

<pre>
Number.Log10(<b>number</b> as nullable number) as nullable number
</pre>

## About

Returns the base 10 logarithm of a number, `number`. If `number` is null **Number.Log10** returns null.

## Example 1

Get the base 10 logarithm of 2.

**Usage**

```powerquery-m
Number.Log10(2)
```

**Output**

`0.3010299956639812`
