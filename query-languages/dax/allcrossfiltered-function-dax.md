---
title: "ALLCROSSFILTERED function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 04/08/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ALLCROSSFILTERED

Clear all filters which are applied to a table.
  
## Syntax  
  
```dax
ALLCROSSFILTERED(<table>)
```
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|table|The table that you want to clear filters on. |  
  
## Return value  

N/A. See remarks.
  
## Remarks  

ALLCROSSFILTERED can only be used to clear filters but not to return a table.

## Example  


```dax
DEFINE 
MEASURE FactInternetSales[TotalQuantity1] = 
	CALCULATE(SUM(FactInternetSales[OrderQuantity]), ALLCROSSFILTERED(FactInternetSales))
MEASURE FactInternetSales[TotalQuantity2] = 
	CALCULATE(SUM(FactInternetSales[OrderQuantity]), ALL(FactInternetSales))
EVALUATE
	SUMMARIZECOLUMNS(DimSalesReason[SalesReasonName], 
		"TotalQuantity1", [TotalQuantity1],
		"TotalQuantity2", [TotalQuantity2])
	ORDER BY DimSalesReason[SalesReasonName]

```

Returns


|DimSalesReason[SalesReasonName]  |[TotalQuantity1]  |[TotalQuantity2] |
|---------|---------|---------|
|Demo Event    |    60398     |         |
|Magazine Advertisement    |    60398     |         |
|Manufacturer     |   60398      |   1818      |
|On Promotion     |   60398      |   7390      |
|Other     |   60398      |    3653     |
|Price     |   60398      |    47733     |
|Quality     |   60398      |   1551      |
|Review     |   60398      |    1640     |
|Sponsorship   |   60398      |         |
|Television  Advertisement    |   60398      |     730    |

 
  
> [!NOTE]
> There is a direct or indirect many-to-many relationship between FactInternetSales table and DimSalesReason table.