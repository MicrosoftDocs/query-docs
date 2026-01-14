---
description: "Learn more about: Number.Exp"
title: "Number.Exp"
ms.subservice: m-source
ms.topic: reference
---
# Number.Exp

## Syntax

<pre>
Number.Exp(<b>number</b> as nullable number) as nullable number
</pre>

## About

Returns the result of raising e to the power of `number` (exponential function).

* `number`: A `number` for which the exponential function is to be calculated. If `number` is null, **Number.Exp** returns null.

## Example 1

Raise e to the power of 3.

**Usage**

```powerquery-m
Number.Exp(3)
```

**Output**

`20.085536923187668`
