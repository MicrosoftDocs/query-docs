---
title: "Filter functions (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 09/04/2019
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
|[ADDMISSINGITEMS](addmissingitems-function-dax.md)       |  Adds combinations of items from multiple columns to a table if they do not already exist.       |
|[ALL](all-function-dax.md)      |  Returns all the rows in a table, or all the values in a column, ignoring any filters that might have been applied.       |
|[ALLCROSSFILTERED](allcrossfiltered-function-dax.md)     |  Clear all filters which are applied to a table.       |
|[ALLEXCEPT](allexcept-function-dax.md)     |  Removes all context filters in the table except filters that have been applied to the specified columns.        |
|[ALLNOBLANKROW](allnoblankrow-function-dax.md)     |  From the parent table of a relationship, returns all rows but the blank row, or all distinct values of a column but the blank row, and disregards any context filters that might exist.         |
|[ALLSELECTED](allselected-function-dax.md)      |  Removes context filters from columns and rows in the current query, while retaining all other context filters or explicit filters.        |
|[CALCULATE](calculate-function-dax.md)      |  Evaluates an expression in a context that is modified by the specified filters.        |
|[CALCULATETABLE](calculatetable-function-dax.md)     |  Evaluates a table expression in a context modified by the given filters.         |
|[CROSSFILTER function](crossfilter-function.md)     | Specifies the cross-filtering direction to be used in a calculation for a relationship that exists between two columns.         |
|[DISTINCT](distinct-function-dax.md)      |  Returns a one-column table that contains the distinct values from the specified column.       |
|[EARLIER](earlier-function-dax.md)      |  Returns the current value of the specified column in an outer evaluation pass of the mentioned column.       |
|[EARLIEST](earliest-function-dax.md)     |  Returns the current value of the specified column in an outer evaluation pass of the specified column.        |
|[FILTER](filter-function-dax.md)      |  Returns a table that represents a subset of another table or expression.        |
|[FILTERS](filters-function-dax.md)     |  Returns the values that are directly applied as filters to *columnName*.        |
|[HASONEFILTER](hasonefilter-function-dax.md)      |  Returns TRUE when the number of directly filtered values on *columnName* is one; otherwise returns FALSE.        |
|[HASONEVALUE](hasonevalue-function-dax.md)     |  Returns TRUE when the context for *columnName* has been filtered down to one distinct value only. Otherwise is FALSE.        |
|[ISCROSSFILTERED](iscrossfiltered-function-dax.md)      |  Returns TRUE when *columnName* or another column in the same or related table is being filtered.         |
|[ISFILTERED](isfiltered-function-dax.md)     |  Returns TRUE when *columnName* is being filtered directly.       |
|[KEEPFILTERS](keepfilters-function-dax.md)      | Modifies how filters are applied while evaluating a CALCULATE or CALCULATETABLE function.         |
|[RELATED](related-function-dax.md)     | Returns a related value from another table.        |
|[RELATEDTABLE](relatedtable-function-dax.md)      |  Evaluates a table expression in a context modified by the given filters.         |
|[REMOVEFILTERS](removefilters-function-dax.md)|Clears filters from the specified tables or columns.|
|[SELECTEDVALUE](selectedvalue-function.md)     |  Returns the value when the context for columnName has been filtered down to one distinct value only. Otherwise returns alternateResult.         |
|[SUBSTITUTEWITHINDEX](substitutewithindex-function-dax.md)      |  Returns a table which represents a left semijoin of the two tables supplied as arguments.        |
|[USERELATIONSHIP](userelationship-function-dax.md)      |   Specifies the relationship to be used in a specific calculation as the one that exists between columnName1 and columnName2.       |
|[VALUES](values-function-dax.md)     |  Returns a one-column table that contains the distinct values from the specified table or column.       |