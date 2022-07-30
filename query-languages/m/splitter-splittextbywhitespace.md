---
description: "Learn more about: Splitter.SplitTextByWhitespace"
title: "Splitter.SplitTextByWhitespace"
ms.date: 3/16/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Splitter.SplitTextByWhitespace

## Syntax

<pre>
Splitter.SplitTextByWhitespace(optional <b>quoteStyle</b> as nullable number) as function
</pre>
  
## About

Returns a function that splits text into a list of text at whitespace.

## Example 1

Split the input by whitespace characters, treating quotes like any other character.

**Usage**

```powerquery-m
Splitter.SplitTextByWhitespace(QuoteStyle.None)("a b#(tab)c")
```

**Output**

`{"a", "b", "c"}`
