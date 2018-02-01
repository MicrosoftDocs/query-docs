---
title: "HASONEVALUE Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.HASONEVALUE.f1"
helpviewer_keywords: 
  - "HASONEVALUE function"
ms.assetid: a1acee60-09a9-4645-9d2b-d63198b4254f
caps.latest.revision: 9
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# HASONEVALUE Function (DAX)
Returns **TRUE** when the context for *columnName* has been filtered down to one distinct value only. Otherwise is **FALSE**.  
  
## Syntax  
  
```html  
HASONEVALUE(<columnName>)  
```  
  
#### Parameters  
columnName  
The name of an existing column, using standard DAX syntax. It cannot be an expression.  
  
## Return Value  
**TRUE** when the context for *columnName* has been filtered down to one distinct value only. Otherwise is **FALSE**.  
  
## Remarks  
  
-   An equivalent expression for HASONEVALUE() is `COUNTROWS(VALUES(<columnName>)) = 1`.  
  
## Example  
In the following example you want to create a formula that verifies if the context is being sliced by one value in order to estimate a percentage against a predefined scenario; in this case you want to compare Reseller Sales against sales in 2007, then you need to know if the context is filtered by single years. Also, if the comparison is meaningless you want to return BLANK.  
  
If you want to follow the scenario, you can download the spreadsheet with the model from [Power Pivot Sample Data](http://powerpivotsampledata.codeplex.com/releases/view/35434) spreadsheet.  
  
Create a measure named [ResellerSales compared to 2007] using the following expression:  
  
```  
=IF(HASONEVALUE(DateTime[CalendarYear]),SUM(ResellerSales_USD[SalesAmount_USD])/CALCULATE(SUM(ResellerSales_USD[SalesAmount_USD]),DateTime[CalendarYear]=2007),BLANK())  
```  
  
1.  After creating the measure you should have an empty result under [ResellerSales compared to 2007]. The BLANK cell in the result is because you don't have single year filters anywhere in your context.  
  
2.  Drag DateTime[CalendarYear] to the **Column Labels** box; your table should look like this:  
  
    ||**Column Labels**||||  
    |-|-|-|-|-|  
    ||**2005**|**2006**|**2007**|**2008**|  
    |**ResellerSales compared to 2007**|**24.83 %**|**74.88 %**|**100.00 %**|**50.73 %**|  
  
3.  Drag ProductCategory[ProductCategoryName] to the **Row Labels** box to have something like this:  
  
    |**ResellerSales compared to 2007**|**Column Labels**||||  
    |-|-|-|-|-|  
    |**Row Labels**|**2005**|**2006**|**2007**|**2008**|  
    |Accessories|6.74 %|31.40 %|100.00 %|55.58 %|  
    |Bikes|28.69 %|77.92 %|100.00 %|53.46 %|  
    |Clothing|3.90 %|55.86 %|100.00 %|44.92 %|  
    |Components|11.05 %|65.99 %|100.00 %|38.65 %|  
    |**Grand Total**|**24.83 %**|**74.88 %**|**100.00 %**|**50.73 %**|  
  
    Did you notice that **Grand Totals** appeared at the bottom of the columns but not for the rows? This is because the context for Grand Totals on rows implies more than one year; but for columns implies a single year.  
  
4.  Drag DateTime[CalendarYear] to the **Horizontal Slicers** box, and drag SalesTerritory[SalesTerritoryGroup] to the **Horizontal Labels** box. You should have an empty results set, because your table contains data for multiple years. Select **2006** in the slicer and your table should now have data again. Try other years to see how the results change.  
  
5.  In summary, HASONEVALUE() allows you to identify if your expression is being evaluated in the context of a single value for *columnName*.  
  
