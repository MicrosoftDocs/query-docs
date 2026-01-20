---
description: "Learn more about: Combiner.CombineTextByEachDelimiter"
title: "Combiner.CombineTextByEachDelimiter"
ms.subservice: m-source
ms.topic: reference
---
# Combiner.CombineTextByEachDelimiter

## Syntax

<pre>
Combiner.CombineTextByEachDelimiter(<b>delimiters</b> as list, optional <b>quoteStyle</b> as nullable number) as function
</pre>

## About

Returns a function that combines a list of text values into a single text value using a sequence of delimiters.

## Example 1

Combine a list of text values using a sequence of delimiters.

**Usage**

```powerquery-m
Combiner.CombineTextByEachDelimiter({"=", "+"})({"a", "b", "c"})
```

**Output**

`"a=b+c"`
