---
description: "Learn more about: DETAILROWS"
title: "DETAILROWS function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 08/26/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# DETAILROWS

Evaluates a Detail Rows Expression defined for a measure and returns the data.

## Syntax  
  
```dax
DETAILROWS([Measure])  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Measure|Name of a measure.|  
  
## Return value

A table with the data returned by the Detail Rows Expression. If no Detail Rows Expression is defined, the data for the table containing the measure is returned.
