---
title: "Number.ToText | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.ToText

## Syntax

<pre>
Number.ToText(<b>number</b> as nullable number, optional <b>format</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text 
</pre>
  
## About  
Formats the numeric value `number` to a text value according to the format specified by `format`. The format is a single character code optionally followed by a number precision specifier. The following character codes may be used for `format`. <ul> <li>"D" or "d": (Decimal) Formats the result as integer digits. The precision specifier controls the number of digits in the output. </li> <li>"E" or "e": (Exponential [scientific]) Exponential notation. The precision specifier controls the maximum number of decimal digits (default is 6). </li> <li>"F" or "f": (Fixed-point) Integral and decimal digits.</li> <li>"G" or "g": (General) Most compact form of either fixed-point or scientific. </li> <li>"N" or "n": (Number) Integral and decimal digits with group separators and a decimal separator. </li> <li>"P" or "p": (Percent) Number multiplied by 100 and displayed with a percent symbol. </li> <li>"R" or "r": (Round-trip) A text value that can round-trip an identical number. The precision specifier is ignored. </li> <li>"X" or "x": (Hexadecimal) A hexadecimal text value. </li> </ul>

## Example 1
Format a number as text without format specified.

```powerquery-m
Number.ToText(4)
```

`"4"`

## Example 2
Format a number as text in Exponential format.

```powerquery-m
Number.ToText(4, "e")
```

`"4.000000e+000"`

## Example 3
Format a number as text in Decimal format with limited precision.

```powerquery-m
Number.ToText(-0.1234, "P1")
```

`"-12.3 %"`
