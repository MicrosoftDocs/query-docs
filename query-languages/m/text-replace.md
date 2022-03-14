---
description: "Learn more about: Text.Replace"
title: "Text.Replace | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.Replace

## Syntax

<pre>
Text.Replace(<b>text</b> as nullable text, <b>old</b> as text, <b>new</b> as text) as nullable text
</pre>
  
## About

Returns the result of replacing all occurrences of text value `old` in text value `text` with text value `new`. This function is case sensitive.

## Example 1

Replace every occurrence of "the" in a sentence with "a".

**Usage**

```powerquery-m
Text.Replace("the quick brown fox jumps over the lazy dog", "the", "a")
```

**Output**

`"a quick brown fox jumps over a lazy dog"`
