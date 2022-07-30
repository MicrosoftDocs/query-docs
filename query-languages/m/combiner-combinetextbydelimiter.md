---
description: "Learn more about: Combiner.CombineTextByDelimiter"
title: "Combiner.CombineTextByDelimiter"
ms.date: 3/11/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Combiner.CombineTextByDelimiter

## Syntax

<pre>
Combiner.CombineTextByDelimiter(<b>delimiter</b> as text, optional <b>quoteStyle</b> as nullable number) as function
</pre>
  
## About

Returns a function that combines a list of text into a single text using the specified delimiter.

## Example 1

Combine a list of text values using a semicolon delimiter.

**Usage**

```powerquery-m
Combiner.CombineTextByDelimiter(";")({"a", "b", "c"})
```

**Output**

`"a;b;c"`
