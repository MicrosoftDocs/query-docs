---
description: "Learn more about: LCM"
title: "LCM function (DAX) | Microsoft Docs"
---
# LCM

Returns the least common multiple of integers. The least common multiple is the smallest positive integer that is a multiple of all integer arguments number1, number2, and so on. Use LCM to add fractions with different denominators.  
  
## Syntax  
  
```dax
LCM(number1, [number2], ...)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number1, number2,...|Number1 is required, subsequent numbers are optional. 1 to 255 values for which you want the least common multiple. If value is not an integer, it is truncated.|  
  
## Return value

Returns the least common multiple of integers.  
  
## Remarks

- If any argument is nonnumeric, LCM returns the #VALUE! error value.  
  
- If any argument is less than zero, LCM returns the #NUM! error value.  
  
- If LCM(a,b) &gt;=2^53, LCM returns the #NUM! error value.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|= LCM(5, 2)|Least common multiple of 5 and 2.|10|  
|= LCM(24, 36)|Least common multiple of 24 and 36.|72|  
