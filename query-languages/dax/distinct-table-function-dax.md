---
title: "DISTINCT (table) Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DISTINCT (table) Function

Returns a table by removing duplicate rows from another table or expression.
  
## Syntax  
  
```dax
DISTINCT(<table>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|The table from which unique rows are to be returned. The table can also be an expression that results in a table.|  
  
## Return value  
A table containing only distinct rows.  
  
## Related functions  
There is another version of the DISTINCT function, [DISTINCT (column)](distinct-function-dax.md), that takes a column name as input parameter.
  
## Example  

The following query:
```dax
EVALUATE DISTINCT( { (1, "A"), (2, "B"), (1, "A") } )
```

Returns table:

|[Value1]    |[Value2]  |
|---------|---------|
|1    |     A    |
|2    |     B    |


  
## See Also  
[Filter Functions &#40;DAX&#41;](filter-functions-dax.md)  
[DISTINCT (column) &#40;DAX&#41;](distinct-function-dax.md)   
[FILTER Function &#40;DAX&#41;](filter-function-dax.md)  
[RELATED Function &#40;DAX&#41;](related-function-dax.md)  
[VALUES Function &#40;DAX&#41;](values-function-dax.md)  
  
