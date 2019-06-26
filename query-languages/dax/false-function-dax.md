---
title: "FALSE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/26/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# FALSE
Returns the logical value FALSE.  
  
## Syntax  
  
```dax
FALSE()  
```
  
## Return value  
Always FALSE.  
  
## Remarks  
The word FALSE is also interpreted as the logical value FALSE.  
  
## Example  
The formula returns the logical value FALSE when the value in the column, 'InternetSales_USD'[SalesAmount_USD], is less than or equal to 200000.  
  
```dax
=IF(SUM('InternetSales_USD'[SalesAmount_USD]) >200000, TRUE(), false())  
```

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
  

  
## See also  
[TRUE function &#40;DAX&#41;](true-function-dax.md)  
[NOT function &#40;DAX&#41;](not-function-dax.md)  
[IF function &#40;DAX&#41;](if-function-dax.md)  
[DAX function reference](dax-function-reference.md)  
  
