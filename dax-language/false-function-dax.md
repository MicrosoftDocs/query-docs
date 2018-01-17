---
title: "FALSE Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.FALSE.f1"
helpviewer_keywords: 
  - "FALSE function"
  - "logical values"
ms.assetid: d59276d3-89b2-4a3a-8737-3c12d97dbf96
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
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
[TRUE Function &#40;DAX&#41;](../DAX/true-function-dax.md)  
[NOT Function &#40;DAX&#41;](../DAX/not-function-dax.md)  
[IF Function &#40;DAX&#41;](../DAX/if-function-dax.md)  
[DAX Function Reference](../DAX/dax-function-reference.md)  
  
