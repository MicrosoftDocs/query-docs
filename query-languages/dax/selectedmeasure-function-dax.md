---
title: "SELECTEDMEASURE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 04/25/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# SELECTEDMEASURENAME

Used by expressions for calculation items to reference the measure that is in context.

> [!NOTE]
> This measure currently applies to [SQL Server 2019 Analysis Services CTP 2.3](https://docs.microsoft.com/sql/sql-server/what-s-new-in-sql-server-ver15?view=sqlallproducts-allversions#calc-ctp24) and later only.
  
## Syntax  
  
```dax
SELECTEDMEASURE() 
```
  
#### Parameters  
  
None  
  
## Return value  

A reference to the measure that is currently in context when the calculation item is evaluated.

## Remarks

Can only be referenced in the expression for a calculation item. 

## Example  

The following calculation item expression calculates the year-to-date for whatever the measure is in context. 
  
```dax
CALCULATE(SELECTEDMEASURE(), DATESYTD(DimDate[Date]))
```
  
## See also  
[SELECTEDSMEASURENAME](selectedmeasurename-function-dax.md)  
[ISSELECTEDSMEASURE](isselectedmeasure-function-dax.md)   
  
