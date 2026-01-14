---
description: "Learn more about: Number.Cos"
title: "Number.Cos"
ms.subservice: m-source
ms.topic: reference
---
# Number.Cos

## Syntax

<pre>
Number.Cos(<b>number</b> as nullable number) as nullable number
</pre>

## About

Returns the cosine of the specified angle.

* `number`: An angle, measured in radians.

## Example 1

Find the cosine of the angle 0.

**Usage**

```powerquery-m
Number.Cos(0)
```

**Output**

`1`

## Example 2

Find the cosine of π radians.

**Usage**

```powerquery-m
Number.Cos(Number.PI)
```

**Output**

`-1`
