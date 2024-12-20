---
description: "Learn more about: Number.ToText"
title: "Number.ToText"
ms.subservice: m-source
---
# Number.ToText

## Syntax

<pre>
Number.ToText(<b>number</b> as nullable number, optional <b>format</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text
</pre>
  
## About

Converts the numeric value `number` to a text value according to the format specified by `format`.

The format is a text value indicating how the number should be converted. For more details on the supported format values, go to [Standard numeric format strings](standard-numeric-format-strings.md) and [Custom numeric format strings](custom-numeric-format-strings.md).

An optional `culture` may also be provided (for example, "en-US") to control the culture-dependent behavior of `format`.

## Example 1

Convert a number to text without specifying a format.

**Usage**

```powerquery-m
Number.ToText(4)
```

**Output**

`"4"`

## Example 2

Convert a number to exponential format.

**Usage**

```powerquery-m
Number.ToText(4, "e")
```

**Output**

`"4.000000e+000"`

## Example 3

Convert a number to percentage format with only one decimal place.

**Usage**

```powerquery-m
Number.ToText(-0.1234, "P1")
```

**Output**

`"-12.3 %"`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
* [Standard numeric format strings](standard-numeric-format-strings.md)
* [Custom numeric format strings](custom-numeric-format-strings.md)
