---
description: "Learn more about: ADDCOLUMNS"
title: "ADDCOLUMNS function (DAX) | Microsoft Docs"
---
# ADDCOLUMNS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Adds calculated columns to the given table or table expression.  
  
## Syntax  
  
```dax
ADDCOLUMNS(<table>, <name>, <expression>[, <name>, <expression>]…)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|table|Any DAX expression that returns a table of data.| 
|name|The name given to the column, enclosed in double quotes.  |
|expression|Any DAX expression that returns a scalar expression, evaluated for each row of *table*. | 
  
## Return value

A table with all its original columns and the added ones.  

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following example returns an extended version of the Product Category table that includes total sales values from the reseller channel and the internet sales.  
  
```dax
ADDCOLUMNS(ProductCategory
               , "Internet Sales", SUMX(RELATEDTABLE(InternetSales_USD), InternetSales_USD[SalesAmount_USD])  
               , "Reseller Sales", SUMX(RELATEDTABLE(ResellerSales_USD), ResellerSales_USD[SalesAmount_USD]))  
```

The following table shows a preview of the data as it would be received by any function expecting to receive a table:  

|ProductCategory[ProductCategoryName]|ProductCategory[ProductCategoryAlternateKey]|ProductCategory[ProductCategoryKey]|[Internet Sales]|[Reseller Sales]|  
|-----|-----|-----|-----|-----|  
|Bikes|1|1|25107749.77|63084675.04|  
|Components|2|2||11205837.96|  
|Clothing|3|3|306157.5829|1669943.267|  
|Accessories|4|4|640920.1338|534301.9888|  
