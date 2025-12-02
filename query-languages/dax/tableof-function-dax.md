---
description: "Learn more about: TABLEOF"
title: "TABLEOF function (DAX)"
---
# TABLEOF

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns a reference to the table associated with a specified column, measure, or calendar.

## Syntax

```dax
TABLEOF(<myColumnRef>)
TABLEOF(<measureName>)
TABLEOF(<calendar>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`reference`|A column, measure, or calendar reference.|

## Return value

A table reference.

## Remarks

- The `TABLEOF` function returns a table reference, not the table data itself.
- When passed a column name, it returns the table that contains that column.
- When passed a measure name, it returns the table where that measure is defined.
- When passed a calendar reference, it returns the table associated with that calendar.
- This function is useful in scenarios where you need to dynamically determine which table a column or measure belongs to.
- `TABLEOF` does not resolve columns from row context; it only resolves columns from the current filter context (base table).
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example 1 - Using TABLEOF with a column
```dax
EVALUATE
ROW ( "RowCount", COUNTROWS ( TABLEOF ( 'Customer'[Customer ID] ) ) )
```

Returns:

| **RowCount** |
| ------------- |
| 18485 |

## Example 2 - Using TABLEOF with a measure
```dax
DEFINE
    MEASURE Sales[Projected Sales] =
        SUM ( 'Sales'[Sales Amount] ) * 1.06

EVALUATE
ROW (
    "Total Projected Sales", ROUND ( SUMX ( TABLEOF ( [Projected Sales] ), [Projected Sales] ), 2 )
)
```

Returns:

| **Total Projected Sales** |
| ------------- |
| 116397830.65 |

## Example 3 - Using TABLEOF in a user-defined function
```dax
DEFINE
    FUNCTION GetTableRowCount = (
            columnRef : ANYREF
        ) =>
        COUNTROWS ( TABLEOF ( columnRef ) )

EVALUATE
ROW (
    "ResellerCount", GetTableRowCount ( 'Reseller'[Reseller ID] ),
    "CustomerCount", GetTableRowCount ( 'Customer'[Customer ID] )
)
```

Returns:

| **ResellerCount** | **CustomerCount** |
| ------------- | ------------- |
| 702 | 18485 |

## Related content
- [Information functions](information-functions-dax.md)
