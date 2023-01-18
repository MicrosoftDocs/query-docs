---
description: "Learn more about: RUNNINGSUM"
title: "RUNNINGSUM function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.subservice: dax
ms.date: 01/17/2023
ms.topic: reference
author: masanto-msft
ms.author: masanto
recommendations: false

---

# RUNNINGSUM

Returns a running sum calculated along the given axis of the Visual Calculation data grid. That is, the sum of the given column calculated over all rows up to the current row.

## Syntax

```dax
RUNNINGSUM ( <column>[, <axis>][, <blanks>] )
```

### Parameters

|Term|Definition|
|--------|--------------|
|column|The column that provides the value for each row.|
|axis|(Optional) An axis reference, the direction along which the running sum will be calculated.|
|blanks|(Optional) An enumeration that defines how to handle blank values when sorting. </br>This parameter is reserved for future use.|

## Return value

A scalar value, the running sum up to the current row.

## Remarks

This function can be used in Visual Calculations only.

The \<axis> and \<blanks> parameters can be omitted.

## Example

The following DAX query:

```dax
VAR _Core = SUMMARIZECOLUMNS(
	'DimDate'[Year],
	'DimProduct'[ProductCategoryName],
    "CurrentYearSales", SUM('FactInternetSales'[SalesAmount])
)
TABLE t = _Core
	WITH VISUAL SHAPE
	AXIS ROWS
		GROUP [Year]
		ORDER BY [Year]
	AXIS COLUMNS
		GROUP [ProductCategoryName]
		ORDER BY [ProductCategoryName]
	DENSIFY "isDensified"
COLUMN t[SalesUpToDate] = RUNNINGSUM([CurrentYearSales], Rows)
EVALUATE t
ORDER BY t[ProductCategoryName] ASC, t[Year] ASC
```

Returns a table that summarizes the total sales for each product category and calendar year, as well as the total sales for that category up to a given year.

## See also

[INDEX](index-function-dax.md)
[MOVINGAVERAGE](movingaverage-function-dax.md)
[ORDERBY](orderby-function-dax.md)
[PARTITIONBY](partitionby-function-dax.md)
[WINDOW](window-function-dax.md)
