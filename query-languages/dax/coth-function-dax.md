---
title: "COTH function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# COTH

Returns the hyperbolic cotangent of a hyperbolic angle.
  
## Syntax  
  
```dax
COTH (<number>)
```
  
### Parameters
  
|Term|Definition|  
|--------|--------------|  
|number|The hyperbolic angle in radians for which you want the hyperbolic cotangent.|  
  
## Return value

The hyperbolic cotangent of the given angle.  
  
## Remarks

The hyperbolic cotangent is an analog of the ordinary (circular) cotangent.

The absolute value of number must be less than 2^27.

If number is outside its constraints, COTH returns the #NUM! error value.

If number is a non-numeric value, COTH returns the #VALUE! error value.

COTH(0) returns the #DIV/0! error value.

The following equation is used:  
:::image type="content" source="media/dax-coth-formula.png" alt-text="COTH formula":::

## Example  
  
The following DAX query,
  
```dax
EVALUATE { COTH(2) }
```

Returns

|[Value] |
|---------|
|1.03731472072755   |
  