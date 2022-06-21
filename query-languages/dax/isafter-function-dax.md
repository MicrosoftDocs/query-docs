---
description: "Learn more about: ISAFTER"
title: "ISAFTER function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 08/31/2021
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# ISAFTER
  
A boolean function that emulates the behavior of a 'Start At' clause and returns true for a row that meets all of the condition parameters.  
  
Based on the sort order, the first parameter is compared with the second parameter. If the sort order is ascending, the comparison to be done is first parameter greater than the second parameter. If the sort order is descending, the comparison to be done is second parameter less than the first parameter.  
  
## Syntax  
  
```DAX  
ISAFTER(<scalar_expression>, <scalar_expression>[, sort_order [, <scalar_expression>, <scalar_expression>[, sort_order]]…)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|scalar expression|Any expression that returns a scalar value like a column reference or integer or string value. Typically the first parameter is a column reference and the second parameter is a scalar value.|  
|sort order|(optional) The order in which the column is sorted. Can be ascending (ASC) or descending (DEC). By default the sort order is ascending.|  
  
## Return value

True or false.  

## Remarks

This function is similar to [ISONORAFTER](isonorafter-function-dax.md). The difference is ISAFTER returns true for values sorted strictly *after* the filter values, where ISONORAFTER returns true for values sorted *on or after* the filter values.

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

Table name: 'Info'  
  
|Country|State|Count|Total|  
|-----------|---------|---------|---------|  
|IND|JK|20|800|  
|IND|MH|25|1000|  
|IND|WB|10|900|  
|USA|CA|5|500|  
|USA|WA|10|900|  

The following expression:

```dax
FILTER (
    Info,
    ISAFTER (
        Info[Country], "IND", ASC,
        Info[State], "MH", ASC )
)
```

Returns:

|Country|State|Count|Total|  
|-----------|---------|---------|---------|  
|IND|WB|10|900|  
|USA|CA|5|500|  
|USA|WA|10|900|  

## See also

[ISONORAFTER](isonorafter-function-dax.md)