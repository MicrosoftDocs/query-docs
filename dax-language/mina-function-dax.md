---
title: "MINA Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
f1_keywords: 
  - "sql13.as.daxref.MINA.f1"
helpviewer_keywords: 
  - "MINA function"
  - "Minimum value, MINA"
ms.assetid: a108ef9d-01ec-42bf-beb6-acad2299046c
caps.latest.revision: 3
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# MINA Function (DAX)
Returns the smallest value in a column, including any logical values and numbers represented as text.  
  
## Syntax  
  
```  
MINA(<column>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**column**|The column for which you want to find the minimum value.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
The MINA function takes as argument a column that contains numbers, and determines the smallest value as follows:  
  
-   If the column contains no numeric values, MINA returns 0 (zero).  
  
-   Rows in the column that evaluates to logical values, such as TRUE and FALSE are treated as 1 if TRUE and 0 (zero) if FALSE.  
  
-   Empty cells are ignored.  
  
If you do not want to include logical values and text as part of the calculation, use the MIN function instead.  
  
## Example  
The following expression returns the minimum freight charge from the table, InternetSales.  
  
```  
=MINA(InternetSales[Freight])  
```  
  
## Example  
The following expression returns the minimum value in the column, PostalCode. Because the data type of the column is text, the function does not find any numeric values, and the formula returns zero (0).  
  
```  
=MINA([PostalCode])  
```  
  
## See Also  
[MIN Function &#40;DAX&#41;](../DAX/min-function-dax.md)  
[MINA Function &#40;DAX&#41;](../DAX/mina-function-dax.md)  
[MINX Function &#40;DAX&#41;](../DAX/minx-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](../DAX/statistical-functions-dax.md)  
  
