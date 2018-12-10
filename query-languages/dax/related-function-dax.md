---
title: "RELATED function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# RELATED
Returns a related value from another table.  
  
## Syntax  
  
```dax
RELATED(<column>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|The column that contains the values you want to retrieve.|  
  
## Return value  
A single value that is related to the current row.  
  
## Remarks  
The RELATED function requires that a relationship exists between the current table and the table with related information. You specify the column that contains the data that you want, and the function follows an existing many-to-one relationship to fetch the value from the specified column in the related table. If a relationship does not exist, you must create a relationship.  
  
When the RELATED function performs a lookup, it examines all values in the specified table regardless of any filters that may have been applied.  
  
> [!NOTE]  
> The RELATED function needs a row context; therefore, it can only be used in calculated column expression, where the current row context is unambiguous, or as a nested function in an expression that uses a table scanning function. A table scanning function, such as SUMX, gets the value of the current row value and then scans another table for instances of that value.  
  
## Example  
In the following example, the measure Non USA Internet Sales is created to produce a sales report that excludes sales in the United States. In order to create the measure, the InternetSales_USD table must be filtered to exclude all sales that belong to the United States in the SalesTerritory table. The United States, as a country, appears 5 times in the SalesTerritory table; once for each of the following regions: Northwest, Northeast, Central, Southwest, and Southeast.  
  
The first approach to filter the Internet Sales, in order to create the measure, could be to add a filter expression like the following:  
  
`FILTER('InternetSales_USD', 'InternetSales_USD'[SalesTerritoryKey]<>1 && 'InternetSales_USD'[SalesTerritoryKey]<>2 && 'InternetSales_USD'[SalesTerritoryKey]<>3 && 'InternetSales_USD'[SalesTerritoryKey]<>4 && 'InternetSales_USD'[SalesTerritoryKey]<>5)`  
  
However, this approach is counterintuitive, prone to typing errors, and might not work if any of the existing regions is split in the future.  
  
A better approach would be to use the existing relationship between InternetSales_USD and SalesTerritory and explicitly state that the country must be different from the United States. To do so, create a filter expression like the following:  
  
`FILTER( 'InternetSales_USD', RELATED('SalesTerritory'[SalesTerritoryCountry])<>"United States")`  
  
This expression uses the RELATED function to lookup the country value in the SalesTerritory table, starting with the value of the key column, SalesTerritoryKey, in the InternetSales_USD table. The result of the lookup is used by the filter function to determine if the InternetSales_USD row is filtered or not.  
  
> [!NOTE]  
> If the example does not work, you might need to create a relationship between the tables.  
  
```dax
= SUMX(FILTER( 'InternetSales_USD'  
            ,  RELATED('SalesTerritory'[SalesTerritoryCountry])  
               <>"United States"  
             )  
     ,'InternetSales_USD'[SalesAmount_USD])  
```

The following table shows only totals for each region, to prove that the filter expression in the measure, Non USA Internet Sales, works as intended.  
  
|Row Labels|Internet Sales|Non USA Internet Sales|  
|--------------|------------------|--------------------------|  
|Australia|$4,999,021.84|$4,999,021.84|  
|Canada|$1,343,109.10|$1,343,109.10|  
|France|$2,490,944.57|$2,490,944.57|  
|Germany|$2,775,195.60|$2,775,195.60|  
|United Kingdom|$5,057,076.55|$5,057,076.55|  
|United States|$9,389,479.79||  
|Grand Total|$26,054,827.45|$16,665,347.67|  
  
The following table shows the final report that you might get if you used this measure in a PivotTable:  
  
|Non USA Internet Sales|Column Labels||||  
|--------------------------|-----------------|----|----|----|  
|Row Labels|Accessories|Bikes|Clothing|Grand Total|  
|2005||$1,526,481.95||$1,526,481.95|  
|2006||$3,554,744.04||$3,554,744.04|  
|2007|$156,480.18|$5,640,106.05|$70,142.77|$5,866,729.00|  
|2008|$228,159.45|$5,386,558.19|$102,675.04|$5,717,392.68|  
|Grand Total|$384,639.63|$16,107,890.23|$172,817.81|$16,665,347.67|  
  
## See also  
[RELATEDTABLE function &#40;DAX&#41;](relatedtable-function-dax.md)  
[Filter functions &#40;DAX&#41;](filter-functions-dax.md)  
  
