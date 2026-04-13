---
description: "Learn more about: NAMEOF"
title: "NAMEOF function (DAX)"
---

# NAMEOF

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the name of a table, column, measure, or calendar as a text string. Optional parameters control which component of the name is returned and how the result is escaped.

## Syntax

```dax
NAMEOF ( <object> [, <component> [, <escaped>]] )
```

### Parameters

|Term|Definition|
|--------|--------------|
|`object`|The table, column, measure, or calendar whose name you want to retrieve.|
|`component`|(Optional) An enumeration that specifies which part of the qualified name to return. If omitted, defaults to `FULL`. See [Component values](#component-values).|
|`escaped`|(Optional) An enumeration that specifies how the returned name is escaped. If omitted, defaults to `ESCAPED`. See [Escaped values](#escaped-values).|

#### Component values

The `component` parameter accepts the following values:

|Value|Description|
|--------|--------------|
|`TABLE`|Returns the table name. Returns an error if the object is not associated with a table (e.g., a calendar).|
|`COLUMN`|Returns the column name. Returns an error if the object is not a column.|
|`MEASURE`|Returns the measure name. Returns an error if the object is not a measure.|
|`CALENDAR`|Returns the calendar name. Returns an error if the object is not a calendar.|
|`FULL`|(Default) Returns the fully qualified name of the object.|
|`SELF`|Returns the name of the object itself: the column or measure name for columns and measures, or the table/calendar name for tables and calendars.|
|`PARENT`|Returns the parent table name for columns and measures. Returns an error for tables and calendars.|

#### Escaped values

The `escaped` parameter accepts the following values:

|Value|Description|
|--------|--------------|
|`ESCAPED`|(Default) Returns the name with full DAX escaping: table names wrapped in single quotes, column and measure names wrapped in square brackets.|
|`UNESCAPED`|Returns the raw name without any delimiters or escape characters. Returns an error for fully qualified names that contain both a parent and child component.|
|`MINIMALLYESCAPED`|Returns the name with escaping applied only when the name requires it. Names that contain only simple letters, digits, and underscores are returned without delimiters. Names that contain spaces or special characters are returned with escaping.|

## Return value

A text string with the requested name, formatted based on the component and escaped parameters.

## Remarks

- When called with only the `object` argument, NAMEOF behaves the same as in previous versions, returning a fully qualified, escaped name. Because `component` defaults to `FULL` and `escaped` defaults to `ESCAPED`, the return formats are:
  - For tables: `'TableName'`.
  - For columns: `'TableName'[ColumnName]`.
  - For measures: `'TableName'[MeasureName]`.
  - For calendars: `'CalendarName'`.
  - For variation columns: `'TableName'[ColumnName].[VariationName]`.
- Variables and dynamic expressions are not supported as arguments to NAMEOF.
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

### Component behavior by input type

The following table shows the result of each `component` value for different input types, using the default `ESCAPED` mode. "Error" indicates that the combination returns an error.

| Input type | `TABLE` | `COLUMN` | `MEASURE` | `CALENDAR` | `FULL` | `SELF` | `PARENT` |
|---|---|---|---|---|---|---|---|
| Column - `Sales[Sales Amount]` | `'Sales'` | `[Sales Amount]` | Error | Error | `'Sales'[Sales Amount]` | `[Sales Amount]` | `'Sales'` |
| Table - `Sales` | `'Sales'` | Error | Error | Error | `'Sales'` | `'Sales'` | Error |
| Measure - `Sales[m1]` | `'Sales'` | Error | `[m1]` | Error | `'Sales'[m1]` | `[m1]` | `'Sales'` |
| Calendar - `myCalendar` | Error | Error | Error | `'myCalendar'` | `'myCalendar'` | `'myCalendar'` | Error |

### Escaped behavior

The `escaped` parameter controls how the name produced by the `component` step is formatted. The following table uses the fully escaped name as a reference and shows the output for each `escaped` value.

| Fully escaped name | `ESCAPED` | `UNESCAPED` | `MINIMALLYESCAPED` |
|---|---|---|---|
| `'Sales'` | `'Sales'` | `Sales` | `Sales` |
| `'Sales'[Sales Amount]` | `'Sales'[Sales Amount]` | Error | `Sales[Sales Amount]` |
| `'Sales'[m1]` | `'Sales'[m1]` | Error | `Sales[m1]` |
| `[Amount]` | `[Amount]` | `Amount` | `Amount` |
| `'Sales Region'` | `'Sales Region'` | `Sales Region` | `'Sales Region'` |
| `'Sales Region'[Column]` | `'Sales Region'[Column]` | Error | `'Sales Region'[Column]` |
| `[Order Quantity]` | `[Order Quantity]` | `Order Quantity` | `[Order Quantity]` |

> [!NOTE]
> `UNESCAPED` returns an error for fully qualified names (names that include both a table and column/measure component), because the result would be ambiguous without delimiters.

#### Special character escaping rules

The following escaping rules apply within DAX name delimiters:

- **Table names (single-quote delimited):** A literal single quote (`'`) in a table name is escaped as two single quotes (`''`).
- **Column and measure names (bracket delimited):** A literal closing bracket (`]`) in a column or measure name is escaped as `]]`. An opening bracket (`[`) does not require escaping.


| Fully escaped name | `ESCAPED` | `UNESCAPED` | `MINIMALLYESCAPED` |
|---|---|---|---|
| `'Ta''''ble'` (table with `'` in name) | `'Ta''''ble'` | `Ta''ble` | `Ta''ble` |
| `[colu[]]mn]` (column with `]` in name) | `[colu[]]mn]` | `colu[]mn` | `[colu[]]mn]` |

## Example 1

The following DAX query returns the fully qualified name of a column:

```dax
EVALUATE
{ NAMEOF ( 'Sales'[ORDER QUANTITY] ) }
```

Returns:

| **[Value]** |
| ------------- |
| 'Sales'[Order Quantity] |

## Example 2

The following DAX query returns the fully qualified name of a measure:

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

## Example 3

The following DAX query uses the `component` parameter to extract only the table name from a column reference:

```dax
EVALUATE
{ NAMEOF ( 'Sales'[Sales Amount], TABLE ) }
```

Returns:

| **[Value]** |
| ------------- |
| 'Sales' |

## Example 4

The following DAX query returns an unescaped table name:

```dax
EVALUATE
{ NAMEOF ( 'Sales', FULL, UNESCAPED ) }
```

Returns:

| **[Value]** |
| ------------- |
| Sales |

## Example 5

The following DAX query uses the `component` and `escaped` parameters to return the minimally escaped parent table name of a column:

```dax
EVALUATE
{ NAMEOF ( 'Sales'[Sales Amount], PARENT, MINIMALLYESCAPED ) }
```

Returns:

| **[Value]** |
| ------------- |
| Sales |

## Related content
- [Information functions](information-functions-dax.md)