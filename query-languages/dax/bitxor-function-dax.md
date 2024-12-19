---
description: "Learn more about: BITXOR"
title: "BITXOR function (DAX)"
---
# BITXOR

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns a bitwise XOR of two numbers.

## Syntax

```dax
BITXOR(<number>, <number>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`Number`|Any scalar expression that returns number. If not an integer, it is truncated.|

## Return value

A bitwise XOR of two numbers.

## Remarks

- This function supports both positive and negative numbers.

## Example

The following DAX query:

```dax
EVALUATE { BITXOR(9, 10) }
```

Returns 3.

## Related content

[BITOR](bitor-function-dax.md)
[BITAND](bitand-function-dax.md)
[BITLSHIFT](bitlshift-function-dax.md)
[BITRSHIFT](bitrshift-function-dax.md)
