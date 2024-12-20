---
description: "Learn more about: Text.PositionOf"
title: "Text.PositionOf"
ms.subservice: m-source
---
# Text.PositionOf

## Syntax

<pre>
Text.PositionOf(<b>text</b> as text, <b>substring</b> as text, optional <b>occurrence</b> as nullable number, optional <b>comparer</b> as nullable function) as any
</pre>

## About

Returns the position of the specified occurrence of the text value `substring` found in `text`. An optional parameter `occurrence` may be used to specify which occurrence position to return (first occurrence by default). Returns -1 if `substring` was not found.

`comparer` is a `Comparer` which is used to control the comparison. Comparers can be used to provide case-insensitive or culture and locale-aware comparisons.

The following built-in comparers are available in the formula language:

* `Comparer.Ordinal`: Used to perform an exact ordinal comparison
* `Comparer.OrdinalIgnoreCase`: Used to perform an exact ordinal case-insensitive comparison
* `Comparer.FromCulture`: Used to perform a culture-aware comparison

## Example 1

Get the position of the first occurrence of "World" in the text "Hello, World! Hello, World!".

**Usage**

```powerquery-m
Text.PositionOf("Hello, World! Hello, World!", "World")
```

**Output**

`7`

## Example 2

Get the position of last occurrence of "World" in "Hello, World! Hello, World!".

**Usage**

```powerquery-m
Text.PositionOf("Hello, World! Hello, World!", "World", Occurrence.Last)
```

**Output**

`21`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
