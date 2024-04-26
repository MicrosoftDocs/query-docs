---
description: "Learn more about: Filter functions"
title: "Filter functions (DAX) | Microsoft Docs"
---
# Filter functions

The filter and value functions in DAX are some of the most complex and powerful, and differ greatly from Excel functions. The lookup functions work by using tables and relationships, like a database. The filtering functions let you manipulate data context to create dynamic calculations.  
  
## In this category

|Function  |Description  |
|---------|---------|
|[ALL](all-function-dax.md)      |  Returns all the rows in a table, or all the values in a column, ignoring any filters that might have been applied.       |
|[ALLCROSSFILTERED](allcrossfiltered-function-dax.md)     |  Clear all filters which are applied to a table.       |
|[ALLEXCEPT](allexcept-function-dax.md)     |  Removes all context filters in the table except filters that have been applied to the specified columns.        |
|[ALLNOBLANKROW](allnoblankrow-function-dax.md)     |  From the parent table of a relationship, returns all rows but the blank row, or all distinct values of a column but the blank row, and disregards any context filters that might exist.         |
|[ALLSELECTED](allselected-function-dax.md)      |  Removes context filters from columns and rows in the current query, while retaining all other context filters or explicit filters.        |
|[CALCULATE](calculate-function-dax.md)      |  Evaluates an expression in a modified filter context.      |
|[CALCULATETABLE](calculatetable-function-dax.md)     |  Evaluates a table expression in a modified filter context.         |
|[EARLIER](earlier-function-dax.md)     |  Returns the current value of the specified column in an outer evaluation pass of the mentioned column.         |
|[EARLIEST](earliest-function-dax.md)     |  Returns the current value of the specified column in an outer evaluation pass of the specified column.         |
|[FILTER](filter-function-dax.md)      |  Returns a table that represents a subset of another table or expression.        |
|[FIRST](first-function-dax.md)      |  Used in visual calculations only. Retrieves a value in the visual matrix from the first row of an axis.       |
|[INDEX](index-function-dax.md)|Returns a row at an absolute position, specified by the position parameter, within the specified partition, sorted by the specified order or on the specified axis.|
|[KEEPFILTERS](keepfilters-function-dax.md)      | Modifies how filters are applied while evaluating a CALCULATE or CALCULATETABLE function.         |
|[LAST](last-function-dax.md)    | Used in visual calculations only. Retrieves a value in the visual matrix from the last row of an axis.        |
|[LOOKUP](lookup-function-dax.md)              | In visual calculation mode only. Look up the value when filters applied.|
|[LOOKUPVALUE](lookupvalue-function-dax.md)    | Returns the value for the row that meets all criteria specified by search conditions. The function can apply one or more search conditions.        |
|[MATCHBY](matchby-function-dax.md)    | In window functions, defines the columns that are used to determine how to match data and identify the *current row*.        |
|[MOVINGAVERAGE](movingaverage-function-dax.md)|Returns a moving average calculated along the given axis of the visual matrix.|
|[NEXT](next-function-dax.md)    | Used in visual calculations only. Retrieves a value in the next row of an axis in the visual matrix.        |
|[OFFSET](offset-function-dax.md)|Returns a single row that is positioned either before or after the *current row* within the same table, by a given offset. |
|[ORDERBY](orderby-function-dax.md)|Defines the columns that determine the sort order within each of a window function’s partitions.|
|[PARTITIONBY](partitionby-function-dax.md)|Defines the columns that are used to partition a window function’s \<relation> parameter.|
|[PREVIOUS](previous-function-dax.md)| Used in visual calculations only. Retrieves a value in the previous row of an axis in the visual matrix. |
|[RANGE](range-function-dax.md)|Returns an interval of rows within the given axis, relative to the current row. A shortcut for WINDOW.|
|[RANK](rank-function-dax.md)| Returns the ranking of a row within the given interval.  |
|[REMOVEFILTERS](removefilters-function-dax.md)|Clears filters from the specified tables or columns.|
|[ROWNUMBER](rownumber-function-dax.md)| Returns the unique ranking of a row within the given interval.  |
|[RUNNINGSUM](runningsum-function-dax.md)|Returns a running sum calculated along the given axis of the visual matrix.|
|[SELECTEDVALUE](selectedvalue-function-dax.md)     |  Returns the value when the context for columnName has been filtered down to one distinct value only. Otherwise returns alternateResult.         |
|[WINDOW](window-function-dax.md)| Returns multiple rows which are positioned within the given interval.  |
