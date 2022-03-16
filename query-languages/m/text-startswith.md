---
description: "Learn more about: Text.StartsWith"
title: "Text.StartsWith | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.StartsWith

## Syntax

<pre>
Text.StartsWith(<b>text</b> as nullable text, <b>substring</b> as text, optional <b>comparer</b> as nullable function) as nullable logical
</pre>
  
## About

Returns true if text value `text` starts with text value `substring`.

* `text`: A `text` value which is to be searched
* `substring`: A `text` value which is the substring to be searched for in `substring`
* `comparer`: *[Optional]* A `Comparer` used for controlling the comparison. For example, `Comparer.OrdinalIgnoreCase` may be used to perform case-insensitive searches

`comparer` is a `Comparer` which is used to control the comparison. Comparers can be used to provide case-insensitive or culture and locale-aware comparisons.

The following built-in comparers are available in the formula language:

* `Comparer.Ordinal`: Used to perform an exact ordinal comparison
* `Comparer.OrdinalIgnoreCase`: Used to perform an exact ordinal case-insensitive comparison
* `Comparer.FromCulture`: Used to perform a culture-aware comparison

## Example 1

Check if the text "Hello, World" starts with the text "hello".

**Usage**

```powerquery-m
Text.StartsWith("Hello, World", "hello")
```

**Output**

`false`

## Example 2

Check if the text "Hello, World" starts with the text "Hello".

**Usage**

```powerquery-m
Text.StartsWith("Hello, World", "Hello")
```

**Output**

`true`
