---
description: "Learn more about: ToJSON"
title: "ToJSON function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 10/26/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# ToJSON

Returns a table as a string using JSON format. This function applies to Power BI Desktop only.
  
## Syntax  
  
```dax
ToJSON(<Table>, [MaxRows])
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Table|The table to be converted to JSON.|  
|MaxRows|(Optional) The maximum number fo rows to convert. Default is 10 rows.|  
  
## Return value

A string with JSON representation of the table. The representation contains column names as "header", count-of-rows as “rowCount”, and values as “data”.
  
## Example

The following DAX query:

```dax
EVALUATE
{ToJSON(DimSalesTerritory)}
```

Returns:

```json
{
"header": ["'DimSalesTerritory'[SalesTerritoryKey]", "'DimSalesTerritory'[SalesTerritoryAlternateKey]", "'DimSalesTerritory'[SalesTerritoryRegion]", "'DimSalesTerritory'[SalesTerritoryCountry]", "'DimSalesTerritory'[SalesTerritoryGroup]"],<br>
"rowCount": 11,
"data": [
[1, 1, "Northwest", "United States", "North America"],
[2, 2, "Northeast", "United States", "North America"],
[3, 3, "Central", "United States", "North America"],
[4, 4, "Southwest", "United States", "North America"],
[5, 5, "Southeast", "United States", "North America"],
[6, 6, "Canada", "Canada", "North America"],
[7, 7, "France", "France", "Europe"],
[8, 8, "Germany", "Germany", "Europe"],
[9, 9, "Australia", "Australia", "Pacific"],
[10, 10, "United Kingdom", "United Kingdom", "Europe"]
]
}
```

## See also

[ToCSV](tocsv-function-dax.md)  
[EvaluateAndLog](evaluateandlog-function-dax.md)  
