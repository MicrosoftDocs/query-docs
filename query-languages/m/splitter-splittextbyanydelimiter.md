---
description: "Learn more about: Splitter.SplitTextByAnyDelimiter"
title: "Splitter.SplitTextByAnyDelimiter"
---
# Splitter.SplitTextByAnyDelimiter

## Syntax

<pre>
Splitter.SplitTextByAnyDelimiter(<b>delimiters</b> as list, optional <b>quoteStyle</b> as nullable number, optional <b>startAtEnd</b> as nullable logical) as function
</pre>
  
## About

Returns a function that splits text into a list of text at any of the specified delimiters.

## Example 1

Split the input by comma or semicolon, ignoring quotes and quoted delimiters and starting from the beginning of the input.

**Usage**

```powerquery-m
Splitter.SplitTextByAnyDelimiter({",", ";"}, QuoteStyle.Csv)("a,b;""c,d;e"",f")
```

**Output**

`{"a", "b", "c,d;e", "f"}`

## Example 2

Split the input by comma or semicolon, ignoring quotes and quoted delimiters and starting from the end of the input.

**Usage**

```powerquery-m
let
    startAtEnd = true
in
    Splitter.SplitTextByAnyDelimiter({",", ";"}, QuoteStyle.Csv, startAtEnd)("a,""b;c,d")
```

**Output**

`{"a,b", "c", "d"}`
