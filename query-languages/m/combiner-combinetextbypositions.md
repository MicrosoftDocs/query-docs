---
description: "Learn more about: Combiner.CombineTextByPositions"
title: "Combiner.CombineTextByPositions"
ms.subservice: m-source
ms.topic: reference
---
# Combiner.CombineTextByPositions

## Syntax

<pre>
Combiner.CombineTextByPositions(<b>positions</b> as list, optional <b>template</b> as nullable text) as function
</pre>

## About

Returns a function that combines a list of text values into a single text value using the specified output positions.

## Example 1

Combine a list of text values by placing them in the output at the specified positions.

**Usage**

```powerquery-m
Combiner.CombineTextByPositions({0, 5, 10})({"abc", "def", "ghi"})
```

**Output**

```powerquery-m
"abc  def  ghi"
```
