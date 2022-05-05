---
description: "Learn more about: Table functions"
title: "Table functions | Microsoft Docs"
ms.date: 5/4/2022
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table functions

These functions create and manipulate table values.

## Table construction

|Function|Description|
|------------|---------------|
|[ItemExpression.From](itemexpression-from.md) | Returns the abstract syntax tree (AST) for the body of a function.|
|[ItemExpression.Item](itemexpression-item.md) | An abstract syntax tree (AST) node representing the item in an item expression.|
|[RowExpression.Column](rowexpression-column.md)|Returns an abstract syntax tree (AST) that represents access to a column within a row expression.|
|[RowExpression.From](rowexpression-from.md)|Returns the abstract syntax tree (AST) for the body of a function.|
|[RowExpression.Row](rowexpression-row.md)|An abstract syntax tree (AST) node representing the row in a row expression.|
|[Table.FromColumns](table-fromcolumns.md)|Returns a table from a list containing nested lists with the column names and values.|
|[Table.FromList](table-fromlist.md)|Converts a list into a table by applying the specified splitting function to each item in the list.|
|[Table.FromRecords](table-fromrecords.md)|Returns a table from a list of records.|
|[Table.FromRows](table-fromrows.md)|Creates a table from the list where each element of the list is a list that contains the column values for a single row.|
|[Table.FromValue](table-fromvalue.md)|Returns a table with a column containing the provided value or list of values.|
|[Table.FuzzyGroup](table-fuzzygroup.md)|Groups the rows of a table by fuzzily matching values in the specified column for each row.|
|[Table.FuzzyJoin](table-fuzzyjoin.md)|Joins the rows from the two tables that fuzzy match based on the given keys.|
|[Table.FuzzyNestedJoin](table-fuzzynestedjoin.md)|Performs a fuzzy join between tables on supplied columns and produces the join result in a new column.|
|[Table.Split](table-split.md)|Splits the specified table into a list of tables using the specified page size.|
|[Table.View](table-view.md)|Creates or extends a table with user-defined handlers for query and action operations.|
|[Table.ViewFunction](table-viewfunction.md) | Creates a function that can be intercepted by a handler defined on a view (via `Table.View`).|

## Conversions

|Function|Description|
|------------|---------------|
|[Table.ToColumns](table-tocolumns.md)|Returns a list of nested lists each representing a column of values in the input table.|
|[Table.ToList](table-tolist.md)|Returns a table into a list by applying the specified combining function to each row of values in a table.|
|[Table.ToRecords](table-torecords.md)|Returns a list of records from an input table.|
|[Table.ToRows](table-torows.md)|Returns a nested list of row values from an input table.|

## Information

|Function|Description|
|------------|---------------|
|[Table.ApproximateRowCount](table-approximaterowcount.md)|Returns the approximate number of rows in the table.|
|[Table.ColumnCount](table-columncount.md)|Returns the number of columns in a table.|
|[Table.IsEmpty](table-isempty.md)|Returns true if the table does not contain any rows.|
|[Table.Profile](table-profile.md)|Returns a profile of the columns of a table.|
|[Table.RowCount](table-rowcount.md)|Returns the number of rows in a table.|
|[Table.Schema](table-schema.md)|Returns a table containing a description of the columns (i.e. the schema) of the specified table.|
|[Tables.GetRelationships](tables-getrelationships.md)|Returns the relationships among a set of tables. |

## Row operations

|Function|Description|
|------------|---------------|
|[Table.AlternateRows](table-alternaterows.md)|Returns a table containing an alternating pattern of the rows from a table.|
|[Table.Combine](table-combine.md)|Returns a table that is the result of merging a list of tables. The tables must all have the same row type structure.|
|[Table.FindText](table-findtext.md)|Returns a table containing only the rows that have the specified text within one of their cells or any part thereof.|
|[Table.First](table-first.md)|Returns the first row from a table.|
|[Table.FirstN](table-firstn.md)|Returns the first row(s) of a table, depending on the countOrCondition parameter.|
|[Table.FirstValue](table-firstvalue.md)|Returns the first column of the first row of the table or a specified default value.|
|[Table.FromPartitions](table-frompartitions.md)|Returns a table that is the result of combining a set of partitioned tables into new columns. The type of the column can optionally be specified, the default is any.|
|[Table.InsertRows](table-insertrows.md)|Returns a table with the list of rows inserted into the table at an index. Each row to insert must match the row type of the table..|
|[Table.Last](table-last.md)|Returns the last row of a table.|
|[Table.LastN](table-lastn.md)|Returns the last row(s) from a table, depending on the countOrCondition parameter.|
|[Table.MatchesAllRows](table-matchesallrows.md)|Returns true if all of the rows in a table meet a condition.|
|[Table.MatchesAnyRows](table-matchesanyrows.md)|Returns true if any of the rows in a table meet a condition.|
|[Table.Partition](table-partition.md)|Partitions the table into a list of groups number of tables, based on the value of the column of each row and a hash function. The hash function is applied to the value of the column of a row to obtain a hash value for the row. The hash value modulo groups determines in which of the returned tables the row will be placed.|
|[Table.PartitionValues](table-partitionvalues.md)|Returns information about how a table is partitioned.|
|[Table.Range](table-range.md)|Returns the specified number of rows from a table starting at an offset.|
|[Table.RemoveFirstN](table-removefirstn.md)|Returns a table with the specified number of rows removed from the table starting at the first row. The number of rows removed depends on the optional countOrCondition parameter.|
|[Table.RemoveLastN](table-removelastn.md)|Returns a table with the specified number of rows removed from the table starting at the last row. The number of rows removed depends on the optional countOrCondition parameter.|
|[Table.RemoveRows](table-removerows.md)|Returns a table with the specified number of rows removed from the table starting at an offset.|
|[Table.RemoveRowsWithErrors](table-removerowswitherrors.md)|Returns a table with all rows removed from the table that contain an error in at least one of the cells in a row.|
|[Table.Repeat](table-repeat.md)|Returns a table containing the rows of the table repeated the count number of times.|
|[Table.ReplaceRows](table-replacerows.md)|Returns a table where the rows beginning at an offset and continuing for count are replaced with the provided rows.|
|[Table.ReverseRows](table-reverserows.md)|Returns a table with the rows in reverse order.|
|[Table.SelectRows](table-selectrows.md)|Returns a table containing only the rows that match a condition.|
|[Table.SelectRowsWithErrors](table-selectrowswitherrors.md)|Returns a table with only the rows from table that contain an error in at least one of the cells in a row.|
|[Table.SingleRow](table-singlerow.md)|Returns a single row from a table.|
|[Table.Skip](table-skip.md)|Returns a table that does not contain the first row or rows of the table.|
|[Table.SplitAt](table-splitat.md)|Returns a list containing the first count rows specified and the remaining rows.|

## Column operations

|Function|Description|
|------------|---------------|
|[Table.Column](table-column.md)|Returns the values from a column in a table.|
|[Table.ColumnNames](table-columnnames.md)|Returns the names of columns from a table.|
|[Table.ColumnsOfType](table-columnsoftype.md)|Returns a list with the names of the columns that match the specified types.|
|[Table.DemoteHeaders](table-demoteheaders.md)|Demotes the header row down into the first row of a table.|
|[Table.DuplicateColumn](table-duplicatecolumn.md) | Duplicates a column with the specified name. Values and type are copied from the source column.|
|[Table.HasColumns](table-hascolumns.md)|Returns true if a table has the specified column or columns.|
|[Table.Pivot](table-pivot.md)|Given a table and attribute column containing pivotValues, creates new columns for each of the pivot values and assigns them values from the valueColumn. An optional aggregationFunction can be provided to handle multiple occurrence of the same key value in the attribute column.|
|[Table.PrefixColumns](table-prefixcolumns.md)|Returns a table where the columns have all been prefixed with a text value.|
|[Table.PromoteHeaders](table-promoteheaders.md)|Promotes the first row of the table into its header or column names.|
|[Table.RemoveColumns](table-removecolumns.md)|Returns a table without a specific column or columns.|
|[Table.ReorderColumns](table-reordercolumns.md)|Returns a table with specific columns in an order relative to one another.|
|[Table.RenameColumns](table-renamecolumns.md)|Returns a table with the columns renamed as specified.|
|[Table.SelectColumns](table-selectcolumns.md)|Returns a table that contains only specific columns.|
|[Table.TransformColumnNames](table-transformcolumnnames.md)|Transforms column names by using the given function.|
|[Table.Unpivot](table-unpivot.md)|Given a list of table columns, transforms those columns into attribute-value pairs.|
|[Table.UnpivotOtherColumns](table-unpivotothercolumns.md)|Translates all columns other than a specified set into attribute-value pairs, combined with the rest of the values in each row.|

## Transformation

|Function|Description|
|------------|---------------|
|[Table.AddColumn](table-addcolumn.md)|Adds a column named newColumnName to a table.|
|[Table.AddFuzzyClusterColumn](table-addfuzzyclustercolumn.md)| Adds a new column with representative values obtained by fuzzy grouping values of the specified column in the table.|
|[Table.AddIndexColumn](table-addindexcolumn.md)|Returns a table with a new column with a specific name that, for each row, contains an index of the row in the table.|
|[Table.AddJoinColumn](table-addjoincolumn.md)|Performs a nested join between table1 and table2 from specific columns and produces the join result as a newColumnName column for each row of table1.|
|[Table.AddKey](table-addkey.md)|Add a key to table.|
|[Table.AggregateTableColumn](table-aggregatetablecolumn.md)|Aggregates tables nested in a specific column into multiple columns containing aggregate values for those tables.|
|[Table.CombineColumns](table-combinecolumns.md)|Table.CombineColumns merges columns using a combiner function to produce a new column. Table.CombineColumns is the inverse of Table.SplitColumns.|
|[Table.CombineColumnsToRecord](table-combinecolumnstorecord.md)|Combines the specified columns into a new record-valued column where each record has field names and values corresponding to the column names and values of the columns that were combined.|
|[Table.ConformToPageReader](table-conformtopagereader.md)|This function is intended for internal use only.|
|[Table.ExpandListColumn](table-expandlistcolumn.md)|Given a column of lists in a table, create a copy of a row for each value in its list.|
|[Table.ExpandRecordColumn](table-expandrecordcolumn.md)|Expands a column of records into columns with each of the values.|
|[Table.ExpandTableColumn](table-expandtablecolumn.md)|Expands a column of records or a column of tables into multiple columns in the containing table.|
|[Table.FillDown](table-filldown.md)|Replaces null values in the specified column or columns of the table with the most recent non-null value in the column.|
|[Table.FillUp](table-fillup.md)|Returns a table from the table specified where the value of the next cell is propagated to the null values cells above in the column specified.|
|[Table.FilterWithDataTable](table-filterwithdatatable.md)|This function is intended for internal use only.|
|[Table.Group](table-group.md)|Groups table rows by the values of key columns for each row.|
|[Table.Join](table-join.md)|Joins the rows of table1 with the rows of table2 based on the equality of the values of the key columns selected by table1, key1 and table2, key2.|
|[Table.Keys](table-keys.md)|Returns a list of key column names from a table.|
|[Table.NestedJoin](table-nestedjoin.md)|Joins the rows of the tables based on the equality of the keys. The results are entered into a new column.|
|[Table.ReplaceErrorValues](table-replaceerrorvalues.md)|Replaces the error values in the specified columns with the corresponding specified value.|
|[Table.ReplaceKeys](table-replacekeys.md)|Returns a new table with new key information set in the keys argument.|
|[Table.ReplaceRelationshipIdentity](table-replacerelationshipidentity.md)|This function is intended for internal use only.|
|[Table.ReplaceValue](table-replacevalue.md)|Replaces oldValue with newValue in specific columns of a table, using the provided replacer function, such as text.Replace or Value.Replace.|
|[Table.SplitColumn](table-splitcolumn.md)|Returns a new set of columns from a single column applying a splitter function to each value.|
|[Table.TransformColumns](table-transformcolumns.md)|Transforms columns from a table using a function.|
|[Table.TransformColumnTypes](table-transformcolumntypes.md)|Transforms the column types from a table using a type.|
|[Table.TransformRows](table-transformrows.md)|Transforms the rows from a table using a transform function.|
|[Table.Transpose](table-transpose.md)|Returns a table with columns converted to rows and rows converted to columns from the input table.|

## Membership

|Function|Description|
|------------|---------------|
|[Table.Contains](table-contains.md)|Determines whether the a record appears as a row in the table.|
|[Table.ContainsAll](table-containsall.md)|Determines whether all of the specified records appear as rows in the table.|
|[Table.ContainsAny](table-containsany.md)|Determines whether any of the specified records appear as rows in the table.|
|[Table.Distinct](table-distinct.md)|Removes duplicate rows from a table, ensuring that all remaining rows are distinct.|
|[Table.IsDistinct](table-isdistinct.md)|Determines whether a table contains only distinct rows.|
|[Table.PositionOf](table-positionof.md)|Determines the position or positions of a row within a table.|
|[Table.PositionOfAny](table-positionofany.md)|Determines the position or positions of any of the specified rows within the table.|
|[Table.RemoveMatchingRows](table-removematchingrows.md)|Removes all occurrences of rows from a table.|
|[Table.ReplaceMatchingRows](table-replacematchingrows.md)|Replaces specific rows from a table with the new rows.|

## Ordering

|Function|Description|
|------------|---------------|
|[Table.Max](table-max.md)|Returns the largest row or rows from a table using a comparisonCriteria.|
|[Table.MaxN](table-maxn.md)|Returns the largest N rows from a table. After the rows are sorted, the countOrCondition parameter must be specified to further filter the result.|
|[Table.Min](table-min.md)|Returns the smallest row or rows from a table using a comparisonCriteria.|
|[Table.MinN](table-minn.md)|Returns the smallest N rows in the given table. After the rows are sorted, the countOrCondition parameter must be specified to further filter the result.|
|[Table.Sort](table-sort.md)|Sorts the rows in a table using a comparisonCriteria or a default ordering if one is not specified.|

## Other

|Function|Description|
|------------|---------------|
|[Table.Buffer](table-buffer.md)|Buffers a table into memory, isolating it from external changes during evaluation.|

## Parameter Values

### Naming output columns

This parameter is a list of text values specifying the column names of the resulting table. This parameter is generally used in the Table construction functions, such as [Table.FromRows](table-fromrows.md) and [Table.FromList](table-fromlist.md).

### Comparison criteria

Comparison criterion can be provided as either of the following values:

- A number value to specify a sort order. More information: [Sort order](#sort-order)

- To compute a key to be used for sorting, a function of one argument can be used.

- To both select a key and control order, comparison criterion can be a list containing the key and order.

- To completely control the comparison, a function of two arguments can be used that returns -1, 0, or 1 given the relationship between the left and right inputs. [Value.Compare](value-compare.md) can be used to delegate this logic.

For examples, go to the description of [Table.Sort](table-sort.md).

### Count or Condition criteria

This criteria is generally used in ordering or row operations. It determines the number of rows returned in the table and can take two forms, a number or a condition.

- A number indicates how many values to return inline with the appropriate function.

- If a condition is specified, the rows containing values that initially meet the condition is returned. Once a value fails the condition, no further values are considered.

More information: [Table.FirstN](table-firstn.md), [Table.MaxN](table-maxn.md)

### Handling of extra values

Extra values are used to indicate how the function should handle extra values in a row. This parameter is specified as a number, which maps to the following options:

`ExtraValues.List = 0`
`ExtraValues.Error = 1`
`ExtraValues.Ignore = 2`

More information: [Table.FromList](table-fromlist.md), [ExtraValues.Type](extravalues-type.md)

### Missing column handling

This parameter is used to indicate how the function should handle missing columns. This parameter is specified as a number, which maps to the following options:

`MissingField.Error = 0`
`MissingField.Ignore = 1`
`MissingField.UseNull = 2;`

This parameter is used in column or transformation operations, for examples, in [Table.TransformColumns](table-transformcolumns.md). More information: [MissingField.Type](missingfield-type.md)

### Sort Order

Sort ordering is used to indicate how the results should be sorted. This parameter is specified as a number, which maps to the following options:

`Order.Ascending = 0`
`Order.Descending = 1`

More information: [Order.Type](order-type.md)

### Equation criteria

Equation criteria for tables can be specified as either:

- A function value that is either:
  
  - A key selector that determines the column in the table to apply the equality criteria.

  - A comparer function that is used to specify the kind of comparison to apply. Built-in comparer functions can be specified. More information: [Comparer functions](comparer-functions.md)

- A list of the columns in the table to apply the equality criteria.

For examples, go to the description of [Table.Distinct](table-distinct.md).  

## See also

* [Table enumerations](table-enumerations.md)
