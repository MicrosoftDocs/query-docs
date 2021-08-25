---
description: "Learn more about: SELECTEDMEASURE"
title: "SELECTEDMEASURE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# SELECTEDMEASURE

Used by expressions for calculation items to reference the measure that is in context.
  
## Syntax  
  
```dax
SELECTEDMEASURE()
```
  
### Parameters  
  
None  
  
## Return value  

A reference to the measure that is currently in context when the calculation item is evaluated.

## Remarks

- Can only be referenced in the expression for a calculation item.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  

The following calculation item expression calculates the year-to-date for whatever the measure is in context.
  
```dax
CALCULATE(SELECTEDMEASURE(), DATESYTD(DimDate[Date]))
```
  
## See also

[SELECTEDMEASURENAME](selectedmeasurename-function-dax.md)  
[ISSELECTEDMEASURE](isselectedmeasure-function-dax.md)   
