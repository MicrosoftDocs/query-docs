---
description: "Learn more about: Splitter.SplitTextByDelimiter"
title: "Splitter.SplitTextByDelimiter | Microsoft Docs"
ms.date: 3/16/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Splitter.SplitTextByDelimiter

## Syntax

<pre>
Splitter.SplitTextByDelimiter(<b>delimiter</b> as text, optional <b>quoteStyle</b> as nullable number) as function
</pre>
  
## About

Returns a function that splits text into a list of text according to the specified delimiter.

## Example 1

Split the input by comma, ignoring quoted commas.

**Usage**

```powerquery-m
Splitter.SplitTextByDelimiter(",", QuoteStyle.Csv)("a,""b,c"",d")
```

**Output**

`{"a", "b,c", "d"}`
