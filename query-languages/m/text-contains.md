---
description: "Learn more about: Text.Contains"
title: "Text.Contains"
ms.date: 3/14/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Text.Contains

## Syntax

<pre>
Text.Contains(<b>text</b> as nullable text, <b>substring</b> as text, optional <b>comparer</b> as nullable function) as nullable logical
</pre>
  
## About

Detects whether `text` contains the value `substring`. Returns true if the value is found. This function doesn't support wildcards or regular expressions.

The optional argument `comparer` can be used to specify case-insensitive or culture and locale-aware comparisons. The following built-in comparers are available in the formula language:

* [Comparer.Ordinal](/powerquery-m/comparer-ordinal): Used to perform a case-sensitive ordinal comparison
* [Comparer.OrdinalIgnoreCase](/powerquery-m/comparer-ordinalignorecase): Used to perform a case-insensitive ordinal comparison
* [Comparer.FromCulture](/powerquery-m/comparer-fromculture): Used to perform a culture-aware comparison

## Example 1

Find if the text "Hello World" contains "Hello".

**Usage**

```powerquery-m
Text.Contains("Hello World", "Hello")
```

**Output**

`true`

## Example 2

Find if the text "Hello World" contains "hello".

**Usage**

```powerquery-m
Text.Contains("Hello World", "hello")
```

**Output**

`false`

## Example 3

Find if the text "Hello World" contains "hello", using a case-insensitive comparer.

**Usage**

```powerquery-m
Text.Contains("Hello World", "hello", Comparer.OrdinalIgnoreCase)
```

**Output**

`true`
