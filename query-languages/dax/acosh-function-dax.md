---
description: "Learn more about: ACOSH"
title: "ACOSH function (DAX)"
---
# ACOSH

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the inverse hyperbolic cosine of a number. The number must be greater than or equal to 1. The inverse hyperbolic cosine is the value whose hyperbolic cosine is `number`, so ACOSH(COSH(number)) equals number.

## Syntax

```dax
ACOSH(number)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`number`|Any real number equal to or greater than 1.|

## Return value

Returns the inverse hyperbolic cosine of a number.

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

|Formula|Description|Result|
|-----------|---------------|----------|
|`= ACOSH(1)`|Inverse hyperbolic cosine of 1.|0|
|`= ACOSH(10)`|Inverse hyperbolic cosine of 10.|2.993228|

