---
description: "Learn more about: COT"
title: "COT function (DAX) | Microsoft Docs"
---
# COT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the cotangent of an angle specified in radians.  
  
## Syntax  
  
```dax
COT (<number>)
```
  
### Parameters
  
|Term|Definition|  
|--------|--------------|  
|number|The angle in radians for which you want the cotangent.|  
  
## Return value

The cotangent of the given angle.  
  
## Remarks

- The absolute value of number must be less than 2^27 and cannot be 0.

- If number is outside its constraints, an error is returned.

- If number is a non-numeric value, an error is returned.

## Example  
  
The following DAX query,
  
```dax
EVALUATE { COT(30) }
```

Returns

|[Value] |
|---------|
|-0.156119952161659    |
