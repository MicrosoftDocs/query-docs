---
description: "Learn more about: FIRST"
title: "FIRST function (DAX)"
---

# FIRST

[!INCLUDE[applies-to-visual-calculations](includes/applies-to-visual-calculations.md)]

Used in visual calculations only. Retrieves a value in the visual matrix from the first element of an axis.

## Syntax

```dax
FIRST ( <column>[, <axis>][, <blanks>][, reset] )
```

### Parameters

|Term|Definition|
|--------|--------------|
|`column`|The column to be retrieved.|
|`axis`|(Optional) An axis reference. If omitted, the first axis of the Visual Shape definition is used.|
|`blanks`|(Optional) An enumeration that defines how to handle blank values when sorting. </br>The supported values are:<ul><li>`DEFAULT` (the default value), where the behavior for numerical values is blank values are ordered between zero and negative values. The behavior for strings is blank values are ordered before all strings, including empty strings.</li><li>`FIRST`, blanks are always ordered on the beginning, regardless of ascending or descending sorting order.</li><li>`LAST`, blanks are always ordered on the end, regardless of ascending or descending sorting order. </li></ul>|
|`reset`|(Optional) Indicates if the calculation resets, and at which level of the visual shape's column hierarchy. Accepted values are: a field reference to a column in the current visual shape, `NONE` (default), `LOWESTPARENT`, `HIGHESTPARENT`, or an integer. The behavior depends on the integer sign: </br> - If zero or omitted, the calculation does not reset. Equivalent to `NONE`. </br> - If positive, the integer identifies the column starting from the highest, independent of grain. `HIGHESTPARENT` is equivalent to 1. </br> - If negative, the integer identifies the column starting from the lowest, relative to the current grain. `LOWESTPARENT` is equivalent to -1.|

## Return value

The value of `column` from the first element of the axis.

## Remarks

This function can only be used in a visual calculation.

## Example

The following visual calculation returns the sales amount of the first row on ROWS axis, that resets on the lowest parent. 

```dax
FirstInternetSalesAmount = FIRST ( [Sum of SalesAmount], ROWS, LowestParent )
```

The screenshot below shows the visual matrix and the visual calculation expression:

![DAX visual calculation](media/dax-queries/dax-visualcalc-first.png)

## Related content

[LAST](last-function-dax.md)
[PREVIOUS](previous-function-dax.md)
[NEXT](next-function-dax.md)
