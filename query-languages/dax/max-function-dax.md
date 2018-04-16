---
title: "MAX Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# MAX Function (DAX)
Returns the largest numeric value in a column, or between two scalar expressions.  
  
## Syntax  
  
```  
MAX(<column>)  
```  

```  
MAX(<expression1>, <expression2>)
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**column**|The column in which you want to find the largest numeric value.|  
|**expression**|Any DAX expression which returns a single numeric value.|  
  
## Property Value/Return Value  
A decimal number.  
  
## Remarks  
When evaluating a single column that contains numeric values, if the column contains no numbers, MAX returns a blank. If you want to evaluate values that are not numbers, use the MAXA function.  

When comparing two expressions, blank is treated as 0 when comparing. That is, Max(1, Blank() ) returns 1, and Max( -1, Blank() ) returns 0. If both arguments are blank, MAX returns a blank. If either expression returns a value which is not allowed, MAX returns an error.
  
## Example  
The following example returns the largest value found in the ExtendedAmount column of the InternetSales table.  
  
```  
=MAX(InternetSales[ExtendedAmount])  
```  

## Example  
The following example returns the largest value between the result of two expressions.  
  
```  
=Max([TotalSales], [TotalPurchases])
```  

  
## See Also  
[MAX Function &#40;DAX&#41;](max-function-dax.md)  
[MAXA Function &#40;DAX&#41;](maxa-function-dax.md)  
[MAXX Function &#40;DAX&#41;](maxx-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
