---
description: "Learn more about: RANGE"
title: "RANGE function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.subservice: dax
ms.date: 01/17/2023
ms.topic: reference
author: masanto-msft
ms.author: masanto
recommendations: false

---

# RANGE

Returns an interval of rows within the given axis, relative to the current row. This interval will be comprised of either the last \<step> rows before the current one, or the first \<step> rows after the current one.

## Syntax

```dax
RANGE ( <step>[, <includeCurrent>][, <axis>][, <blanks>][, <reset>] )
```

### Parameters

|Term|Definition|
|--------|--------------|
|step|The number of rows before (negative value) or after (positive value) the current row to include in the range. Must be a constant value.</br>- If negative, the window will contain the last -step rows before the current row.</br>- Otherwise, the window will contain the first step rows after the current row.|
|includeCurrent|(Optional) A logical value specifying whether or not to include the current row in the range. Default value is True.|
|axis|(Optional) An axis reference, the direction along which the interval will be created.|
|blanks|(Optional) An enumeration that defines how to handle blank values when sorting. </br>This parameter is reserved for future use.|
|reset|(Optional) Indicates if the calculation resets, and at which level of the visual shape's column hierarchy. Accepted values are: NONE, LOWESTPARENT, HIGHESTPARENT, or an integer. The behavior depends on the integer sign: </br> - If zero or omitted, the calculation does not reset. Equivalent to NONE. </br> - If positive, the integer identifies the column starting from the highest, independent of grain. HIGHESTPARENT is equivalent to 1. </br> - If negative, the integer identifies the column starting from the lowest, relative to the current grain. LOWESTPARENT is equivalent to -1. |

## Return value

An interval of data rows.

## Remarks

This function can be used in visual calculations only.

The \<includeCurrent>, \<axis>, \<blanks> and \<reset> parameters can be omitted.

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
COLUMN t[TotalSalesLast6Months] = CALCULATE(
	SUM([CurrentMonthSales]),
	RANGE(-5, Rows)
)
EVALUATE t
ORDER BY t[ProductCategoryName] ASC, t[Year] ASC, t[MonthNumberOfYear] ASC
```

Returns a table that summarizes the total sales for each product category and month, as well as the total sales in the last 6 months.

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
COLUMN t[TotalSalesFollowingYear] = CALCULATE(
	SUM([CurrentMonthSales]),
	RANGE(12, FALSE, Rows, KEEP)
)
EVALUATE t
ORDER BY t[ProductCategoryName] ASC, t[Year] ASC, t[MonthNumberOfYear] ASC
```

Returns a table that summarizes the total sales for each product category and month, as well as the total sales in the following 12 months, not including the current month.

## See also

[INDEX](index-function-dax.md)
[ORDERBY](orderby-function-dax.md)
[PARTITIONBY](partitionby-function-dax.md)
[WINDOW](window-function-dax.md)
