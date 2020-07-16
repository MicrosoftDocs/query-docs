---
title: "REMOVEFILTERS function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# REMOVEFILTERS

Clear filters from the specified tables or columns.
  
## Syntax  
  
```dax
REMOVEFILTERS([<table> | <column>[, <column>[, <column>[,…]]]])
```
  
### Parameters
  
|Term|Definition|  
|--------|--------------|  
|table|The table that you want to clear filters on. |  
|column|The column that you want to clear filters on.|  
  
## Return value

N/A. See remarks.
  
## Remarks  

- REMOVEFILTERS can only be used to clear filters but not to return a table.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example 1

DAX query

```dax
DEFINE
MEASURE FactInternetSales[TotalSales] = SUM(FactInternetSales[SalesAmount])
MEASURE FactInternetSales[%Sales] = DIVIDE([TotalSales], CALCULATE([TotalSales],REMOVEFILTERS()))

EVALUATE
    SUMMARIZECOLUMNS(
      ROLLUPADDISSUBTOTAL(DimProductCategory[EnglishProductCategoryName], "IsGrandTotal"),
      "TotalSales", [TotalSales],
      "%Sales", [%Sales]
    )
ORDER BY
  [IsGrandTotal] DESC, [TotalSales] DESC 
```

Returns

|DimProductCategory[EnglishProductCategoryName] | [IsGrandTotal] |[TotalSales]  |[%Sales]  |
|---------|---------|---------|---------|
|Row1     |   True      |   29358677.2207      |     1    |
|Bikes     |  False       |   28318144.6507      |   0.964557920570538      |
|Accessories    | False        |    700759.96     |   0.023868921434441      |
|Clothing    |  False       |   339772.61      |    0.0115731579950215     |

## Example 2

DAX query

```dax
DEFINE
MEASURE FactInternetSales[TotalSales] = SUM(FactInternetSales[SalesAmount])
MEASURE FactInternetSales[%Sales] = DIVIDE([TotalSales], CALCULATE([TotalSales],REMOVEFILTERS(DimProductSubcategory[EnglishProductSubcategoryName])))

EVALUATE
    SUMMARIZECOLUMNS(
      DimProductCategory[EnglishProductCategoryName],
      DimProductSubcategory[EnglishProductSubcategoryName],
      "TotalSales", [TotalSales],
      "%Sales", [%Sales]
    )
ORDER BY
  DimProductCategory[EnglishProductCategoryName] ASC,
  DimProductSubcategory[EnglishProductSubcategoryName] ASC
```

Returns

|DimProductCategory [EnglishProductCategoryName]  |DimProductSubcategory [EnglishProductSubcategoryName]  |[TotalSales]  |[%Sales] |
|---------|---------|---------|---------|
|Accessories     |   Bike Racks      |   39360      |   0.05616759      |
|Accessories     |   Bike Stands      |   39591      |   0.05649723     |
|Accessories     |   Bottles and Cages      |   56798.19      |   0.08105228      |
|Accessories     |   Cleaners      |   7218.6      |   0.0103011      |
|Accessories     |   Fenders      |   46619.58      |   0.06652717      |
|Accessories     |   Helmets     |   225335.6      |   0.3215589      |
|Accessories     |   Hydration Packs      |   40307.67      |   0.05751994      |
|Accessories     |   Tires and Tubes      |   245529.32      |   0.35037578      |
|Bikes     |   Mountain Bikes     |   9952759.564      |   0.35146228      |
|Bikes     |   Road Bikes      |  14520584.04       |   0.51276608      |
|Bikes     |   Touring Bikes      |  3844801.05       |   0.13577164     |
|Clothing     |   Caps      |  19688.1       |   0.05794493      |
|Clothing     |   Gloves      |  35020.7       |   0.10307099      |
|Clothing     |   Jerseys      |  172950.68       |   0.5090189      |
|Clothing     |   Shorts     |  71319.81      |   0.20990453      |
|Clothing     |   Socks      |  5106.32      |   0.01502864      |
|Clothing     |   Vests      |  35687       |   0.10503201      |
