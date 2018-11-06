---
title: "RELATEDTABLE Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# RELATEDTABLE Function (DAX)
Evaluates a table expression in a context modified by the given filters.  
  
## Syntax  
  
```dax
RELATEDTABLE(<tableName>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**tableName**|The name of an existing table using standard DAX syntax. It cannot be an expression.|  
  
## Return Value  
A table of values.  
  
## Remarks  
The RELATEDTETABLE function changes the context in which the data is filtered, and evaluates the expression in the new context that you specify.  
  
This function is a shortcut for CALCULATETABLE function with no logical expression.  
  
## Example  
The following example uses the RELATEDTABLE function to create a calculated column with the Internet Sales in the Product Category table.  
  
The following table shows the results of using the code shown here.  
  
|||||  
|-|-|-|-|  
|Product Category Key|Product Category AlternateKey|Product Category Name|Internet Sales|  
|1|1|Bikes|$28,318,144.65|  
|2|2|Components||  
|3|3|Clothing|$339,772.61|  
|4|4|Accessories|$700,759.96|  
  
```dax
= SUMX( RELATEDTABLE('InternetSales_USD')  
     , [SalesAmount_USD])  
```
  
## See Also  
[CALCULATETABLE Function &#40;DAX&#41;](calculatetable-function-dax.md)  
[Filter Functions &#40;DAX&#41;](filter-functions-dax.md)  
  
