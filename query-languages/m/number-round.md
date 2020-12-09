---
title: "Number.Round | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Number.Round

## Syntax

<pre>
Number.Round(<b>number</b> as nullable number, optional <b>digits</b> as nullable number, optional <b>roundingMode</b> as nullable number) as nullable number
</pre>
  
## About  
Returns the result of rounding `number` to the nearest number. If `number` is null, `Number.Round` returns null. `number` is rounded to the nearest integer, unless the optional parameter `digits` is specified. If `digits` is specified, `number` is rounded to the `digits` number of decimal digits. An optional `roundingMode` parameter specifies rounding direction when there is a tie between the possible numbers to round to (see `RoundingMode.Type` for possible values).

## Example 1
Round 1.234 to the nearest integer.

```powerquery-m
Number.Round(1.234)
```

`1`

## Example 2
Round 1.56 to the nearest integer.

```powerquery-m
Number.Round(1.56)
```

`2`

## Example 3
Round 1.2345 to two decimal places.

```powerquery-m
Number.Round(1.2345, 2)
```

`1.23`

## Example 4
Round 1.2345 to three decimal places (Rounding up).

```powerquery-m
Number.Round(1.2345, 3, RoundingMode.Up)
```

`1.235`

## Example 5
Round 1.2345 to three decimal places (Rounding down).

```powerquery-m
Number.Round(1.2345, 3, RoundingMode.Down)
```

`1.234`
