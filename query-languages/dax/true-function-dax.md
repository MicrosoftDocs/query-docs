---
title: "TRUE Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# TRUE Function (DAX)
Returns the logical value TRUE.  
  
## Syntax  
  
```dax
TRUE()  
```
  
## Return value  
Always TRUE.  
  
## Remarks  
The word TRUE is also interpreted as the logical value TRUE.  
  
## Example  
The formula returns the logical value TRUE when the value in the column, 'InternetSales_USD'[SalesAmount_USD], is greater than 200000.  
  
The following table shows the results when the example formula is used in a PivotTable, with 'ProductCategory'[ProductCategoryName] in Row Labels and 'DateTime'[CalendarYear] in Column Labels.  
  
|True-False|Column Labels||||||  
|---------------|-----------------|----|----|----|----|----|  
|Row Labels|2005|2006|2007|2008||Grand Total|  
|Accessories|FALSE|FALSE|TRUE|TRUE|FALSE|TRUE|  
|Bikes|TRUE|TRUE|TRUE|TRUE|FALSE|TRUE|  
|Clothing|FALSE|FALSE|FALSE|FALSE|FALSE|TRUE|  
|Components|FALSE|FALSE|FALSE|FALSE|FALSE|FALSE|  
||FALSE|FALSE|FALSE|FALSE|FALSE|FALSE|  
|Grand Total|TRUE|TRUE|TRUE|TRUE|FALSE|TRUE|  
  
```dax
= IF(SUM('InternetSales_USD'[SalesAmount_USD]) >200000, TRUE(), false())  
```
  
## See Also  
[FALSE Function &#40;DAX&#41;](false-function-dax.md)  
[NOT Function &#40;DAX&#41;](not-function-dax.md)  
[IF Function &#40;DAX&#41;](if-function-dax.md)  
[DAX Function Reference](dax-function-reference.md)  
  
