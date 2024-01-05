---
description: "Learn more about: LOOKUP"
title: "LOOKUP function (DAX) | Microsoft Docs"
---
# LOOKUP

Used in visual calculations only. Returns a value from a cell in a visual matrix by using absolute navigation. You can specify a value as a filter for any axis on the visual matrix. Anything not specified is inferred from the context. If Lookup can’t result in single value, an error is returned.

## Syntax

```dax
LOOKUP(<column>[, <filter1> [, <filter2> [, …]]])
```

### Parameters

|Term|Definition|
|--------|--------------|
|column| Only column reference is allowed,  For example [Sales] is allowed, but [Sales] – [Cost] is not, nor is SUM([Sales]) |
|filter1, filter2,…|(Optional) Filter has to be either: 1. An equality filter. For example [Year]=2019 or [Year]=MAX([Year]). 2.The Collapse function. For example, LOOKUP([Sales], Collapse([Country])) returns the subtotal value for Sales for all Countries|

## Return value

The value of **column** at the row after filters are applied.

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
lookup([SumOfInternetSales], [Year] = 2006, [MonthNumberOfYear] = 1, [Month] = "January")

evaluate selectcolumns(
	filter(t, not isblank([SumOfInternetSales])),
	[ProductCategoryName], [ProductSubcategoryName], [Year], [MonthNumberOfYear], [SumOfInternetSales], [ccLookup]
)
order by [ProductCategoryName], [ProductSubcategoryName], [Year], [MonthNumberOfYear]
```
