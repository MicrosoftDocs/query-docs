---
description: "Learn more about: Number.RoundUp"
title: "Number.RoundUp"
ms.subservice: m-source
---
# Number.RoundUp

## Syntax

<pre>
Number.RoundUp(<b>number</b> as nullable number, optional <b>digits</b> as nullable number) as nullable number
</pre>
  
## About

Returns the result of rounding `number` up to the next highest integer. If `number` is null, this function returns null. If `digits` is provided, `number` is rounded to the specified number of decimal digits.

## Example 1

Round up 1.234 to integer.

**Usage**

```powerquery-m
Number.RoundUp(1.234)
```

**Output**

`2`

## Example 2

Round up 1.999 to integer.

**Usage**

```powerquery-m
Number.RoundUp(1.999)
```

**Output**

`2`

## Example 3

Round up 1.234 to two decimal places.

**Usage**

```powerquery-m
Number.RoundUp(1.234, 2)
```

**Output**

`1.24`
