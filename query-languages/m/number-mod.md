---
description: "Learn more about: Number.Mod"
title: "Number.Mod"
ms.subservice: m-source
ms.topic: reference
---
# Number.Mod

## Syntax

<pre>
Number.Mod(
    <b>number</b> as nullable number,
    <b>divisor</b> as nullable number,
    optional <b>precision</b> as nullable number
) as nullable number
</pre>
  
## About

Returns the remainder resulting from the integer division of `number` by `divisor`. If `number` or `divisor` are `null`, this function returns `null`.

* `number`: The dividend.
* `divisor`: The divisor.
* `precision`: (Optional) The precision of the integer division. This parameter can be either [Precision.Double](precision-type.md) for `Double` precision or [Precision.Decimal](precision-type.md) for `Decimal` precision. The default value is `Precision.Double`.

## Example 1

Find the remainder when you divide 5 by 3.

**Usage**

```powerquery-m
Number.Mod(5, 3)
```

**Output**

`2`

## Example 2

Find the remainder when you divide 10.5 by 0.2, using both `Double` precision and `Decimal` precision.

**Usage**

```powerquery-m
let
    Dividend = 10.5,
    Divisor = 0.2,

    #"Use Double Precision" = Number.Mod(Dividend, Divisor, Precision.Double),
    #"Use Decimal Precision" = Number.Mod(Dividend, Divisor, Precision.Decimal),

    // Convert to text to inspect precision
    #"Double To Text" = Number.ToText(#"Use Double Precision", "G"),
    #"Decimal To Text" = Number.ToText(#"Use Decimal Precision", "G"),
    
    #"Display Result" = [
        DoublePrecision = #"Double To Text",
        DecimalPrecision = #"Decimal To Text"
    ]

in
    #"Display Result"
```

**Output**

```powerquery-m
[
    DoublePrecision = "0.0999999999999994",
    DecimalPrecision = "0.1"
]
```
