---
description: "Learn more about: BITAND"
title: "BITAND function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 10/05/2021
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# BITAND

Returns a bitwise 'AND' of two numbers.
  
## Syntax  
  
```dax
BITAND(<number>, <number>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|Number|Any scalar expression that returns number. If not an integer, it is truncated.|
  
## Return value

A bitwise 'AND' of two numbers.
  
## Remarks

- This function supports both positive and negative numbers.
- This function is effectively the same as the & (bitwise AND) operator in C++.

## Example

The following DAX query:

```dax
EVALUATE { BITAND(13, 11) }
```

Returns 9.

## See also

[BITLSHIFT](bitlshift-function-dax.md)  
[BITRSHIFT](bitrshift-function-dax.md)  
[BITOR](bitor-function-dax.md)  
[BITXOR](bitxor-function-dax.md)
