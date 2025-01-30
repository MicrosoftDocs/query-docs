---
description: "Learn more about: Splitter.SplitTextByLengths"
title: "Splitter.SplitTextByLengths"
ms.subservice: m-source
---
# Splitter.SplitTextByLengths

## Syntax

<pre>
Splitter.SplitTextByLengths(<b>lengths</b> as list, optional <b>startAtEnd</b> as nullable logical) as function
</pre>
  
## About

Returns a function that splits text into a list of text by each specified length.

## Example 1

Split the input into the first two characters followed by the next three, starting from the beginning of the input.

**Usage**

```powerquery-m
Splitter.SplitTextByLengths({2, 3})("AB123")
```

**Output**

`{"AB", "123"}`

## Example 2

Split the input into the first three characters followed by the next two, starting from the end of the input.

**Usage**

```powerquery-m
let
    startAtEnd = true
in
    Splitter.SplitTextByLengths({5, 2}, startAtEnd)("RedmondWA98052")
```

`{"WA", "98052"}`
