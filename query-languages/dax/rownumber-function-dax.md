---
description: "Learn more about: ROWNUMBER"
title: "ROWNUMBER function (DAX)"
author: rahulten
---
# ROWNUMBER

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the unique ranking for the current context within the specified partition, sorted by the specified order. If a match cannot be found then rownumber is blank.

## Syntax

```dax
ROWNUMBER ( [<relation> or <axis>][, <orderBy>][, <blanks>][, <partitionBy>][, <matchBy>][, <reset>] )
```

### Parameters

|Term|Definition|
|--------|--------------|
|`relation`|(Optional) A table expression from which the output row is returned. </br>If specified, all columns in `orderBy` and `partitionBy` must come from it. </br>If omitted: </br>- `orderBy` must be explicitly specified.</br>- All `orderBy` and `partitionBy` columns must be fully qualified and come from a single table. </br>- Defaults to ALLSELECTED() of all columns in `orderBy` and `partitionBy`.|
|`axis`|(Optional) An axis in the visual shape. Available in visual calculations only, and replaces `relation`.
|`orderBy`|(Optional) An ORDERBY() clause containing the columns that define how each partition is sorted. </br>If omitted: </br>- `relation` must be explicitly specified. </br>- Defaults to ordering by every column in `relation` that is not already specified in `partitionBy`.|
|`blanks`|(Optional) An enumeration that defines how to handle blank values when sorting the `relation` or `axis`. </br>The supported values are:<ul><li>`DEFAULT` (the default value), where the behavior for numerical values is blank values are ordered between zero and negative values. The behavior for strings is blank values are ordered before all strings, including empty strings.</li><li>`FIRST`, blanks are always ordered on the beginning, regardless of ascending or descending sorting order.</li><li>`LAST`, blanks are always ordered on the end, regardless of ascending or descending sorting order. </li></ul></br>Note, when the `blanks` parameter and blanks in the [ORDERBY()](orderby-function-dax.md) function on individual expressions are both specified, `blanks` on individual orderBy expression takes priority for the relevant orderBy expression, and orderBy expressions without `blanks` being specified will honor the `blanks` parameter on the parent function.|
|`partitionBy`|(Optional) A [PARTITIONBY()](partitionby-function-dax.md) clause containing the columns that define how `relation` is partitioned. If omitted, `relation` is treated as a single partition.|
|`matchBy`|(Optional) A [MATCHBY()](matchby-function-dax.md) clause containing the columns that define how to match data and identify the current row.|
|`reset`|(Optional) Available in visual calculations only. Indicates if the calculation resets, and at which level of the visual shape's column hierarchy. Accepted values are: a field reference to a column in the current visual shape, `NONE` (default), `LOWESTPARENT`, `HIGHESTPARENT`, or an integer. The behavior depends on the integer sign: </br> - If zero or omitted, the calculation does not reset. Equivalent to `NONE`. </br> - If positive, the integer identifies the column starting from the highest, independent of grain. `HIGHESTPARENT` is equivalent to 1. </br> - If negative, the integer identifies the column starting from the lowest, relative to the current grain. `LOWESTPARENT` is equivalent to -1.|

## Return value

The rownumber number for the current context.

## Remarks

Each `orderBy`, `partitionBy`, and `matchBy` column must have a corresponding outer value to help define the current row on which to operate, with the following behavior:

- If there is exactly one corresponding outer column, its value is used.
- If there is no corresponding outer column, then:
  - ROWNUMBER will first determine all `orderBy`, `partitionBy`, and `matchBy` columns that have no corresponding outer column.
  - For every combination of existing values for these columns in ROWNUMBER parent context, ROWNUMBER is evaluated and a row is returned.
  - ROWNUMBER’s final output is a union of these rows.
- If there is more than one corresponding outer column, an error is returned.

If `matchBy` is present, then ROWNUMBER will try to use columns in `matchBy` and `partitionBy` to idenfity the current row.
If the columns specified within `orderBy` and `partitionBy` cannot uniquely identify every row in `relation`, then:

- ROWNUMBER will try to find the least number of additional columns required to uniquely identify every row.
- If such columns can be found, ROWNUMBER will
  - Try to find the least number of additional columns required to uniquely identify every row.
  - Automatically append these new columns to `orderBy` clause.
  - Sort each partition using this new set of orderBy columns.
- If such columns cannot be found and the function detects a tie at runtime, an error is returned.

`reset` can be used in visual calculations only, and cannot be used in combination with `orderBy` or `partitionBy`. If `reset` is present, `axis` can be specified but `relation` cannot.

If the value of `reset` is absolute (i.e., a positive integer, `HIGHESTPARENT` or a field reference) and the calculation is evaluated at or above the target level in the hierarchy, the calculation resets for each individual element. That is, the function is evaluated within a partition containing only that specific element.

## Example 1 - calculated column

The following DAX query:

```dax
EVALUATE
ADDCOLUMNS(
    'DimGeography',
    "UniqueRank",
    ROWNUMBER(
    	'DimGeography',
    	ORDERBY(
    		'DimGeography'[StateProvinceName], desc,
    		'DimGeography'[City], asc),
    	PARTITIONBY(
    		'DimGeography'[EnglishCountryRegionName])))
ORDER BY [EnglishCountryRegionName] asc, [StateProvinceName] desc, [City] asc
```

Returns a table that uniquely ranks each geography with the same EnglishCountryRegionName, by their StateProvinceName and City.

## Example 2 - visual calculation

The following visual calculation DAX queries:

```dax
SalesRankWithinYear = ROWNUMBER(ORDERBY([SalesAmount], DESC), PARTITIONBY([CalendarYear]))

SalesRankAllHistory = ROWNUMBER(ORDERBY([SalesAmount], DESC))
```

Create two columns that uniquely rank each month by the total sales, both within each year, and the entire history.

The screenshot below shows the visual matrix and the first visual calculation expression:

![DAX visual calculation](media/dax-queries/dax-visualcalc-rownumber.png)

## Related content

[INDEX](index-function-dax.md)
[ORDERBY](orderby-function-dax.md)
[PARTITIONBY](partitionby-function-dax.md)
[WINDOW](window-function-dax.md)
[RANK](rank-function-dax.md)
