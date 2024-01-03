---
description: "Learn more about: PREVIOUS"
title: "PREVIOUS function (DAX) | Microsoft Docs"
---

# PREVIOUS

Used in Visual Caculations only. Retrieves a value in the previous row of an axis in the data grid.
  
## Syntax  
  
```dax
PREVIOUS ( <expression>[, <steps>][, <axis>][, <blanks>][, reset] )
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|expression| The expression to be evaluated.|
|steps| (Optional) Indicates the number of rows to go backward to fetch the value. If omitted, **1** is used (the exactly previous row).|
|axis|(Optional) An axis reference. If omitted, the first axis of the Visual Shape definition is used.|
|blanks|(Optional) An enumeration that defines how to handle blank values when sorting. </br>The supported values are:<ul><li>DEFAULT (the default value), where the behavior for numerical values is blank values are ordered between zero and negative values. The behavior for strings is blank values are ordered before all strings, including empty strings.</li><li>FIRST, blanks are always ordered on the beginning, regardless of ascending or descending sorting order.</li><li>LAST, blanks are always ordered on the end, regardless of ascending or descending sorting order. </li></ul>|
|reset|(Optional) Specifies how the calculation restarts. Valid values are: None, LowestParent, HighestParent, or an integer. None is the default value.|


## Return value

The value of \<expression> evaluated from the previous row of the axis.
  
## Remarks

This function can only be used in a Visual Caculation.

## Example

With the following DAX query:
  
```dax
DEFINE
    VAR Core =
        SUMMARIZECOLUMNS (
            ROLLUPADDISSUBTOTAL (
                'DimDate'[Year],
                "IsGrandTotalRowTotal",
                ROLLUPGROUP ( 'DimDate'[Month], 'DimDate'[MonthNumberOfYear] ),
                "IsDM1Total"
            ),
            ROLLUPADDISSUBTOTAL (
                'DimProduct'[ProductCategoryName],
                "IsGrandTotalColumnTotal",
                'DimProduct'[ProductSubcategoryName],
                "IsDM4Total"
            ),
            "SumSalesAmount", CALCULATE ( SUM ( 'FactInternetSales'[SalesAmount] ) )
        )
    TABLE t = Core
        WITH VISUAL SHAPE
        AXIS ROWS
            GROUP [Year]
                TOTAL [IsGrandTotalRowTotal]
            GROUP
                [Month],
                [MonthNumberOfYear]
                TOTAL [IsDM1Total]
            ORDER BY
                [Year],
                [MonthNumberOfYear]
        AXIS COLUMNS
            GROUP [ProductCategoryName]
                TOTAL [IsGrandTotalColumnTotal]
            GROUP [ProductSubcategoryName]
                TOTAL [IsDM4Total]
            ORDER BY
                [ProductCategoryName],
                [ProductSubcategoryName]
        DENSIFY "isDensified"
    COLUMN t[PreviousPreviousInternetSalesAmount] =
        PREVIOUS ( [SumSalesAmount], 2, ROWS, LowestParent )

EVALUATE
t
ORDER BY
    [ProductCategoryName],
    [ProductSubcategoryName],
    [YEAR],
    [MonthNumberOfYear]
```

PreviousPreviousInternetSalesAmount is added as a Visual Caculation that returns SalesAmount of the previous previous row on ROWS axis, that resets on the lowest parent. On Year and Month level, it returns the SalesAmount of the previous previous month within the current year; for the first two months of the year, it returns blank. On Year level, it returns SalesAmount of the previous previous year of the current year; for the first two years, it returns blank.

## Related content

[FIRST](first-function-dax.md)  
[LAST](last-function-dax.md)  
[NEXT](next-function-dax.md)
