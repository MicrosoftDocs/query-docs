---
description: "Learn more about: Number.Round"
title: "Number.Round"
ms.date: 4/13/2022
---
# Number.Round

## Syntax

<pre>
Number.Round(<b>number</b> as nullable number, optional <b>digits</b> as nullable number, optional <b>roundingMode</b> as nullable number) as nullable number
</pre>

## About

Returns the result of rounding `number` to the nearest number. If `number` is null, **Number.Round** returns null.

By default, `number` is rounded to the nearest integer, and ties are broken by rounding to the nearest even number (using [RoundingMode.ToEven](/powerquery-m/roundingmode-toeven), also known as "banker's rounding").

However, these defaults can be overridden via the following optional parameters.

* `digits`: Causes `number` to be rounded to the specified number of decimal digits.
* `roundingMode`: Overrides the default tie-breaking behavior when `number` is at the midpoint between two potential rounded values (refer to [RoundingMode.Type](roundingmode-type.md) for possible values).

## Example 1

Round 1.234 to the nearest integer.

**Usage**

```powerquery-m
Number.Round(1.234)
```

**Output**

`1`

## Example 2

Round 1.56 to the nearest integer.

**Usage**

```powerquery-m
Number.Round(1.56)
```

**Output**

`2`

## Example 3

Round 1.2345 to two decimal places.

**Usage**

```powerquery-m
Number.Round(1.2345, 2)
```

**Output**

`1.23`

## Example 4

Round 1.2345 to three decimal places (Rounding up).

**Usage**

```powerquery-m
Number.Round(1.2345, 3, RoundingMode.Up)
```

**Output**

`1.235`

## Example 5

Round 1.2345 to three decimal places (Rounding down).

**Usage**

```powerquery-m
Number.Round(1.2345, 3, RoundingMode.Down)
```

**Output**

`1.234`
