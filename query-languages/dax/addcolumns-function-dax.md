---
title: "ADDCOLUMNS Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ADDCOLUMNS Function (DAX)
Adds calculated columns to the given table or table expression.  
  
## Syntax  
  
```dax
ADDCOLUMNS(<table>, <name>, <expression>[, <name>, <expression>]…)  
```
  
#### Parameters  
*table*  
Any DAX expression that returns a table of data.  
  
*name*  
The name given to the column, enclosed in double quotes.  
  
*expression*  
Any DAX expression that returns a scalar expression, evaluated for each row of *table*.  
  
## Return Value  
A table with all its original columns and the added ones.  
  
## Remarks  
  
## Example  
The following example returns an extended version of the Product Category table that includes total sales values from the reseller channel and the internet sales.  
  
```dax
ADDCOLUMNS(ProductCategory,   
               , "Internet Sales", SUMX(RELATEDTABLE(InternetSales_USD), InternetSales_USD[SalesAmount_USD])  
               , "Reseller Sales", SUMX(RELATEDTABLE(ResellerSales_USD), ResellerSales_USD[SalesAmount_USD]))  
```dax
The following table shows a preview of the data as it would be received by any function expecting to receive a table:  
  
||||||  
|-|-|-|-|-|  
|**ProductCategory[ProductCategoryName]**|**ProductCategory[ProductCategoryAlternateKey]**|**ProductCategory[ProductCategoryKey]**|**[Internet Sales]**|**[Reseller Sales]**|  
|Bikes|1|1|25107749.77|63084675.04|  
|Components|2|2||11205837.96|  
|Clothing|3|3|306157.5829|1669943.267|  
|Accessories|4|4|640920.1338|534301.9888|  
  
