---
title: "LOOKUPVALUE Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# LOOKUPVALUE Function (DAX)
Returns the value in *result_columnName* for the row that meets all criteria specified by *search_columnName* and *search_value*.  
  
## Syntax  
  
```  
LOOKUPVALUE( <result_columnName>, <search_columnName>, <search_value>[, <search_columnName>, <search_value>]…)  
```  
  
#### Parameters  
result_columnName  
The name of an existing column that contains the value you want to return. The column must be named using standard DAX syntax, usually, fully qualified. It cannot be an expression.  
  
search_columnName  
The name of an existing column, in the same table as result_columnName or in a related table, over which the look-up is performed. The column must be named using standard DAX syntax, usually, fully qualified. It cannot be an expression.  
  
search_value  
A scalar expression that does not refer to any column in the same table being searched.  
  
## Return Value  
The value of *result_column* at the row where all pairs of *search_column* and *search_value* have a match.  
  
If there is no match that satisfies all the search values, a BLANK is returned. In other words, the function will not return a lookup value if only some of the criteria match.  
  
If multiple rows match the search values and in all cases *result_column* values are identical then that value is returned. However, if *result_column* returns different values an error is returned.  
  
## Remarks  
  
## Example  
The following example returns the SafetyStocklLevel for the bike model "Mountain-400-W Silver, 46".  
  
```  
=LOOKUPVALUE(Product[SafetyStockLevel], [ProductName], " Mountain-400-W Silver, 46")  
```  
