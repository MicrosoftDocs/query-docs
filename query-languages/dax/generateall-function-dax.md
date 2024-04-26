---
description: "Learn more about: GENERATEALL"
title: "GENERATEALL function (DAX) | Microsoft Docs"
---
# GENERATEALL

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns a table with the Cartesian product between each row in *table1* and the table that results from evaluating *table2* in the context of the current row from *table1*.  
  
## Syntax  
  
```dax
GENERATEALL(<table1>, <table2>)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|table1|Any DAX expression that returns a table. |  
|table2|Any DAX expression that returns a table. |  
  
## Return value

A table with the Cartesian product between each row in *table1* and the table that results from evaluating *table2* in the context of the current row from *table1*  
  
## Remarks  
  
- If the evaluation of *table2* for the current row in *table1* returns an empty table, then the current row from *table1* will be included in the results and columns corresponding to *table2* will have null values for that row. This is different than GENERATE() where the current row from *table1* will **not** be included in the results.  
  
- All column names from *table1* and *table2* must be different or an error is returned.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

In the following example, the user wants a summary table of the sales by Region and Product Category for the Resellers channel, like the following table:  
  
|SalesTerritory[SalesTerritoryGroup]|ProductCategory[ProductCategoryName]|[Reseller Sales]|  
|----------------------------------------|-----------------------------------------|---------------------|  
|Europe|Accessories|$        142,227.27|  
|Europe|Bikes|$    9,970,200.44|  
|Europe|Clothing|$        365,847.63|  
|Europe|Components|$    2,214,440.19|  
|NA|Accessories||  
|NA|Bikes||  
|NA|Clothing||  
|NA|Components||  
|North America|Accessories|$        379,305.15|  
|North America|Bikes|$  52,403,796.85|  
|North America|Clothing|$    1,281,193.26|  
|North America|Components|$    8,882,848.05|  
|Pacific|Accessories|$          12,769.57|  
|Pacific|Bikes|$        710,677.75|  
|Pacific|Clothing|$          22,902.38|  
|Pacific|Components|$        108,549.71|  
  
The following formula produces the above table:  
  
```dax
GENERATEALL(  
SUMMARIZE(SalesTerritory, SalesTerritory[SalesTerritoryGroup])  
,SUMMARIZE(ProductCategory
, [ProductCategoryName]  
, "Reseller Sales", SUMX(RELATEDTABLE(ResellerSales_USD), ResellerSales_USD[SalesAmount_USD])  
)  
)  
```
  
1. The first SUMMARIZE produces a table of territory groups, where each row is a territory group, like those listed below:  
  
    |SalesTerritory[SalesTerritoryGroup]|  
    |----------------------------------------|  
    |North America|  
    |Europe|  
    |Pacific|  
    |NA|  
  
2. The second SUMMARIZE produces a table of Product Category groups with the Reseller sales for each group, as shown below:  
  
    |ProductCategory[ProductCategoryName]|[Reseller Sales]|  
    |-----------------------------------------|---------------------|  
    |Bikes|$               63,084,675.04|  
    |Components|$               11,205,837.96|  
    |Clothing|$                 1,669,943.27|  
    |Accessories|$                     534,301.99|  
  
3. However, when you take the above table and evaluate the table under the context of each row from the territory groups table, you obtain different results for each territory.  
