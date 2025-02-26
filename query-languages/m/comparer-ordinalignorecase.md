---
description: "Learn more about: Comparer.OrdinalIgnoreCase"
title: "Comparer.OrdinalIgnoreCase"
ms.subservice: m-source
---
# Comparer.OrdinalIgnoreCase

## Syntax

<pre>
Comparer.OrdinalIgnoreCase(<b>x</b> as any, <b>y</b> as any) as number
</pre>

## About

Returns a case-insensitive comparer function which uses Ordinal rules to compare the provided values `x` and `y`.

A comparer function accepts two arguments and returns -1, 0, or 1 based on whether the first value is less than, equal to, or greater than the second.

## Example 1

Using case-insensitive Ordinal rules, compare "Abc" with "abc". Note "Abc" is less than "abc" using `Comparer.Ordinal`.

**Usage**

```powerquery-m
Comparer.OrdinalIgnoreCase("Abc", "abc")
```

**Output**

`0`
