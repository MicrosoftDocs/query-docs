---
description: "Learn more about: Combiner.CombineTextByRanges"
title: "Combiner.CombineTextByRanges"
ms.subservice: m-source
ms.topic: reference
---
# Combiner.CombineTextByRanges

## Syntax

<pre>
Combiner.CombineTextByRanges(<b>ranges</b> as list, optional <b>template</b> as nullable text) as function
</pre>

## About

Returns a function that combines a list of text values into a single text value using the specified output positions and lengths. A null length indicates that the entire text value should be included.

## Example 1

Combine a list of text values using the specified output positions and lengths.

**Usage**

```powerquery-m
Combiner.CombineTextByRanges({{0, 1}, {3, 2}, {6, null}})({"abc", "def", "ghijkl"})
```

**Output**

```powerquery-m
"a  de ghijkl"
```
