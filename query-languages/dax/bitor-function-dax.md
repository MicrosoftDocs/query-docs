---
description: "Learn more about: BITOR"
title: "BITOR function (DAX)"
---
# BITOR

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns a bitwise OR of two numbers.
  
## Syntax  
  
```dax
BITOR(<number>, <number>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`Number`|Any scalar expression that returns number. If not an integer, it is truncated.|
  
## Return value

A bitwise OR of two numbers.
  
## Remarks

- This function supports both positive and negative numbers.

## Example

The following DAX query:

```dax
EVALUATE 
    { BITOR(9, 10) }
```

Returns 11.

## Related content

[BITAND](bitand-function-dax.md)  
[BITXOR](bitxor-function-dax.md)  
[BITLSHIFT](bitlshift-function-dax.md)  
[BITRSHIFT](bitrshift-function-dax.md)  
