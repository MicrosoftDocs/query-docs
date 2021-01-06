---
title: "TRUE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 01/06/2021
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# TRUE

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
  
```dax
= IF(SUM('InternetSales_USD'[SalesAmount_USD]) >200000, TRUE(), false())  
```

The following table shows the results when the example formula is used in a PivotTable or visualization, with 'ProductCategory'[ProductCategoryName] in Row Labels and 'DateTime'[CalendarYear] in Column Labels.  
  
|Row Labels|2005|2006|2007|2008||Grand Total|
|---------------|-----------------|----|----|----|----|----|  
|Accessories|FALSE|FALSE|TRUE|TRUE|FALSE|TRUE|  
|Bikes|TRUE|TRUE|TRUE|TRUE|FALSE|TRUE|  
|Clothing|FALSE|FALSE|FALSE|FALSE|FALSE|TRUE|  
|Components|FALSE|FALSE|FALSE|FALSE|FALSE|FALSE|  
||FALSE|FALSE|FALSE|FALSE|FALSE|FALSE|  
|Grand Total|TRUE|TRUE|TRUE|TRUE|FALSE|TRUE|  
  
## See also

[FALSE](false-function-dax.md)  
[NOT](not-function-dax.md)  
[IF](if-function-dax.md)  
