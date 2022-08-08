---
description: "Learn more about: Splitter.SplitTextByPositions"
title: "Splitter.SplitTextByPositions"
ms.date: 3/16/2022
---
# Splitter.SplitTextByPositions

## Syntax

<pre> 
Splitter.SplitTextByPositions(<b>positions</b> as list, optional <b>startAtEnd</b> as nullable logical) as function
</pre>
  
## About

Returns a function that splits text into a list of text at each specified position.

## Example 1

Split the input at the specified positions, starting from the beginning of the input.

**Usage**

```powerquery-m
Splitter.SplitTextByPositions({0, 3, 4})("ABC|12345")
```

**Output**

`{"ABC", "|", "12345"}`

## Example 2

Split the input at the specified positions, starting from the end of the input.

**Usage**

```powerquery-m
let
    startAtEnd = true
in
    Splitter.SplitTextByPositions({0, 5}, startAtEnd)("Redmond98052")
```

**Output**

`{"Redmond", "98052"}`
