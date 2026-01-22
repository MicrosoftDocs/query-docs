---
description: "Learn more about: ALLEXCEPT"
title: "ALLEXCEPT function (DAX)"
ms.topic: reference

---
# ALLEXCEPT

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Removes all context filters in the table except filters that have been applied to the specified columns.

## Syntax

```dax
ALLEXCEPT(<table>,<column>[,<column>[,…]])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`table`|The table over which all context filters are removed, except filters on those columns that are specified in subsequent arguments.|
|`column`|The column for which context filters must be preserved.|

The first argument to the ALLEXCEPT function must be a reference to a base table. All subsequent arguments must be references to base columns. You cannot use table expressions or column expressions with the ALLEXCEPT function.

## Return value

A table with all filters removed except for the filters on the specified columns.

## Remarks

- This function is not used by itself, but serves as an intermediate function that can be used to change the set of results over which some other calculation is performed.

- ALL and ALLEXCEPT can be used in different scenarios:

    |Function and usage|Description|
    |----------------------|---------------|
    |ALL(Table)|Removes all filters from the specified table. In effect, ALL(Table) returns all of the values in the table, removing any filters from the context that otherwise might have been applied. This function is useful when you are working with many levels of grouping, and want to create a calculation that creates a ratio of an aggregated value to the total value.|
    |ALL (Column[, Column[, …]])|Removes all filters from the specified columns in the table; all other filters on other columns in the table still apply. All column arguments must come from the same table. The ALL(Column) variant is useful when you want to remove the context filters for one or more specific columns and to keep all other context filters.|
    |ALLEXCEPT(Table, Column1 [,Column2]...)|Removes all context filters in the table except filters that are applied to the specified columns. This is a convenient shortcut for situations in which you want to remove the filters on many, but not all, columns in a table.|

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following measure formula sums SalesAmount_USD and uses the ALLEXCEPT function to remove any context filters on the DateTime table except if the filter has been applied to the CalendarYear column.

```dax
= CALCULATE(SUM(ResellerSales_USD[SalesAmount_USD]), ALLEXCEPT(DateTime, DateTime[CalendarYear]))
```

Because the formula uses ALLEXCEPT, whenever any column but CalendarYear from the table DateTime is used to slice a visualization, the formula will remove any slicer filters, providing a value equal to the sum of SalesAmount_USD. However, if the column CalendarYear is used to slice the visualization, the results are different. Because CalendarYear is specified as the argument to ALLEXCEPT, when the data is sliced on the year, a filter will be applied on years at the row level

## Related content

- [Filter functions](filter-functions-dax.md)
- [ALL function](all-function-dax.md)
- [FILTER function](filter-function-dax.md)
