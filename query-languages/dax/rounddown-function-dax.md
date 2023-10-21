---
description: "Learn more about: ROUNDDOWN"
title: "ROUNDDOWN function (DAX) | Microsoft Docs"
---
# ROUNDDOWN

Rounds a number down, toward zero.  
  
## Syntax  
  
```dax
ROUNDDOWN(<number>, <num_digits>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|A real number that you want rounded down.|  
|num_digits|The number of digits to which you want to round. Negative rounds to the left of the decimal point; zero to the nearest integer.|  
  
## Return value

A decimal number.  
  
## Remarks

- If **num_digits** is greater than 0 (zero), then the value in **number** is rounded down to the specified number of decimal places.  
  
- If **num_digits** is 0, then the value in **number** is rounded down to the nearest integer.  
  
- If **num_digits** is less than 0, then the value in **number** is rounded down to the left of the decimal point.  

- ROUNDDOWN behaves like ROUND, except that it always rounds a number down. The INT function also rounds down, but with INT the result is always an integer, whereas with ROUNDDOWN you can control the precision of the result.  
  
## Example 1

The following example rounds 3.14159 down to three decimal places. The expected result is 3.141.  
  
```dax
= ROUNDDOWN(3.14159,3)  
```
  
## Example 2

The following example rounds the value of 31415.92654 down to 2 decimal places to the left of the decimal. The expected result is 31400.  
  
```dax
= ROUNDDOWN(31415.92654, -2)  
```
  
## See also

[Math and Trig functions](math-and-trig-functions-dax.md)  
[ROUND](round-function-dax.md)  
[ROUNDUP](roundup-function-dax.md)  
[ROUNDDOWN](rounddown-function-dax.md)  
[MROUND](mround-function-dax.md)  
[INT](int-function-dax.md)  
