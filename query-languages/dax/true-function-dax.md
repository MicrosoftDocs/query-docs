---
description: "Learn more about: TRUE"
title: "TRUE function (DAX)"
---
# TRUE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the logical value `TRUE`.
  
## Syntax  
  
```dax
TRUE()  
```
  
## Return value

Always `TRUE`.
  
## Remarks

The word `TRUE` is also interpreted as the logical value `TRUE`.  
  
## Example

The formula returns the logical value `TRUE` when the value in the column, 'InternetSales_USD'[SalesAmount_USD], is greater than 200000.  
  
```dax
= IF(SUM('InternetSales_USD'[SalesAmount_USD]) >200000, TRUE(), false())  
```

The following table shows the results when the example formula is used in a report with 'ProductCategory'[ProductCategoryName] in Row Labels and 'DateTime'[CalendarYear] in Column Labels.  
  
|Row Labels|2005|2006|2007|2008|-|Grand Total|
|---------------|-----------------|----|----|----|----|----|  
|Accessories|`FALSE`|`FALSE`|`TRUE`|`TRUE`|`FALSE`|`TRUE`|  
|Bikes|`TRUE`|`TRUE`|`TRUE`|`TRUE`|`FALSE`|`TRUE`|  
|Clothing|`FALSE`|`FALSE`|`FALSE`|`FALSE`|`FALSE`|`TRUE`|  
|Components|`FALSE`|`FALSE`|`FALSE`|`FALSE`|`FALSE`|`FALSE`|  
||`FALSE`|`FALSE`|`FALSE`|`FALSE`|`FALSE`|`FALSE`|  
|Grand Total|`TRUE`|`TRUE`|`TRUE`|`TRUE`|`FALSE`|`TRUE`|  
  
## Related content

[FALSE](false-function-dax.md)  
[NOT](not-function-dax.md)  
[IF](if-function-dax.md)  
