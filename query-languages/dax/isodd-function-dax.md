---
description: "Learn more about: ISODD"
title: "ISODD function (DAX)"
---
# ISODD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns `TRUE` if number is odd, or `FALSE` if number is even.  
  
## Syntax  
  
```dax
ISODD(number)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`number`|The value to test. If number is not an integer, it is truncated.|  
  
## Return value

Returns `TRUE` if number is odd, or `FALSE` if number is even.  
  
## Remarks

- If number is nonnumeric, ISODD returns the `#VALUE!` error value.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
