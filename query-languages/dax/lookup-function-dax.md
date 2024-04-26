---
description: "Learn more about: LOOKUP"
title: "LOOKUP function (DAX) | Microsoft Docs"
---
# LOOKUP

Used in visual calculations only. Returns a value from a cell in a visual matrix by using absolute navigation. You can specify a value as a filter for any axis on the visual matrix. Anything not specified is inferred from the context. If Lookup can’t result in single value, an error is returned.

## Syntax

```dax
LOOKUP(<scalar>|<colref>, <colref>, <scalar>|<colref>[, <colref>, <sclar>|<colref>]...)
```

### Parameters

|Term|Definition|
|--------|--------------|
|scalar/colref| The expression or value from column that we wants to get. |
|colref|(Optional) The column to be filtered. For example, when we want [Year] = 2019, we put [Year] here.|
|scalar/colref|(Optional) The value to filter. In above example, put 2019 here.|

## Return value

The value of **column** or **expression** after filters are applied.

If there isn't a match, an error is returned.

If multiple rows match the filters, an error is returned.

## Example 1

In this example, LOOKUP retrieves the sum of sale easily for filters: [Year] = 2006, [MonthNumberOfYear] = 1, [Month] = "January".

```dax
// GB column references
Define
var _Core = SUMMARIZECOLUMNS(
        'DimDate'[Year],
		'DimDate'[Month], 'DimDate'[MonthNumberOfYear],
        'DimProduct'[ProductCategoryName],
        'DimProduct'[ProductSubcategoryName],
      "SumOfInternetSales", CALCULATE(SUM('FactInternetSales'[SalesAmount]))
    )
table t = _Core
	with visual shape
	axis rows 
		group [Year]
		group [Month], [MonthNumberOfYear]
		order by [Year], [MonthNumberOfYear] 
	axis columns 
		group [ProductCategoryName]
		group [ProductSubcategoryName]
		order by [ProductCategoryName], [ProductSubcategoryName] 
	densify "isDensified"

column t[ccLookup] = 
lookup([SumOfInternetSales], [Year], 2006, [MonthNumberOfYear], 1, [Month], "January")

evaluate selectcolumns(
	filter(t, not isblank([SumOfInternetSales])),
	[ProductCategoryName], [ProductSubcategoryName], [Year], [MonthNumberOfYear], [SumOfInternetSales], [ccLookup]
)
order by [ProductCategoryName], [ProductSubcategoryName], [Year], [MonthNumberOfYear]
```
