---
description: "Learn more about: Table functions"
title: "Table functions"
ms.date: 6/19/2025
ms.custom: "nonautomated-date"
ms.subservice: m-source
---
# Table functions

These functions create and manipulate table values.

## Table construction

|Name|Description|
|------------|---------------|
[#table](sharptable.md) | Creates a table value from columns and rows.|
|[ItemExpression.From](itemexpression-from.md) | Returns the abstract syntax tree (AST) for the body of a function.|
|[ItemExpression.Item](itemexpression-item.md) | An abstract syntax tree (AST) node representing the item in an item expression.|
|[RowExpression.Column](rowexpression-column.md)|Returns an abstract syntax tree (AST) that represents access to a column within a row expression.|
|[RowExpression.From](rowexpression-from.md)|Returns the abstract syntax tree (AST) for the body of a function.|
|[RowExpression.Row](rowexpression-row.md)|An abstract syntax tree (AST) node representing the row in a row expression.|
|[Table.FromColumns](table-fromcolumns.md)|Creates a table from a list of columns and specified values.|
|[Table.FromList](table-fromlist.md)|Converts a list into a table by applying the specified splitting function to each item in the list.|
|[Table.FromRecords](table-fromrecords.md)|Converts a list of records into a table.|
|[Table.FromRows](table-fromrows.md)|Creates a table from a list of row values and optional columns.|
|[Table.FromValue](table-fromvalue.md)|Creates a table with a column from the provided value or values.|
|[Table.WithErrorContext](table-witherrorcontext.md) | This function is intended for internal use only.|
|[Table.View](table-view.md)|Creates or extends a table with user-defined handlers for query and action operations.|
|[Table.ViewError](table-viewerror.md) | Creates a modified error record that won't trigger a fallback when thrown by a handler defined on a view (via [Table.View](table-view.md)).|
|[Table.ViewFunction](table-viewfunction.md) | Creates a function that can be intercepted by a handler defined on a view (via [Table.View](table-view.md)).|

## Conversions

|Name|Description|
|------------|---------------|
|[Table.ToColumns](table-tocolumns.md)|Creates a list of nested lists of column values from a table.|
|[Table.ToList](table-tolist.md)|Converts a table into a list by applying the specified combining function to each row of values in the table.|
|[Table.ToRecords](table-torecords.md)|Converts a table to a list of records.|
|[Table.ToRows](table-torows.md)|Creates a list of nested lists of row values from a table.|

## Information

|Name|Description|
|------------|---------------|
|[Table.ApproximateRowCount](table-approximaterowcount.md)|Returns the approximate number of rows in the table.|
|[Table.ColumnCount](table-columncount.md)|Returns the number of columns in the table.|
|[Table.IsEmpty](table-isempty.md)|Indicates whether the table contains any rows.|
|[Table.PartitionValues](table-partitionvalues.md)|Returns information about how a table is partitioned.|
|[Table.Profile](table-profile.md)|Returns a profile of the columns of a table.|
|[Table.RowCount](table-rowcount.md)|Returns the number of rows in the table.|
|[Table.Schema](table-schema.md)|Returns a table containing a description of the columns (that is, the schema) of the specified table.|
|[Tables.GetRelationships](tables-getrelationships.md)|Gets the relationships among a set of tables.|

## Row operations

|Name|Description|
|------------|---------------|
|[Table.AlternateRows](table-alternaterows.md)|Keeps the initial offset then alternates taking and skipping the following rows.|
|[Table.Combine](table-combine.md)|Returns a table that is the result of merging a list of tables.|
|[Table.FindText](table-findtext.md)|Returns all the rows that contain the given text in the table.|
|[Table.First](table-first.md)|Returns the first row or a specified default value.|
|[Table.FirstN](table-firstn.md)|Returns the first count rows specified.|
|[Table.FirstValue](table-firstvalue.md)|Returns the first column of the first row of the table or a specified default value.|
|[Table.FromPartitions](table-frompartitions.md)|Returns a table that is the result of combining a set of partitioned tables.|
|[Table.InsertRows](table-insertrows.md)|Inserts a list of rows into the table at the specified position.|
|[Table.Last](table-last.md)|Returns the last row or a specified default value.|
|[Table.LastN](table-lastn.md)|Returns the last specified number of rows.|
|[Table.MatchesAllRows](table-matchesallrows.md)|Indicates whether all the rows in the table meet the given condition.|
|[Table.MatchesAnyRows](table-matchesanyrows.md)|Indicates whether any the rows in the table meet the given condition.|
|[Table.Partition](table-partition.md)|Partitions the table into a list of tables based on the number of groups and column specified.|
|[Table.Range](table-range.md)|Returns the rows beginning at the specified offset.|
|[Table.RemoveFirstN](table-removefirstn.md)|Returns a table with the specified number of rows removed from the table starting at the first row.|
|[Table.RemoveLastN](table-removelastn.md)|Returns a table with the specified number of rows removed from the table starting at the last row.|
|[Table.RemoveRows](table-removerows.md)|Removes the specified number of rows.|
|[Table.RemoveRowsWithErrors](table-removerowswitherrors.md)|Returns a table with the rows removed from the input table that contain an error in at least one of the cells. If a columns list is specified, then only the cells in the specified columns are inspected for errors.|
|[Table.Repeat](table-repeat.md)|Repeats the rows of the tables a specified number of times.|
|[Table.ReplaceRows](table-replacerows.md)|Replaces the specified range of rows with the provided row or rows.|
|[Table.ReverseRows](table-reverserows.md)|Returns a table with the rows in reverse order.|
|[Table.SelectRows](table-selectrows.md)|Selects the rows that meet the condition function.|
|[Table.SelectRowsWithErrors](table-selectrowswitherrors.md)|Returns a table with only those rows of the input table that contain an error in at least one of the cells. If a columns list is specified, then only the cells in the specified columns are inspected for errors.|
|[Table.SingleRow](table-singlerow.md)|Returns a single row in the table.|
|[Table.Skip](table-skip.md)|Returns a table with the first specified number of rows skipped.|
|[Table.SplitAt](table-splitat.md)|Returns a list containing the first count rows specified and the remaining rows.|

## Column operations

|Name|Description|
|------------|---------------|
|[Table.Column](table-column.md)|Returns a specified column of data from the table as a list.|
|[Table.ColumnNames](table-columnnames.md)|Returns the column names as a list.|
|[Table.ColumnsOfType](table-columnsoftype.md)|Returns a list with the names of the columns that match the specified types.|
|[Table.DemoteHeaders](table-demoteheaders.md)|Demotes the column headers to the first row of values.|
|[Table.DuplicateColumn](table-duplicatecolumn.md) | Duplicates a column with the specified name. Values and type are copied from the source column.|
|[Table.HasColumns](table-hascolumns.md)|Indicates whether the table contains the specified column or columns.|
|[Table.Pivot](table-pivot.md)|Given a pair of columns representing attribute-value pairs, rotates the data in the attribute column into a column headings.|
|[Table.PrefixColumns](table-prefixcolumns.md)|Returns a table where the columns have all been prefixed with the given text.|
|[Table.PromoteHeaders](table-promoteheaders.md)|Promotes the first row of values as the new column headers (that is, as column names).|
|[Table.RemoveColumns](table-removecolumns.md)|Removes the specified columns.|
|[Table.ReorderColumns](table-reordercolumns.md)|Returns a table with the columns in the specified order.|
|[Table.RenameColumns](table-renamecolumns.md)|Returns a table with the columns renamed as specified.|
|[Table.SelectColumns](table-selectcolumns.md)|Returns a table with only the specified columns.|
|[Table.TransformColumnNames](table-transformcolumnnames.md)|Transforms column names by using the given function.|
|[Table.Unpivot](table-unpivot.md)|Translates a set of columns in a table into attribute-value pairs.|
|[Table.UnpivotOtherColumns](table-unpivotothercolumns.md)|Translates all columns other than a specified set into attribute-value pairs.|

## Transformation

|Name|Description|
|------------|---------------|
|[Table.AddColumn](table-addcolumn.md)|Adds a column with the specified name. The value is computed using the specified selection function with each row taken as an input.|
|[Table.AddFuzzyClusterColumn](table-addfuzzyclustercolumn.md)| Adds a new column with representative values obtained by fuzzy grouping values of the specified column in the table.|
|[Table.AddIndexColumn](table-addindexcolumn.md)|Appends a column with explicit position values.|
|[Table.AddJoinColumn](table-addjoincolumn.md)|Performs a join between tables on supplied columns and produces the join result in a new column.|
|[Table.AddKey](table-addkey.md)|Adds a key to a table.|
|[Table.AggregateTableColumn](table-aggregatetablecolumn.md)|Aggregates a column of tables into multiple columns in the containing table.|
|[Table.CombineColumns](table-combinecolumns.md)|Combines the specified columns into a new column using the specified combiner function.|
|[Table.CombineColumnsToRecord](table-combinecolumnstorecord.md)|Combines the specified columns into a new record-valued column where each record has field names and values corresponding to the column names and values of the columns that were combined.|
|[Table.ConformToPageReader](table-conformtopagereader.md)|This function is intended for internal use only.|
|[Table.ExpandListColumn](table-expandlistcolumn.md)|Given a column of lists in a table, create a copy of a row for each value in its list.|
|[Table.ExpandRecordColumn](table-expandrecordcolumn.md)|Expands a column of records into columns with each of the values.|
|[Table.ExpandTableColumn](table-expandtablecolumn.md)|Expands a column of records or a column of tables into multiple columns in the containing table.|
|[Table.FillDown](table-filldown.md)|Propagates the value of a previous cell to the null-valued cells below in the column.|
|[Table.FillUp](table-fillup.md)|Propagates the value of a cell to the null-valued cells above in the column.|
|[Table.FilterWithDataTable](table-filterwithdatatable.md)|This function is intended for internal use only.|
|[Table.FuzzyGroup](table-fuzzygroup.md)|Groups rows in the table based on fuzzy matching of keys.|
|[Table.FuzzyJoin](table-fuzzyjoin.md)|Joins the rows from the two tables that fuzzy match based on the given keys.|
|[Table.FuzzyNestedJoin](table-fuzzynestedjoin.md)|Performs a fuzzy join between tables on supplied columns and produces the join result in a new column.|
|[Table.Group](table-group.md)|Groups rows in the table that have the same key.|
|[Table.Join](table-join.md)|Joins the rows from the two tables that match based on the given keys.|
|[Table.Keys](table-keys.md)|Returns the keys of the specified table.|
|[Table.NestedJoin](table-nestedjoin.md)|Performs a join between tables on supplied columns and produces the join result in a new column.|
|[Table.ReplaceErrorValues](table-replaceerrorvalues.md)|Replaces the error values in the specified columns with the corresponding specified value.|
|[Table.ReplaceKeys](table-replacekeys.md)|Replaces the keys of the specified table.|
|[Table.ReplaceRelationshipIdentity](table-replacerelationshipidentity.md)|This function is intended for internal use only.|
|[Table.ReplaceValue](table-replacevalue.md)|Replaces one value with another in the specified columns.|
|[Table.Split](table-split.md)|Splits the specified table into a list of tables using the specified page size.|
|[Table.SplitColumn](table-splitcolumn.md)|Splits the specified column into a set of additional columns using the specified splitter function.|
|[Table.TransformColumns](table-transformcolumns.md)|Transforms the values of one or more columns.|
|[Table.TransformColumnTypes](table-transformcolumntypes.md)|Applies type transformation(s) of the form { column, type } using a specific culture.|
|[Table.TransformRows](table-transformrows.md)|Transforms the rows of the table using the specified transform function.|
|[Table.Transpose](table-transpose.md)|Makes columns into rows and rows into columns.|

## Membership

|Name|Description|
|------------|---------------|
|[Table.Contains](table-contains.md)|Indicates whether the specified record appears as a row in the table.|
|[Table.ContainsAll](table-containsall.md)|Indicates whether all of the specified records appear as rows in the table.|
|[Table.ContainsAny](table-containsany.md)|Indicates whether any of the specified records appear as rows in the table.|
|[Table.Distinct](table-distinct.md)|Removes duplicate rows from the table.|
|[Table.IsDistinct](table-isdistinct.md)|Indicates whether the table contains only distinct rows (no duplicates).|
|[Table.PositionOf](table-positionof.md)|Returns the position or positions of the row within the table.|
|[Table.PositionOfAny](table-positionofany.md)|Returns the position or positions of any of the specified rows within the table.|
|[Table.RemoveMatchingRows](table-removematchingrows.md)|Removes all occurrences of the specified rows from the table.|
|[Table.ReplaceMatchingRows](table-replacematchingrows.md)|Replaces all the specified rows with the provided row or rows.|

## Ordering

|Name|Description|
|------------|---------------|
|[Table.AddRankColumn](table-addrankcolumn.md)|Appends a column with the ranking of one or more other columns.|
|[Table.Max](table-max.md)|Returns the largest row or default value using the given criteria.|
|[Table.MaxN](table-maxn.md)|Returns the largest row or rows using the given criteria.|
|[Table.Min](table-min.md)|Returns the smallest row or a default value using the given criteria.|
|[Table.MinN](table-minn.md)|Returns the smallest row or rows using the given criteria.|
|[Table.Sort](table-sort.md)|Sorts the table using one or more column names and comparison criteria.|

## Other

|Name|Description|
|------------|---------------|
|[Table.Buffer](table-buffer.md)|Buffers a table in memory, isolating it from external changes during evaluation.|
|[Table.StopFolding](table-stopfolding.md) | Prevents any downstream operations from being run against the original source of the data.|

## Parameter Values

### Naming output columns

This parameter is a list of text values specifying the column names of the resulting table. This parameter is generally used in the [Table construction functions](#table-construction), such as [Table.FromRows](table-fromrows.md) and [Table.FromList](table-fromlist.md).

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

`ExtraValues.List = 0`<br/>
`ExtraValues.Error = 1`<br/>
`ExtraValues.Ignore = 2`

More information: [Table.FromList](table-fromlist.md), [ExtraValues.Type](extravalues-type.md)

### Missing column handling

This parameter is used to indicate how the function should handle missing columns. This parameter is specified as a number, which maps to the following options:

`MissingField.Error = 0`<br/>
`MissingField.Ignore = 1`<br/>
`MissingField.UseNull = 2;`

This parameter is used in column or transformation operations, for examples, in [Table.TransformColumns](table-transformcolumns.md). More information: [MissingField.Type](missingfield-type.md)

### Sort Order

Sort ordering is used to indicate how the results should be sorted. This parameter is specified as a number, which maps to the following options:

`Order.Ascending = 0`<br/>
`Order.Descending = 1`

More information: [Order.Type](order-type.md)

### Equation criteria

Equation criteria for tables can be specified as either:

- A function value that is either:
  
  - A key selector that determines the column in the table to apply the equality criteria.

  - A comparer function that is used to specify the kind of comparison to apply. Built-in comparer functions can be specified. More information: [Comparer functions](comparer-functions.md)

- A list of the columns in the table to apply the equality criteria.

For examples, go to the description of [Table.Distinct](table-distinct.md).  
