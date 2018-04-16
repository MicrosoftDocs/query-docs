---
title: "CALCULATE Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: Minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# CALCULATE Function (DAX)
Evaluates an expression in a context that is modified by the specified filters.  
  
## Syntax  
  
```  
CALCULATE(<expression>,<filter1>,<filter2>…)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**expression**|The expression to be evaluated.|  
|**filter1***,***filter2***,…*|(optional) A comma separated list of Boolean expression or a table expression that defines a filter.|  
  
The expression used as the first parameter is essentially the same as a measure.  
  
The following restrictions apply to Boolean expressions that are used as arguments:  
  
-   The expression cannot reference a measure.  
  
-   The expression cannot use a nested CALCULATE function.  
  
-   The expression cannot use any function that scans a table or returns a table, including aggregation functions.  
  
However, a Boolean expression can use any function that looks up a single value, or that calculate a scalar value.  
  
## Return Value  
The value that is the result of the expression.  
  
## Remarks  
If the data has been filtered, the CALCULATE function changes the context in which the data is filtered, and evaluates the expression in the new context that you specify. For each column used in a filter argument, any existing filters on that column are removed, and the filter used in the filter argument is applied instead.  
  
## Example  
To calculate the ratio of current reseller sales to all reseller sales, you add to the PivotTable a measure that calculates the sum of sales for the current cell (the numerator), and then divides that sum by the total sales for all resellers (the denominator). To ensure that the denominator remains the same regardless of how the PivotTable might be filtering or grouping the data, the part of the formula that represents the denominator must use the ALL function to clear any filters and create the correct total.  
  
The following table shows the results when the new measure, named **All Reseller Sales Ratio**, is created by using the formula in the code section.  
  
To see how this works, add the field, CalendarYear, to the **Row Labels** area of the PivotTable, and add the field, ProductCategoryName, to the **Column Labels** area. Then add the new measure to the **Values** area of the PivotTable. To display the numbers as percentages, apply percentage number formatting to the area of the PivotTable that contains the new measure, **All Reseller Sales Ratio**.  
  
|All Reseller Sales|Column Labels|||||  
|----------------------|-----------------|----|----|----|----|  
|Row Labels|Accessories|Bikes|Clothing|Components|Grand Total|  
|2005|0.02%|9.10%|0.04%|0.75%|9.91%|  
|2006|0.11%|24.71%|0.60%|4.48%|29.90%|  
|2007|0.36%|31.71%|1.07%|6.79%|39.93%|  
|2008|0.20%|16.95%|0.48%|2.63%|20.26%|  
|Grand Total|0.70%|82.47%|2.18%|14.65%|100.00%|  
  
```  
=( SUM('ResellerSales_USD'[SalesAmount_USD]))  
 /CALCULATE( SUM('ResellerSales_USD'[SalesAmount_USD])  
           ,ALL('ResellerSales_USD'))  
```  
The CALCULATE expression in the denominator enables the sum expression to include all rows in the calculation. This overrides the implicit filters for CalendarYear and ProductCategoryName that exist for the numerator part of the expression.  
  
## Related Functions  
Whereas the CALCULATE function requires as its first argument an expression that returns a single value, the CALCULATETABLE function takes a table of values.  
  
## See Also  
[CALCULATETABLE Function &#40;DAX&#41;](calculatetable-function-dax.md)  
[Filter Functions &#40;DAX&#41;](filter-functions-dax.md)  
  
