---
description: "Learn more about: COLUMNSTATISTICS"
title: "COLUMNSTATISTICS function (DAX)"
ms.custom: sfi-image-nochange
---
# COLUMNSTATISTICS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table of statistics regarding every column in every table in the model.

## Syntax

```dax
COLUMNSTATISTICS ()
```

### Parameters

This function does not take any parameters.

## Return value

A table of statistics. Each row of this table represents a different column in the model. Table columns include:

- `Table Name`: The current column’s table.
- `Column Name`: The current column’s name.
- `Min`: The minimum value found within the current column.
- `Max`: The maximum value found within the current column.
- `Cardinality`: The number of distinct values found within the current column.
- `Max Length`: The length of the longest string found within the current column (only applicable for string columns).

## Remarks

- Columns in an error state and columns from query-scope calculated tables do not appear in the result table.

- If a filter from the filter context is applied to COLUMNSTATISTICS(), an error is returned.

- For binary-typed columns, the Min and Max statistics will have BLANK values.

## Example

[!INCLUDE [power-bi-dax-sample-model](includes/power-bi-dax-sample-model.md)]

The following DAX query:

```dax
DEFINE
    TABLE FilteredProduct =
        FILTER (
            Product,
            [Color] == "Blue"
        )
    COLUMN Customer[Location] = [State-Province] & " " & [Country-Region]

EVALUATE
COLUMNSTATISTICS ()

```

Returns a table with statistics regarding all columns from all tables in the model. The table also includes statistics for the query-scope calculated column, Customer[Location]. However, the table does not include the columns from the query-scope calculated table, FilteredProduct.

:::image type="content" source="media/columnstatistics-function-dax/columnstatistics-result-table.png" alt-text="COLUMNSTATISTICS result table":::

## Related content

[Filter context](dax-overview.md#filter-context)
[CALCULATETABLE function](calculatetable-function-dax.md)
