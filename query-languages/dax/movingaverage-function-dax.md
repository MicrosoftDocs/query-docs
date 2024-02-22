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

Returns a moving average calculated along the given axis of the visual calculation data grid. That is, the average of the given column calculated over the last \<windowSize> rows.

## Syntax

```dax
MOVINGAVERAGE ( <column>, <windowSize>[, <includeCurrent>][, <axis>][, <blanks>][, <reset>] )
```

### Parameters

|Term|Definition|
|--------|--------------|
|column|The column that provides the value for each row.|
|windowSize|The number of rows to include in the calculation. Must be a constant value.|
|includeCurrent|(Optional) A logical value specifying whether or not to include the current row in the range. Default value is True.|
|axis|(Optional) An axis reference, the direction along which the moving average will be calculated.|
|blanks|(Optional) An enumeration that defines how to handle blank values when sorting. </br>This parameter is reserved for future use.|
|reset|(Optional) Indicates if the calculation resets, and at which level of the visual shape's column hierarchy. Accepted values are: NONE, LOWESTPARENT, HIGHESTPARENT, or an integer. The behavior depends on the integer sign: </br> - If zero or omitted, the calculation does not reset. Equivalent to NONE. </br> - If positive, the integer identifies the column starting from the highest, independent of grain. HIGHESTPARENT is equivalent to 1. </br> - If negative, the integer identifies the column starting from the lowest, relative to the current grain. LOWESTPARENT is equivalent to -1. |

## Return value

A scalar value, the moving average at the current row.

## Remarks

This function can be used in visual calculations only.

The \<includeCurrent>, \<axis>, \<blanks> and \<reset> parameters can be omitted.

## Example 1

Given a table that summarizes the total sales for each product category and calendar month, the following DAX query adds a column with the average of total sales for that category in the last 6 months:

```dax
AvgSalesLast6Months = MOVINGAVERAGE([SalesAmount], 6, Rows)
```

The screenshot below shows the visual matrix and the visual calculation expression:

![DAX visual calculation](media/dax-queries/dax-visualcalc-movingaverage.png)

## Example 2

Given the same table, the following DAX query adds a column with the average of total sales for that category in the previous 12 months (not including the current month):

```dax
AvgSalesPrev12Months = MOVINGAVERAGE([SalesAmount], 12, FALSE, Rows, KEEP)
```

## See also

[INDEX](index-function-dax.md)  
[ORDERBY](orderby-function-dax.md)  
[PARTITIONBY](partitionby-function-dax.md)  
[RUNNINGSUM](runningsum-function-dax.md)  
[WINDOW](window-function-dax.md)  
