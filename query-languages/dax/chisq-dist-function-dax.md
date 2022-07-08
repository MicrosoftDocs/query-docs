---
description: "Learn more about: CHISQ.DIST"
title: "CHISQ.DIST function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# CHISQ.DIST

Returns the chi-squared distribution.
  
The chi-squared distribution is commonly used to study variation in the percentage of something across samples, such as the fraction of the day people spend watching television.
  
## Syntax  
  
```dax
CHISQ.DIST(<x>, <deg_freedom>, <cumulative>)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|x|The value at which you want to evaluate the distribution.|  
|Deg_freedom|The number of degrees of freedom.| 
|cumulative|A logical value that determines the form of the function. If cumulative is TRUE, CHISQ.DIST returns the cumulative distribution function; if FALSE, it returns the probability density function.|
  
## Return value

The chi-squared distribution.  
  
## Remarks

- If x or deg_freedom is nonnumeric, an error is returned.
  
- If deg_freedom is not an integer, it is rounded.
  
- If x < 0, an error is returned.

- If deg_freedom < 1 or deg_freedom > 10^10, an error is returned.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
The following DAX query,
  
```dax
EVALUATE { CHISQ.DIST(2, 2, TRUE) }
```

Returns

|[Value] |
|---------|
|0.632120558828558     |
