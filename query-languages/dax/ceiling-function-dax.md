---
description: "Learn more about: CEILING"
title: "CEILING function (DAX)"
---
# CEILING

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Rounds a number up, to the nearest integer or to the nearest multiple of significance.  
  
## Syntax  
  
```dax
CEILING(<number>, <significance>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`number`|The number you want to round, or a reference to a column that contains numbers.|  
|`significance`|The multiple of significance to which you want to round. For example, to round to the nearest integer, type 1.|  
  
## Return value

A number rounded as specified.  
  
## Remarks

- There are two CEILING functions in DAX, with the following differences:  
  
  - The CEILING function emulates the behavior of the CEILING function in Excel.  
  - The ISO.CEILING function follows the ISO-defined behavior for determining the ceiling value.  
  
- The two functions return the same value for positive numbers, but different values for negative numbers.  When using a positive multiple of significance, both CEILING and ISO.CEILING round negative numbers upward (toward positive infinity).  When using a negative multiple of significance, CEILING rounds negative numbers downward (toward negative infinity), while ISO.CEILING rounds negative numbers upward (toward positive infinity).  
  
- The return type is usually of the same type of the significant argument, with the following exceptions:  
  
  - If the number argument type is currency, the return type is currency.  
  - If the significance argument type is Boolean, the return type is integer.  
  - If the significance argument type is non-numeric, the return type is real.  
  
## Example 1

The following formula returns 4.45. This might be useful if you want to avoid using smaller units in your pricing. If an existing product is priced at $4.42, you can use CEILING to round prices up to the nearest unit of five cents.  
  
```dax
= CEILING(4.42,0.05)  
```
  
## Example 2

The following formula returns similar results as the previous example, but uses numeric values stored in the column, **ProductPrice**.  
  
```dax
= CEILING([ProductPrice],0.05)  
```
  
## Related content

[Math and Trig functions](math-and-trig-functions-dax.md)  
[FLOOR function](floor-function-dax.md)  
[ISO.CEILING function](iso-ceiling-function-dax.md)  
[ROUNDUP function](roundup-function-dax.md)  
  
