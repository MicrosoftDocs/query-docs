---
title: "FALSE Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# FALSE Function (DAX)
Returns the logical value FALSE.  
  
## Syntax  
  
```  
FALSE()  
```  
  
## Return Value  
Always FALSE.  
  
## Remarks  
The word FALSE is also interpreted as the logical value FALSE.  
  
## Example  
The formula returns the logical value FALSE when the value in the column, 'InternetSales_USD'[SalesAmount_USD], is less than or equal to 200000.  
  
The following table shows the results when the example formula is used with 'ProductCategory'[ProductCategoryName] in Row Labels and 'DateTime'[CalendarYear] in Column Labels.  
  
|True-False|Column Labels||||||  
|---------------|-----------------|----|----|----|----|----|  
|Row Labels|2005|2006|2007|2008||Grand Total|  
|Accessories|FALSE|FALSE|TRUE|TRUE|FALSE|TRUE|  
|Bikes|TRUE|TRUE|TRUE|TRUE|FALSE|TRUE|  
|Clothing|FALSE|FALSE|FALSE|FALSE|FALSE|TRUE|  
|Components|FALSE|FALSE|FALSE|FALSE|FALSE|FALSE|  
||FALSE|FALSE|FALSE|FALSE|FALSE|FALSE|  
|Grand Total|TRUE|TRUE|TRUE|TRUE|FALSE|TRUE|  
  
```  
=IF(SUM('InternetSales_USD'[SalesAmount_USD]) >200000, TRUE(), false())  
```  
  
## See Also  
[TRUE Function &#40;DAX&#41;](true-function-dax.md)  
[NOT Function &#40;DAX&#41;](not-function-dax.md)  
[IF Function &#40;DAX&#41;](if-function-dax.md)  
[DAX Function Reference](dax-function-reference.md)  
  
