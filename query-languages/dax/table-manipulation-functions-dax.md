---
description: "Learn more about: Table manipulation functions"
title: "Table manipulation functions (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 08/26/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false
---
# Table manipulation functions

These functions return a table or manipulate existing tables.

## In this category

|Function  |Description  |
|---------|---------|
|[ADDCOLUMNS](addcolumns-function-dax.md)      |     Adds calculated columns to the given table or table expression.          |
|[ADDMISSINGITEMS](addmissingitems-function-dax.md)       |     Adds combinations of items from multiple columns to a table if they do not already exist.    |
|[CROSSJOIN](crossjoin-function-dax.md)      |  Returns a table that contains the Cartesian product of all rows from all tables in the arguments.      |
|[CURRENTGROUP](currentgroup-function-dax.md)      |  Returns a set of rows from the table argument of a GROUPBY expression.      |
|[DATATABLE](datatable-function.md)    |  Provides a mechanism for declaring an inline set of data values.        |
|[DETAILROWS](detailrows-function-dax.md)    |  Evaluates a Detail Rows Expression defined for a measure and returns the data.        |
|[DISTINCT column](distinct-function-dax.md)      |  Returns a one-column table that contains the distinct values from the specified column.       |
|[DISTINCT table](distinct-table-function-dax.md)      |  Returns a table by removing duplicate rows from another table or expression.       |
|[EXCEPT](except-function-dax.md)     |  Returns the rows of one table which do not appear in another table.       |
|[FILTERS](filters-function-dax.md)     |  Returns a table of values directly applied as filters to *columnName*.        |
|[GENERATE](generate-function-dax.md)      |  Returns a table with the Cartesian product between each row in *table1* and the table that results from evaluating *table2* in the context of the current row from *table1*.       |
|[GENERATEALL](generateall-function-dax.md)     |  Returns a table with the Cartesian product between each row in *table1* and the table that results from evaluating *table2* in the context of the current row from *table1*.         |
|[GENERATESERIES](generateseries-function.md)     | Returns a single column table containing the values of an arithmetic series.        |
|[GROUPBY](groupby-function-dax.md)      |  Similar to the SUMMARIZE function, GROUPBY does not do an implicit CALCULATE for any extension columns that it adds.       |
|[IGNORE](ignore-function-dax.md)      |   Modifies SUMMARIZECOLUMNS by omitting specific expressions from the BLANK/NULL evaluation.      |
|[INTERSECT](intersect-function-dax.md)       |   Returns the row intersection of two tables, retaining duplicates.       |
|[NATURALINNERJOIN](naturalinnerjoin-function-dax.md)     |  Performs an inner join of a table with another table.        |
|[NATURALLEFTOUTERJOIN](naturalleftouterjoin-function-dax.md)     |  Performs a join of the LeftTable with the RightTable.       |
|[ROLLUP](rollup-function-dax.md)    |  Modifies the behavior of SUMMARIZE by adding rollup rows to the result on columns defined by the groupBy_columnName parameter.     |
|[ROLLUPADDISSUBTOTAL](rollupaddissubtotal-function-dax.md)    | Modifies the behavior of SUMMARIZECOLUMNS by adding rollup/subtotal rows to the result based on the groupBy_columnName columns.        |
|[ROLLUPISSUBTOTAL](rollupissubtotal-function-dax.md)    |  Pairs rollup groups with the column added by ROLLUPADDISSUBTOTAL within an ADDMISSINGITEMS expression.      |
|[ROLLUPGROUP](rollupgroup-function-dax.md)    |   Modifies the behavior of SUMMARIZE and SUMMARIZECOLUMNS by adding rollup rows to the result on columns defined by the the groupBy_columnName parameter.       |
|[ROW](row-function-dax.md)     |  Returns a table with a single row containing values that result from the expressions given to each column.         |
|[SELECTCOLUMNS](selectcolumns-function-dax.md)    |  Adds calculated columns to the given table or table expression.         |
|[SUBSTITUTEWITHINDEX](substitutewithindex-function-dax.md)      |  Returns a table which represents a left semijoin of the two tables supplied as arguments.        |
|[SUMMARIZE](summarize-function-dax.md)      | Returns a summary table for the requested totals over a set of groups.          |
|[SUMMARIZECOLUMNS](summarizecolumns-function-dax.md)      |  Returns a summary table over a set of groups.        |
|[Table Constructor](table-Constructor.md)    |  Returns a table of one or more columns.       |
|[TOPN](topn-function-dax.md)     |  Returns the top N rows of the specified table.       |
|[TREATAS](treatas-function.md)     |  Applies the result of a table expression as filters to columns from an unrelated table.        |
|[UNION](union-function-dax.md)     |  Creates a union (join) table from a pair of tables.         |
|[VALUES](values-function-dax.md)     |  Returns a one-column table that contains the distinct values from the specified table or column.       |
