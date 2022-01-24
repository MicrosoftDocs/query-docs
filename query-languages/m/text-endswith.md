---
description: "Learn more about: Text.EndsWith"
title: "Text.EndsWith | Microsoft Docs"
ms.date: 1/24/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.EndsWith

## Syntax

<pre>
Text.EndsWith(<b>text</b> as nullable text, <b>substring</b> as text, optional <b>comparer</b> as nullable function) as nullable logical
</pre>
  
## About

Indicates whether the given text, `text`, ends with the specified value, `substring`. The indication is case sensitive.

`comparer` is a `Comparer` which is used to control the comparison. Comparers can be used to provide case-insensitive or culture and locale-aware comparisons.

The following built-in comparers are available in the formula language:

* `Comparer.Ordinal`: Used to perform an exact ordinal comparison
* `Comparer.OrdinalIgnoreCase`: Used to perform an exact ordinal case-insensitive comparison
* `Comparer.FromCulture`: Used to perform a culture-aware comparison

## Example 1

Check if "Hello, World" ends with "world".

```powerquery-m
Text.EndsWith("Hello, World", "world")
```

`false`

## Example 2

Check if "Hello, World" ends with "World".

```powerquery-m
Text.EndsWith("Hello, World", "World")
```

`true`
