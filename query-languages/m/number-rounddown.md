---
description: "Learn more about: Number.RoundDown"
title: "Number.RoundDown"
ms.date: 4/13/2022
---
# Number.RoundDown

## Syntax

<pre>
Number.RoundDown(<b>number</b> as nullable number, optional <b>digits</b> as nullable number) as nullable number
</pre>
  
## About

Returns the result of rounding `number` down to the previous highest integer. If `number` is null, this function returns null. If `digits` is provided, `number` is rounded to the specified number of decimal digits.

## Example 1

Round down 1.234 to integer.

**Usage**

```powerquery-m
Number.RoundDown(1.234)
```

**Output**

`1`

## Example 2

Round down 1.999 to integer.

**Usage**

```powerquery-m
Number.RoundDown(1.999)
```

**Output**

`1`

## Example 3

Round down 1.999 to two decimal places.

**Usage**

```powerquery-m
Number.RoundDown(1.999, 2)
```

**Output**

`1.99`
