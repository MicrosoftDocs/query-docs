---
description: "Learn more about: Comparer.Equals"
title: "Comparer.Equals | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Comparer.Equals

## Syntax

<pre>
Comparer.Equals(comparer as function, x as any, y as any) as logical  
</pre>
  
## About

Returns a `logical` value based on the equality check over the two given values, `x` and `y`, using the provided `comparer`.

`comparer` is a `Comparer` which is used to control the comparison. Comparers can be used to provide case-insensitive or culture and locale-aware comparisons.

The following built-in comparers are available in the formula language:

* `Comparer.Ordinal`: Used to perform an exact ordinal comparison
* `Comparer.OrdinalIgnoreCase`: Used to perform an exact ordinal case-insensitive comparison
* `Comparer.FromCulture`: Used to perform a culture-aware comparison

## Example 1

Compare "1" and "A" using "en-US" locale to determine if the values are equal.

**Usage**

```powerquery-m
Comparer.Equals(Comparer.FromCulture("en-US"), "1", "A")
```

**Output**

`false`
