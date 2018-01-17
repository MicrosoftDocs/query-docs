---
title: "MIN Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.MIN.f1"
helpviewer_keywords: 
  - "MIN function"
  - "Minimum value, MIN"
ms.assetid: c5172068-216e-4e3b-b5f2-7384c091bdbc
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# MIN Function (DAX)
Returns the smallest numeric value in a column, or between two scalar expressions. Ignores logical values and text.  
  
## Syntax  
  
```  
MIN(<column>)  
```  

```  
MIN(<expression1>, <expression2>)
```  

#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**column**|The column in which you want to find the smallest numeric value.|  
|**expression**|Any DAX expression which returns a single numeric value.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
The MIN function takes a column or two expressions as an argument, and returns the smallest numeric value. The following types of values in the columns are counted:  
  
-   Numbers  
  
-   Dates  

-   Blanks
  
-   If the column contains no numerical data, MIN returns blanks.  
  
When evaluating a column, empty cells, logical values, and text are ignored. If you want to include logical values and text representations of numbers in a reference as part of the calculation, use the MINA function.  

When comparing expressions, blank is treated as 0 when comparing. That is, Min(1,Blank() ) returns 0, and Min( -1, Blank() ) returns -1. If both arguments are blank, MIN returns a blank. If either expression returns a value which is not allowed, MIN returns an error.
  
## Example  
The following example returns the smallest value from the calculated column, ResellerMargin.  
  
```  
=MIN([ResellerMargin])  
```  
  
## Example  
The following example returns the smallest value from a column that contains dates and times, TransactionDate. This formula therefore returns the date that is earliest.  
  
```  
=MIN([TransactionDate])  
```  

## Example  
The following example returns the smallest value from the result of two scalar expressions.  
  
```  
=Min([TotalSales], [TotalPurchases]) 
```  

  
## See Also  
[MIN Function &#40;DAX&#41;](../DAX/min-function-dax.md)  
[MINA Function &#40;DAX&#41;](../DAX/mina-function-dax.md)  
[MINX Function &#40;DAX&#41;](../DAX/minx-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](../DAX/statistical-functions-dax.md)  
  
