---
description: "Learn more about: EVEN"
title: "EVEN function (DAX) | Microsoft Docs"
---
# EVEN

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns number rounded up to the nearest even integer. You can use this function for processing items that come in twos. For example, a packing crate accepts rows of one or two items. The crate is full when the number of items, rounded up to the nearest two, matches the crate's capacity.  
  
## Syntax  
  
```dax
EVEN(number)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`number`|The value to round.|  
  
## Return value

Returns number rounded up to the nearest even integer.  
  
## Remarks

- If `number` is nonnumeric, EVEN returns the #VALUE! error value.  
  
- Regardless of the sign of number, a value is rounded up when adjusted away from zero. If number is an even integer, no rounding occurs.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|`= EVEN(1.5)`|Rounds 1.5 to the nearest even integer|2|  
|`= EVEN(3)`|Rounds 3 to the nearest even integer|4|  
|`= EVEN(2)`|Rounds 2 to the nearest even integer|2|  
|`= EVEN(-1)`|Rounds -1 to the nearest even integer|-2|  
