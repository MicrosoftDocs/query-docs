---
description: "Learn more about: Text.EndsWith"
title: "Text.EndsWith"
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

* [Comparer.Ordinal](/powerquery-m/comparer-ordinal): Used to perform an exact ordinal comparison
* [Comparer.OrdinalIgnoreCase](/powerquery-m/comparer-ordinalignorecase): Used to perform an exact ordinal case-insensitive comparison
* [Comparer.FromCulture](/powerquery-m/comparer-fromculture): Used to perform a culture-aware comparison

## Example 1

Check if "Hello, World" ends with "world".

**Usage**

```powerquery-m
Text.EndsWith("Hello, World", "world")
```

**Output**

`false`

## Example 2

Check if "Hello, World" ends with "World".

**Usage**

```powerquery-m
Text.EndsWith("Hello, World", "World")
```

**Output**

`true`
