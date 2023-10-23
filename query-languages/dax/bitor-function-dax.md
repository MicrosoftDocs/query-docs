---
description: "Learn more about: BITOR"
title: "BITOR function (DAX) | Microsoft Docs"
---
# BITOR

Returns a bitwise OR of two numbers.
  
## Syntax  
  
```dax
BITOR(<number>, <number>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|Number|Any scalar expression that returns number. If not an integer, it is truncated.|
  
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

## See also

[BITAND](bitand-function-dax.md)  
[BITXOR](bitxor-function-dax.md)  
[BITLSHIFT](bitlshift-function-dax.md)  
[BITRSHIFT](bitrshift-function-dax.md)  
