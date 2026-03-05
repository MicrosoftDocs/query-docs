---
description: "Learn more about: Splitter.SplitTextByEachDelimiter"
title: "Splitter.SplitTextByEachDelimiter"
ms.subservice: m-source
ms.topic: reference
---
# Splitter.SplitTextByEachDelimiter

## Syntax

<pre>
Splitter.SplitTextByEachDelimiter(
    <b>delimiters</b> as list,
    optional <b>quoteStyle</b> as nullable number,
    optional <b>startAtEnd</b> as nullable logical
) as function
</pre>
  
## About

Returns a function that splits text into a list of text at each specified delimiter in sequence.

## Example 1

Split the input by comma, then semicolon, starting from the beginning of the input.

**Usage**

```powerquery-m
Splitter.SplitTextByEachDelimiter({",", ";"})("a,b;c,d")
```

**Output**

`{"a", "b", "c,d"}`

## Example 2

Split the input by comma, then semicolon, treating quotes like any other character and starting from the end of the input.

**Usage**

```powerquery-m
let
    startAtEnd = true
in
    Splitter.SplitTextByEachDelimiter({",", ";"}, QuoteStyle.None, startAtEnd)("a,""b;c"",d")
```

**Output**

`{"a,""b", "c""", "d"}`
