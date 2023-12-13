---
description: "Learn more about: BITAND"
title: "BITAND function (DAX) | Microsoft Docs"
---
# BITAND

Returns a bitwise AND of two numbers.
  
## Syntax  
  
```dax
BITAND(<number>, <number>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|Number|Any scalar expression that returns number. If not an integer, it is truncated.|
  
## Return value

A bitwise AND of two numbers.
  
## Remarks

- This function supports both positive and negative numbers.

## Example

The following DAX query:

```dax
EVALUATE { BITAND(13, 11) }
```

Returns 9.

## Related content

[BITLSHIFT](bitlshift-function-dax.md)  
[BITRSHIFT](bitrshift-function-dax.md)  
[BITOR](bitor-function-dax.md)  
[BITXOR](bitxor-function-dax.md)
