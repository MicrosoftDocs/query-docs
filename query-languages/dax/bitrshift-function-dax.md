---
description: "Learn more about: BITRSHIFT"
title: "BITRSHIFT function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 10/05/2021
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# BITRSHIFT

Returns a number shifted right by the specified number of bits.  
  
## Syntax  
  
```dax
BITRSHIFT(<Number>, <Shift_Amount>) 
```

### Parameters

|Term|Definition|
|--------|--------------|
|Number|Any DAX expression that returns an integer expression.|
|Shift_Amount|Any DAX expression that returns an integer expression.|
  
## Return value

An integer value.
  
## Remarks

- Be sure to understand the nature of bitshift operations and overflow/underflow of integers before using DAX bitshift functions.
- If Shift_Amount is negative, it will shift in the opposite direction.
- If absolute value of Shift_Amount is larger than 64, there will be no error but will result in overflow/underflow.
- There’s no limit on Number, but the result may overflow/underflow.
- This function is effectively the same as the >> (right shift) operator in C++.
  
## Examples

### Example 1

The following DAX query:

```dax
EVALUATE 
    { BITRSHIFT(16, 3) }
```

Returns 2.

This is effectively equivalent to `EVALUATE { BITLSHIFT(16, -3) }`.

### Example 2

The following DAX query:

```dax
EVALUATE 
    { BITRSHIFT(16, 123) }
```

Returns 0.

### Example 3

The following DAX query:

```dax
EVALUATE 
    { BITRSHIFT(-16, 123) }
```

Returns -1.

This aligns with 2’s complement binary operations. Because the first bit of a negative number of a signed integer is 1, and shift-right makes all the bits 1, -1 is returned.

### Example 4

The following DAX query:

```dax
Define 
Measure FACTA[RightShift] = BITRSHIFT(SELECTEDVALUE(Sales[Amount]), 3)

EVALUATE 
SUMMARIZECOLUMNS(
    FACTA[I2],
    "RIGHTSHIFT", 
    [RightShift]
)
```

Shifts right each sales amount with 3 bits and returns the bit-shifted sales amount.

## See also

[BITLSHIFT](bitlshift-function-dax.md)  
[BITAND](bitand-function-dax.md)  
[BITOR](bitor-function-dax.md)  
[BITXOR](bitxor-function-dax.md)
