---
description: "Learn more about: NAMEOF"
title: "NAMEOF function (DAX)"
---

# NAMEOF

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the name of a table, column, measure, or calendar as a text string.

## Syntax

```dax
NAMEOF ( <object> )
```

### Parameters

|Term|Definition|
|--------|--------------|
|`object`|The table, column, measure, or calendar whose name you want to retrieve.|

## Return value

A text string containing the qualified name of the object.

## Remarks

- For tables, returns the name in the format `'TableName'`.
- For columns, returns the name in the format `'TableName'[ColumnName]`.
- For measures, returns the name in the format `'TableName'[MeasureName]`.
- For calendars, returns the name in the format `'CalendarName'`.
- For variation columns, returns the name in the format `'TableName'[ColumnName].[VariationName]`.
- Variables and dynamic expressions are not supported as arguments to NAMEOF.
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]


## Example 1

The following DAX query returns the qualified name of a column:

```dax
EVALUATE
{ NAMEOF ( 'Sales'[ORDER QUANTITY] ) }
```

Returns:

| **[Value]** |
| ------------- |
| 'Sales'[Order Quantity] |

## Example 2

The following DAX query returns the qualified name of a measure:

```dax
DEFINE
    MEASURE Sales[Projected Sales] =
        SUM ( 'Sales'[Sales Amount] ) * 1.06

EVALUATE
{ NAMEOF ( [Projected Sales] ) }
```

Returns:

| **[Value]** |
| ------------- |
| 'Sales'[Projected Sales] |
