---
description: "Learn more about: NEXT"
title: "NEXT function (DAX)"
---

# NEXT

[!INCLUDE[applies-to-visual-calculations](includes/applies-to-visual-calculations.md)]

Used in visual calculations only. Retrieves a value in the next element of an axis in the visual matrix.

## Syntax

```dax
NEXT ( <column>[, <steps>][, <axis>][, <orderBy>][, <blanks>][, reset] )
```

### Parameters

|Term|Definition|
|--------|--------------|
|`column`|The column to be retrieved.|
|`steps`| (Optional) Indicates the number of rows to go forward to fetch the value. If omitted, **1** is used (the exactly next row).|
|`axis`|(Optional) An axis reference. If omitted, the first axis of the Visual Shape definition is used.|
|`orderBy`|(Optional) An ORDERBY() clause with expressions that determine how to sort each partition along the `axis`. If `orderBy` is not provided, the data is sorted by the grouping columns on the default `axis` in ascending order by default.|
|`blanks`|(Optional) An enumeration that defines how to handle blank values when sorting the `axis`. </br>The supported values are:<ul><li>`DEFAULT`(the default value), where the behavior for numerical values is blank values are ordered between zero and negative values. The behavior for strings is blank values are ordered before all strings, including empty strings.</li><li>`FIRST`, blanks are always ordered on the beginning, regardless of ascending or descending sorting order.</li><li>`LAST`, blanks are always ordered on the end, regardless of ascending or descending sorting order. </li></ul>|
|`reset`|(Optional) Indicates if the calculation resets, and at which level of the visual shape's column hierarchy. Accepted values are: a field reference to a column in the current visual shape, `NONE` (default), `LOWESTPARENT`, `HIGHESTPARENT`, or an integer. The behavior depends on the integer sign: </br> - If zero or omitted, the calculation does not reset. Equivalent to `NONE`. </br> - If positive, the integer identifies the column starting from the highest, independent of grain. `HIGHESTPARENT` is equivalent to 1. </br> - If negative, the integer identifies the column starting from the lowest, relative to the current grain. `LOWESTPARENT` is equivalent to -1.|

## Return value

The value of `column` from the next element of the axis.

## Remarks

This function can only be used in a visual calculation.

If the value of `reset` is absolute (i.e., a positive integer, `HIGHESTPARENT` or a field reference) and the calculation is evaluated at or above the target level in the hierarchy, the calculation resets for each individual element. That is, the function is evaluated within a partition containing only that specific element.

## Example

The following visual calculation returns the sales amount of the next row on ROWS axis, that resets on the lowest parent. 

```dax
NextInternetSalesAmount = NEXT ( [Sum of SalesAmount], ROWS, LowestParent )
```

The screenshot below shows the visual matrix and the visual calculation expression:

![DAX visual calculation](media/dax-queries/dax-visualcalc-next.png)

## Related content

[FIRST](first-function-dax.md)
[LAST](last-function-dax.md)
[PREVIOUS](PREVIOUS-function-dax.md)
