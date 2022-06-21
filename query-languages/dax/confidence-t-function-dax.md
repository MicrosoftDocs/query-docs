---
description: "Learn more about: CONFIDENCE.T"
title: "CONFIDENCE.T function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# CONFIDENCE.T

Returns the confidence interval for a population mean, using a Student's t distribution.  
  
## Syntax  
  
```dax
CONFIDENCE.T(alpha,standard_dev,size)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|alpha|The significance level used to compute the confidence level. The confidence level equals 100*(1 - alpha)%, or in other words, an alpha of 0.05 indicates a 95 percent confidence level.|  
|standard_dev|The population standard deviation for the data range and is assumed to be known.|  
|size|The sample size.|  
  
## Return value

Returns the confidence interval for a population mean, using a Student's t distribution.  
  
## Remarks

- If any argument is nonnumeric, CONFIDENCE.T returns the #VALUE! error value.  
  
- If alpha ≤ 0 or alpha ≥ 1, CONFIDENCE.T returns the #NUM! error value.  
  
- If standard_dev ≤ 0, CONFIDENCE.T returns the #NUM! error value.  
  
- If size is not an integer, it is rounded.  
  
- If size equals 1, CONFIDENCE.T returns #DIV/0! error value.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|= CONFIDENCE.T(0.05,1,50)|Confidence interval for the mean of a population based on a sample size of 50, with a 5% significance level and a standard deviation of 1. This is based on a Student's t-distribution.|0.284196855|  
