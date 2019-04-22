---
title: "COUNT function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 04/19/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# COUNT

The COUNT function counts the number of cells in a column that contain non-blank values.  
  
## Syntax  
  
```dax
COUNT(<column>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|The column that contains the values to be counted.|  
  
## Return value

A whole number.  
  
## Remarks

The only argument allowed to this function is a column. The COUNT function counts rows that contain the following kinds of values:  
  
- Numbers  
  
- Dates  

- Strings
  
When the function finds no rows to count, it returns a blank.

Blank values are skipped. TRUE/FALSE values are not supported.

If you want to evaluate a column of TRUE/FALSE values, use the COUNTA function.

## Example

The following example shows how to count the number of values in the column, ShipDate.  
  
```dax
=COUNT([ShipDate])  
```

To count logical values or text, use the COUNTA or COUNTAX functions.  
  
## See also  

[COUNTA function &#40;DAX&#41;](counta-function-dax.md)  
[COUNTAX function &#40;DAX&#41;](countax-function-dax.md)  
[COUNTX function &#40;DAX&#41;](countx-function-dax.md)  
[Statistical functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
