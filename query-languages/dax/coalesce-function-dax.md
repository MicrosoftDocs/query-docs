---
title: "COALESCE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 02/26/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# CONCATENATE

Returns the first expression that does not evaluate to BLANK. If all expressions evaluate to BLANK, BLANK is returned.
  
## Syntax  
  
```dax
COALESCE(<expression>, <expression>[, <expression>]…)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|expression|Any DAX expression that returns a scalar expression.|  
  
## Return value

A scalar value coming from one of the expressions or BLANK if all expressions evaluate to BLANK. 
  
## Remarks

Input expressions may be of different data types.
  
## Example 1
  
  The following DAX query:

```dax
EVALUATE { COALESCE(BLANK(), 10, DATE(2008, 3, 3)) }
```

 Returns `10`, which is the first expression that does not evaluate to BLANK.  

## Example 2
  
  The following DAX expression:

```dax
= COALESCE(SUM(FactInternetSales[SalesAmount]), 0)
```

Returns the sum of all values in the SalesAmount column in the FactInternetSales table, or `0`. 
This can then be used to convert BLANK values of total sales to `0`.  


  
