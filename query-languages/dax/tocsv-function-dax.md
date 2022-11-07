---
description: "Learn more about: TOCSV"
title: "TOCSV function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 10/26/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# TOCSV

Returns a table as a string in CSV format.
  
## Syntax  
  
```dax
TOCSV(<Table>, [MaxRows], [Delimiter], [IncludeHeaders])
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Table|The table to be converted to CSV.|  
|MaxRows| (Optional) The maximum number fo rows to convert. Default is 10 rows.|  
|Delimiter|(Optional) A column delimiter. Default is comma ",".|  
|IncludeHeaders|(Optional) Specifies a header with column name as the first row. Default is True.|
  
## Return value

A string with CSV representation of the table.
  
## Example

The following DAX query:

```dax
EVALUATE
{TOCSV(DimSalesTerritory)}

```

Returns:

```
'DimSalesTerritory'[SalesTerritoryKey],'DimSalesTerritory'[SalesTerritoryAlternateKey],'DimSalesTerritory'[SalesTerritoryRegion],'DimSalesTerritory'[SalesTerritoryCountry],'DimSalesTerritory'[SalesTerritoryGroup]
1,1,Northwest,United States,North America
2,2,Northeast,United States,North America
3,3,Central,United States,North America
4,4,Southwest,United States,North America
5,5,Southeast,United States,North America
6,6,Canada,Canada,North America
7,7,France,France,Europe
8,8,Germany,Germany,Europe
9,9,Australia,Australia,Pacific
10,10,United Kingdom,United Kingdom,Europe
```

## See also

[TOJSON](tojson-function-dax.md)  
[EVALUATEANDLOG](evaluateandlog-function-dax.md)  
