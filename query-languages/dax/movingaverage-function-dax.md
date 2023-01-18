---
description: "Learn more about: MOVINGAVERAGE"
title: "MOVINGAVERAGE function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.subservice: dax
ms.date: 01/17/2023
ms.topic: reference
author: masanto-msft
ms.author: masanto
recommendations: false

---

# MOVINGAVERAGE

Returns a moving average calculated along the given axis of the Visual Calculation data grid. That is, the average of the given column calculated over the last \<windowSize> rows.

## Syntax

```dax
MOVINGAVERAGE ( <column>, <windowSize>[, <includeCurrent>][, <axis>][, <blanks>] )
```

### Parameters

|Term|Definition|
|--------|--------------|
|column|The column that provides the value for each row.|
|windowSize|The number of rows before the current row to include in the calculation. Must be a constant value.|
|includeCurrent|(Optional) A logical value specifying whether or not to include the current row in the range. Default value is True.|
|axis|(Optional) An axis reference, the direction along which the moving average will be calculated.|
|blanks|(Optional) An enumeration that defines how to handle blank values when sorting. </br>This parameter is reserved for future use.|

## Return value

A scalar value, the moving average at the current row.

## Remarks

This function can be used in Visual Calculations only.

The \<includeCurrent>, \<axis> and \<blanks> parameters can be omitted.

## Example 1

The following DAX query:

```dax
DEFINE
VAR _Core = SUMMARIZECOLUMNS(
	'DimDate'[Year],
	'DimDate'[MonthNumberOfYear],
	'DimProduct'[ProductCategoryName],
    "CurrentMonthSales", SUM('FactInternetSales'[SalesAmount])
)
TABLE t = _Core
	WITH VISUAL SHAPE
	AXIS ROWS
		GROUP [Year], [MonthNumberOfYear]
		ORDER BY [Year], [MonthNumberOfYear]
	AXIS COLUMNS
		GROUP [ProductCategoryName]
		ORDER BY [ProductCategoryName]
	DENSIFY "isDensified"
COLUMN t[AvgSalesLast6Months] = MOVINGAVERAGE([CurrentMonthSales], 5, Rows)
EVALUATE t
ORDER BY t[ProductCategoryName] ASC, t[Year] ASC, t[MonthNumberOfYear] ASC
```

Returns a table that summarizes the total sales for each product category and calendar month, as well as the average of total sales for that category in the last 6 months.

## Example 2

The following DAX query:

```dax
DEFINE
VAR _Core = SUMMARIZECOLUMNS(
	'DimDate'[Year],
	'DimDate'[MonthNumberOfYear],
	'DimProduct'[ProductCategoryName],
    "CurrentMonthSales", SUM('FactInternetSales'[SalesAmount])
)
TABLE t = _Core
	WITH VISUAL SHAPE
	AXIS ROWS
		GROUP [Year], [MonthNumberOfYear]
		ORDER BY [Year], [MonthNumberOfYear]
	AXIS COLUMNS
		GROUP [ProductCategoryName]
		ORDER BY [ProductCategoryName]
	DENSIFY "isDensified"
COLUMN t[AvgSalesPrev12Months] = MOVINGAVERAGE([CurrentMonthSales], 12, FALSE, Rows, KEEP)
EVALUATE t
ORDER BY t[ProductCategoryName] ASC, t[Year] ASC, t[MonthNumberOfYear] ASC
```

Returns a table that summarizes the total sales for each product category and calendar month, as well as the average of total sales for that category in the previous 12 months (not including the current month).

## See also

[INDEX](index-function-dax.md)
[ORDERBY](orderby-function-dax.md)
[PARTITIONBY](partitionby-function-dax.md)
[RUNNINGSUM](runningsum-function-dax.md)
[WINDOW](window-function-dax.md)
