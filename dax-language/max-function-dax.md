---
title: "MAX Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.MAX.f1"
helpviewer_keywords: 
  - "MAX function"
  - "Maximum value, MAX"
ms.assetid: 0f96a534-31c7-4564-ac36-62bc991248d5
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
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
[MAX Function &#40;DAX&#41;](../DAX/max-function-dax.md)  
[MAXA Function &#40;DAX&#41;](../DAX/maxa-function-dax.md)  
[MAXX Function &#40;DAX&#41;](../DAX/maxx-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](../DAX/statistical-functions-dax.md)  
  
