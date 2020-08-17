---
title: "Filter functions (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 08/17/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

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
|[KEEPFILTERS](keepfilters-function-dax.md)      | Modifies how filters are applied while evaluating a CALCULATE or CALCULATETABLE function.         |
|[LOOKUPVALUE](lookupvalue-function-dax.md)    | Returns the value for the row that meets all criteria specified by search conditions. The function can apply one or more search conditions.        |
|[REMOVEFILTERS](removefilters-function-dax.md)|Clears filters from the specified tables or columns.|
|[SELECTEDVALUE](selectedvalue-function.md)     |  Returns the value when the context for columnName has been filtered down to one distinct value only. Otherwise returns alternateResult.         |
