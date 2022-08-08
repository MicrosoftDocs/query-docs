---
description: "Learn more about: Number.ToText"
title: "Number.ToText"
ms.date: 3/11/2022
---
# Number.ToText

## Syntax

<pre>
Number.ToText(<b>number</b> as nullable number, optional <b>format</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text
</pre>
  
## About

Formats the numeric value `number` to a text value according to the format specified by `format`. The format is a single character code optionally followed by a number precision specifier. The following character codes may be used for `format`.

* "D" or "d": (Decimal) Formats the result as integer digits. The precision specifier controls the number of digits in the output.
* "E" or "e": (Exponential/scientific) Exponential notation. The precision specifier controls the maximum number of decimal digits (default is 6).
* "F" or "f": (Fixed-point) Integral and decimal digits.
* "G" or "g": (General) Most compact form of either fixed-point or scientific.
* "N" or "n": (Number) Integral and decimal digits with group separators and a decimal separator.
* "P" or "p": (Percent) Number multiplied by 100 and displayed with a percent symbol.
* "R" or "r": (Round-trip) A text value that can round-trip an identical number. The precision specifier is ignored.
* "X" or "x": (Hexadecimal) A hexadecimal text value.

An optional `culture` may also be provided (for example, "en-US").

## Example 1

Format a number as text without format specified.

**Usage**

```powerquery-m
Number.ToText(4)
```

**Output**

`"4"`

## Example 2

Format a number as text in Exponential format.

**Usage**

```powerquery-m
Number.ToText(4, "e")
```

**Output**

`"4.000000e+000"`

## Example 3

Format a number as text in Decimal format with limited precision.

**Usage**

```powerquery-m
Number.ToText(-0.1234, "P1")
```

**Output**

`"-12.3 %"`
