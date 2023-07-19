---
description: "Learn more about: Number.ToText"
title: "Number.ToText"
ms.date: 7/18/2023
---
# Number.ToText

## Syntax

<pre>
Number.ToText(<b>number</b> as nullable number, optional <b>format</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text
</pre>
  
## About

Converts the numeric value `number` to a text value according to the format specified by `format`.

The format is a text value indicating how the number should be converted. For more details on the supported format values, go to [https://go.microsoft.com/fwlink/?linkid=2241210](https://go.microsoft.com/fwlink/?linkid=2241210) and [https://go.microsoft.com/fwlink/?linkid=2240884](https://go.microsoft.com/fwlink/?linkid=2240884).

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
