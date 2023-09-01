---
description: "Learn more about: Comparer.OrdinalIgnoreCase"
title: "Comparer.OrdinalIgnoreCase"
---
# Comparer.OrdinalIgnoreCase

## Syntax

<pre>
Comparer.OrdinalIgnoreCase(<b>x</b> as any, <b>y</b> as any) as number
</pre>

## About

Returns a case-insensitive comparer function which uses Ordinal rules to compare the provided values `x` and `y`.

## Example 1

Using case-insensitive Ordinal rules, compare "Abc" with "abc". Note "Abc" is less than "abc" using `Comparer.Ordinal`.

**Usage**

```powerquery-m
Comparer.OrdinalIgnoreCase("Abc", "abc")
```

**Output**

`0`
