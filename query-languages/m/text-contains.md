---
description: "Learn more about: Text.Contains"
title: "Text.Contains | Microsoft Docs"
ms.date: 1/24/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.Contains

## Syntax

<pre>
Text.Contains(<b>text</b> as nullable text, <b>substring</b> as text, optional <b>comparer</b> as nullable function) as nullable logical
</pre>
  
## About

Detects whether `text` contains the value `substring`. Returns true if the value is found. This function doesn't support wildcards or regular expressions.

The optional argument `comparer` can be used to specify case-insensitive or culture and locale-aware comparisons. The following built-in comparers are available in the formula language:

* `Comparer.Ordinal`: Used to perform a case-sensitive ordinal comparison
* `Comparer.OrdinalIgnoreCase`: Used to perform a case-insensitive ordinal comparison
* `Comparer.FromCulture`: Used to perform a culture-aware comparison

## Example 1

Find if the text "Hello World" contains "Hello".

```powerquery-m
Text.Contains("Hello World", "Hello")
```

`true`

## Example 2

Find if the text "Hello World" contains "hello".

```powerquery-m
Text.Contains("Hello World", "hello")
```

`false`

## Example 3

Find if the text "Hello World" contains "hello", using a case-insensitive comparer.

```powerquery-m
Text.Contains("Hello World", "hello", Comparer.OrdinalIgnoreCase)
```

`true`
