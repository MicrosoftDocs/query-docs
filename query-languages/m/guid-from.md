---
description: "Learn more about: Guid.From"
title: "Guid.From"
ms.subservice: m-source
ms.topic: reference
---
# Guid.From

## Syntax

<pre>
Guid.From(<b>value</b> as nullable text) as nullable text
</pre>

## About

Returns a `Guid.Type` value from the given `value`. If the given `value` is `null`, **Guid.From** returns `null`. A check will be performed to determine if the given `value` is in an acceptable format. Acceptable formats provided in the examples.

## Example 1

The Guid can be provided as 32 contiguous hexadecimal digits.

**Usage**

```powerquery-m
Guid.From("05FE1DADC8C24F3BA4C2D194116B4967")
```

**Output**

`"05fe1dad-c8c2-4f3b-a4c2-d194116b4967"`

## Example 2

The Guid can be provided as 32 hexadecimal digits separated by hyphens into blocks of 8-4-4-4-12.

**Usage**

```powerquery-m
Guid.From("05FE1DAD-C8C2-4F3B-A4C2-D194116B4967")
```

**Output**

`"05fe1dad-c8c2-4f3b-a4c2-d194116b4967"`

## Example 3

The Guid can be provided as 32 hexadecimal digits separated by hyphens and enclosed in braces.

**Usage**

```powerquery-m
Guid.From("{05FE1DAD-C8C2-4F3B-A4C2-D194116B4967}")
```

**Output**

`"05fe1dad-c8c2-4f3b-a4c2-d194116b4967"`

## Example 4

The Guid can be provided as 32 hexadecimal digits separated by hyphens and enclosed by parentheses.

**Usage**

```powerquery-m
Guid.From("(05FE1DAD-C8C2-4F3B-A4C2-D194116B4967)")
```

**Output**

`"05fe1dad-c8c2-4f3b-a4c2-d194116b4967"`
