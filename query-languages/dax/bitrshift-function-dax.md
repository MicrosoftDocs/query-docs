---
description: "Learn more about: BITRSHIFT"
title: "BITRSHIFT function (DAX) | Microsoft Docs"
---
# BITRSHIFT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns a number shifted right by the specified number of bits.  
  
## Syntax  
  
```dax
BITRSHIFT(<Number>, <Shift_Amount>) 
```

### Parameters

|Term|Definition|
|--------|--------------|
|`Number`|Any DAX expression that returns an integer expression.|
|`Shift_Amount`|Any DAX expression that returns an integer expression.|
  
## Return value

An integer value.
  
## Remarks

- Be sure to understand the nature of bitshift operations and overflow/underflow of integers before using DAX bitshift functions.
- If Shift_Amount is negative, it will shift in the opposite direction.
- If absolute value of Shift_Amount is larger than 64, there will be no error but will result in overflow/underflow.
- There’s no limit on Number, but the result may overflow/underflow.
  
## Examples

### Example 1

The following DAX query:

```dax
EVALUATE 
    { BITRSHIFT(16, 3) }
```

Returns 2.

### Example 2

The following DAX query:

```dax
EVALUATE 
    { BITRSHIFT(1024, -3) }
```

Returns 8192.

### Example 3

The following DAX query:

```dax
Define 
    Measure Sales[RightShift] = BITRSHIFT(SELECTEDVALUE(Sales[Amount]), 3)

EVALUATE 
SUMMARIZECOLUMNS(
    Sales[Amount],
    "RIGHTSHIFT", 
    [RightShift]
)
```

Shifts right each sales amount with 3 bits and returns the bit-shifted sales amount.

## Related content

[BITLSHIFT](bitlshift-function-dax.md)  
[BITAND](bitand-function-dax.md)  
[BITOR](bitor-function-dax.md)  
[BITXOR](bitxor-function-dax.md)
