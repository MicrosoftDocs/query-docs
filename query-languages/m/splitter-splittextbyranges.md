---
description: "Learn more about: Splitter.SplitTextByRanges"
title: "Splitter.SplitTextByRanges | Microsoft Docs"
ms.date: 5/19/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Splitter.SplitTextByRanges

## Syntax

<pre>
Splitter.SplitTextByRanges(<b>ranges</b> as list, optional <b>startAtEnd</b> as nullable logical) as function
</pre>
  
## About

Returns a function that splits text into a list of text according to the specified offsets and lengths. A null length indicates that all remaining input should be included.

## Example 1

Split the input by the specified position and length pairs, starting from the beginning of the input. Note that the ranges in this example overlap.

**Usage**

```powerquery-m
Splitter.SplitTextByRanges({{0, 4}, {2, 10}})("codelimiter")
```

**Output**

`{"code", "delimiter"}`

## Example 2

Split the input by the specified position and length pairs, starting from the end of the input.

**Usage**

```powerquery-m
let
    startAtEnd = true
in
    Splitter.SplitTextByRanges({{0, 5}, {6, 2}}, startAtEnd)("RedmondWA?98052")
```

**Output**

`{"WA", "98052"}`
