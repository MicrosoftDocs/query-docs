---
title: "COT function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 05/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# COT

Returns the cotangent of an angle specified in radians.  
  
## Syntax  
  
```dax
COT (<number>)
```
  
### Parameters
  
|Term|Definition|  
|--------|--------------|  
|number|The angle in radians for which you want the cotangent|  
  
## Return value

The cotangent of the given angle.  
  
## Remarks

The absolute value of number must be less than 2^27.

If number is outside its constraints, COT returns the #NUM! error value.

If number is a non-numeric value, COT returns the #VALUE! error value.

COT(0) returns the #DIV/0! error value.

## Example  
  
The following DAX query,
  
```dax
EVALUATE { COT(30) }
```

Returns

|[Value] |
|---------|
|-0.156119952161659    |
  
