---
description: "Learn more about: Comparer.FromCulture"
title: "Comparer.FromCulture"
---
# Comparer.FromCulture

## Syntax

<pre>
Comparer.FromCulture(<b>culture</b> as text, optional <b>ignoreCase</b> as nullable logical) as function
</pre>

## About

Returns a comparer function that uses the `culture` and the case-sensitivity specified by `ignoreCase` to perform comparisons.

A comparer function accepts two arguments and returns -1, 0, or 1 based on whether the first value is less than, equal to, or greater than the second.

The default value for `ignoreCase` is false. The `culture` should be one of the locales supported by the .NET framework (for example, "en-US").

## Example 1

Compare "a" and "A" using "en-US" locale to determine if the values are equal.

**Usage**

```powerquery-m
Comparer.FromCulture("en-US")("a", "A")
```

**Output**

`-1`

## Example 2

Compare "a" and "A" using "en-US" locale ignoring the case to determine if the values are equal.

**Usage**

```powerquery-m
Comparer.FromCulture("en-US", true)("a", "A")
```

**Output**

`0`
