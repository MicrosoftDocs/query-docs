---
description: "Learn more about: COLUMNSTATISTICS"
title: "COLUMNSTATISTICS function (DAX)"
ms.topic: reference
ms.date: 07/13/2026
ms.custom: sfi-image-nochange, ExampleTypeAW2020
---
# COLUMNSTATISTICS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table of statistics for every column in every table in the model.

## Syntax

```dax
COLUMNSTATISTICS ()
```

### Parameters

This function doesn't take any parameters.

## Return value

A table of statistics. Each row of this table represents a different column in the model. Table columns include:

- `Table Name`: The current column’s table.
- `Column Name`: The current column’s name.
- `Min`: The minimum value found within the current column.
- `Max`: The maximum value found within the current column.
- `Cardinality`: The number of distinct values found within the current column.
- `Max Length`: The length of the longest string found within the current column (only applicable for string columns).

## Remarks

- Columns in an error state and columns from query-scope calculated tables don't appear in the result table.

- If you apply a filter from the filter context to `COLUMNSTATISTICS()`, the function returns an error.

- For binary-typed columns, the Min and Max statistics have BLANK values.

## Example

[!INCLUDE [power-bi-dax-sample-model](includes/power-bi-dax-sample-model.md)]

The following DAX query:

```dax
DEFINE
    TABLE FilteredProduct =
        FILTER ( Product, [Color] == "Blue" )
    COLUMN Customer[Location] = [State-Province] & " " & [Country-Region]

EVALUATE
COLUMNSTATISTICS ()
```

Returns a table with statistics for all columns from all tables in the model. The table also includes statistics for the query-scope calculated column, Customer[Location]. However, the table doesn't include the columns from the query-scope calculated table, FilteredProduct.

The following excerpt shows the **Customer** table rows from the result, including the calculated **Location** column:

|Table Name|Column Name|Min|Max|Cardinality|Max Length|
|---|---|---|---|---|---|
|Customer|CustomerKey|-1|29483|18485| |
|Customer|Customer ID|[Not Applicable]|AW00029483|18485|16|
|Customer|Customer|[Not Applicable]|Zoe Watson|18401|26|
|Customer|City|[Not Applicable]|York|270|21|
|Customer|State-Province|[Not Applicable]|Yveline|54|19|
|Customer|Country-Region|[Not Applicable]|United States|7|16|
|Customer|Postal Code|[Not Applicable]|YO15|324|16|
|Customer|Location|[Not Applicable] [Not Applicable]|Yveline France|54|33|

:::image type="content" source="media/columnstatistics-function-dax/columnstatistics-result-table.png" alt-text="COLUMNSTATISTICS result table":::

## Related content

- [Filter context](dax-overview.md#filter-context)
- [CALCULATETABLE function](calculatetable-function-dax.md)
