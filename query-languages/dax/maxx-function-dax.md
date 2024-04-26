---
description: "Learn more about: MAXX"
title: "MAXX function (DAX) | Microsoft Docs"
---
# MAXX

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the highest value that results from evaluating an expression for each row of a table.
  
## Syntax  
  
```dax
MAXX(<table>,<expression>,[<variant>])    
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|The table containing the rows for which the expression will be evaluated.|  
|expression|The expression to be evaluated for each row of the table.|  
|variant|(Optional) If TRUE, and if there are variant or mixed value types, the highest value based on ORDER BY DESC is returned.|
  
## Return value

The highest value.
  
## Remarks

- The **table** argument to the MAXX function can be a table name or an expression that evaluates to a table. The second argument indicates the expression to be evaluated for each row of the table.  
  
- Of the values to evaluate, only the following are counted:  
  - Numbers
  - Texts
  - Dates
  
- Blank values are skipped. TRUE/FALSE values are not supported.

- If the expression has variant or mixed value types such as text and number, then by default MAXX considers only numbers. If `<variant> = TRUE`, the maximum value is returned.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example 1

The following formula uses an expression as the second argument to calculate the total amount of taxes and shipping for each order in the InternetSales table. The expected result is 375.7184.  
  
```dax
= MAXX(InternetSales, InternetSales[TaxAmt]+ InternetSales[Freight])  
```
  
## Example 2

The following formula first filters the InternetSales table by using a FILTER expression to return a subset of orders for a specific sales region defined as, [SalesTerritory] = 5. The MAXX function then evaluates the expression used as the second argument for each row of the filtered table and returns the highest amount for taxes and shipping for just those orders. The expected result is 250.3724.  
  
```dax
= MAXX(FILTER(InternetSales,[SalesTerritoryCode]="5"), InternetSales[TaxAmt]+ InternetSales[Freight])  
```
  
## Related content

[MAX function](max-function-dax.md)  
[MAXA function](maxa-function-dax.md)  
[Statistical functions](statistical-functions-dax.md)  
