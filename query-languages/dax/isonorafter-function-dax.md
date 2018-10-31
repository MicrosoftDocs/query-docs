---
title: "ISONORAFTER Function (DAX) | Microsoft Docs"
ms.prod: powerbi 
ms.technology: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ISONORAFTER Function (DAX)
  
A boolean function that emulates the behavior of a ‘Start At’ clause and returns true for a row that meets all of the condition parameters.  
  
This function takes a variable number of triples, the first two values in a triple are the expressions to be compared, and the third parameter indicates the sort order. The sort order can be ascending (default) or descending.  
  
Based on the sort order, the first parameter is compared with the second parameter. If the sort order is ascending, the comparison to be done is first parameter greater than or equal to second parameter. If the sort order is descending, the comparison to be done is second parameter less than or equal to first parameter.  
  
## Syntax  
  
```vb  
ISONORAFTER(<scalar_expression>, <scalar_expression>sort_order] [,scalar_expression>, <scalar_expression>, [sort_order][,…])  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|scalar expression|Any expression that returns a scalar value like a column reference or integer or string value. Typically the first parameter is a column reference and the second parameter is a scalar value.|  
|sort order|(optional) The order in which the column is sorted. Can be ascending (ASC) or descending (DEC). By default the sort order is ascending.|  
  
## Return Value  
True or false.  
  
## Example  
Table name: ‘Info’  
  
|Country|State|Count|Total|  
|-----------|---------|---------|---------|  
|IND|JK|20|800|  
|IND`|MH|25|1000|  
|IND|WB|10|900|  
|USA|CA|5|500|  
|USA|WA|10|900|  
  
```dax
FILTER(Info, ISONORAFTER(Info[Country], “IND”, ASC, Info[State], “MH”, ASC))  
```
