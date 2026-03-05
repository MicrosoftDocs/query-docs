---
description: "Learn more about: FIXED"
title: "FIXED function (DAX)"
ms.topic: reference
---
# FIXED

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Rounds a number to the specified number of decimals and returns the result as text. You can specify that the result be returned with or without commas.

## Syntax

```dax
FIXED(<number>, <decimals>, <no_commas>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`number`|The number you want to round and convert to text, or a column containing a number.|
|`decimals`|(optional) The number of digits to the right of the decimal point; if omitted, 2.|
|`no_commas`|(optional) A logical value: if 1, do not display commas in the returned text; if 0 or omitted, display commas in the returned text.|

## Return value

A number represented as text.

## Remarks

- If the value used for the `decimals` parameter is negative, `number` is rounded to the left of the decimal point.

- If you omit `decimals`, it is assumed to be 2.

- If `no_commas` is 0 or is omitted, then the returned text includes commas as usual.

- The major difference between formatting a cell containing a number by using a command and formatting a number directly with the FIXED function is that FIXED converts its result to text. A number formatted with a command from the formatting menu is still a number.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following formula used in a calculated column gets the numeric value for the current row in Product[List Price] and returns it as text with 2 decimal places and no commas.

[!INCLUDE [power-bi-dax-sample-model](includes/power-bi-dax-sample-model.md)]

```dax
= FIXED([List Price],2,1)
```

## Related content

- [CEILING](ceiling-function-dax.md)
- [FLOOR](floor-function-dax.md)
- [ISO.CEILING](iso-ceiling-function-dax.md)
- [MROUND](mround-function-dax.md)
- [ROUND](round-function-dax.md)
- [ROUNDDOWN](rounddown-function-dax.md)
- [ROUNDUP](roundup-function-dax.md)
