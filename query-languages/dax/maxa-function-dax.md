---
title: "MAXA Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# MAXA Function (DAX)
Returns the largest value in a column. Logical values and blanks are counted.  
  
## Syntax  
  
```  
MAXA(<column>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**column**|The column in which you want to find the largest value.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
The MAXA function takes as argument a column, and looks for the largest value among the following types of values:  
  
-   Numbers  
  
-   Dates  
  
-   Logical values, such as TRUE and FALSE. Rows that evaluate to TRUE count as 1; rows that evaluate to FALSE count as 0 (zero).  
  
Empty cells are ignored. If the column contains no values that can be used, MAXA returns 0 (zero).  
  
If you do not want to include logical values and blanks as part of the calculation, use the MAX function.  
  
## Example  
The following example returns the greatest value from a calculated column, named **ResellerMargin**, that computes the difference between list price and reseller price.  
  
```  
=MAXA([ResellerMargin])  
```  
  
## Example  
The following example returns the largest value from a column that contains dates and times. Therefore, this formula gets the most recent transaction date.  
  
```  
=MAXA([TransactionDate])  
```  
  
## See Also  
[MAX Function &#40;DAX&#41;](max-function-dax.md)  
[MAXA Function &#40;DAX&#41;](maxa-function-dax.md)  
[MAXX Function &#40;DAX&#41;](maxx-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
