---
description: "Learn more about: ISEVEN"
title: "ISEVEN function (DAX) | Microsoft Docs"
---
# ISEVEN

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns `TRUE` if number is even, or `FALSE` if number is odd.  
  
## Syntax  
  
```dax
ISEVEN(number)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`number`|The value to test. If number is not an integer, it is truncated.|  
  
## Return value

Returns `TRUE` if number is even, or `FALSE` if number is odd.  
  
## Remarks

- If number is nonnumeric, ISEVEN returns the `#VALUE!` error value.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
