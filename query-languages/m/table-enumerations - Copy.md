---
description: "Learn more about: Table enumerations"
title: "Table enumerations | Microsoft Docs"
ms.date: 5/4/2022
ms.service: powerquery
ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table enumerations

These enumerations are used with table functions.

|Enumeration | Description|
|---------------- | -----------|
|[ExtraValues](extravalues.md) | Specifies what to do if the splitter function returns more columns than the table expects.|
|[GroupKind](groupkind.md) | Specifies what type of group is formed in the input table.|
|[JoinAlgorithm](joinalgorithm.md) |Specifies the algorithm to use when joining tables.|
|[JoinKind](joinkind.md) |Specifies how the rows of two tables are joined.|
|[JoinSide](joinside.md) | Specifies which table (left or right) is to be joined.|
|[MissingField.Error](missingfield-error.md) | An optional parameter in record and table functions indicating that missing fields should result in an error. (This is the default parameter value.)|
|[MissingField.Ignore](missingfield-ignore.md) | An optional parameter in record and table functions indicating that missing fields should be ignored.|
|[MissingField.UseNull](missingfield-usenull.md) | An optional parameter in record and table functions indicating that missing fields should be included as null values.|

## Transformation

**Parameters for Group options**

- GroupKind.Global = 0;

- GroupKind.Local = 1;

**Parameters for Join kinds**

- JoinKind.Inner = 0;

- JoinKind.LeftOuter = 1;

- JoinKind.RightOuter = 2;

- JoinKind.FullOuter = 3;

- JoinKind.LeftAnti = 4;

- JoinKind.RightAnti = 5

**Join Algorithm**

The following JoinAlgorithm values can be specified to Table.Join

-   ```  
    JoinAlgorithm.Dynamic        0,  
    ```  
  
-   ```  
    JoinAlgorithm.PairwiseHash   1,  
    ```  
  
-   ```  
    JoinAlgorithm.SortMerge      2,  
    ```  
  
-   ```  
    JoinAlgorithm.LeftHash       3,  
    ```  
  
-   ```  
    JoinAlgorithm.RightHash      4,  
    ```  
  
-   ```  
    JoinAlgorithm.LeftIndex      5,  
    ```  
  
-   ```  
    JoinAlgorithm.RightIndex     6,  
    ```  

Parameter values | Description
---------------- | -----------  
| [JoinSide.Left](joinside-left.md) | Specifies the left table of a join.|
| [JoinSide.Right](joinside-right.md) | Specifies the right table of a join.|

**Example data**

The following tables are used by the examples in this section.

**Customers table**

```
Customers = Table.FromRecords({

  [CustomerID = 1, Name = "Bob", Phone = "123-4567"],

  [CustomerID = 2, Name = "Jim", Phone = "987-6543"],

  [CustomerID = 3, Name = "Paul", Phone = "543-7890"],

  [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]

}
```

**Orders table**

```
Orders = Table.FromRecords({

  [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0],

  [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0],

  [OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0],

  [OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200.0],

  [OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2.0],

  [OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20.0],

  [OrderID = 7, CustomerID = 5, Item = "Bait", Price = 3.25],

  [OrderID = 8, CustomerID = 5, Item = "Fishing Rod", Price = 100.0],

  [OrderID = 9, CustomerID = 6, Item = "Bait", Price = 3.25]

})
```

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

**Parameters for membership checks**

**Occurrence specification**

-   ```
    Occurrence.First  = 0
    ```

-   ```
    Occurrence.Last   = 1
    ```

-   ```
    Occurrence.All    = 2
    ```

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

**Example data**

The following tables are used by the examples in this section.

**Employees table**

```
Employees = Table.FromRecords(

    {[Name="Bill",   Level=7,  Salary=100000],

     [Name="Barb",   Level=8,  Salary=150000],

     [Name="Andrew", Level=6,  Salary=85000],

     [Name="Nikki",  Level=5,  Salary=75000],

     [Name="Margo",  Level=3,  Salary=45000],

     [Name="Jeff",   Level=10, Salary=200000]},

type table [

    Name = text,

    Level = number,

    Salary = number

])
```

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

This parameter is a list of text values specifying the column names of the resulting table. This parameter is generally used in the Table construction functions, such as Table.FromRows and Table.FromList.

### Comparison criteria

Comparison criterion can be provided as either of the following values:

- A number value to specify a sort order. See sort order in the parameter values section above.

- To compute a key to be used for sorting, a function of 1 argument can be used.

- To both select a key and control order, comparison criterion can be a list containing the key and order.

- To completely control the comparison, a function of 2 arguments can be used that returns -1, 0, or 1 given the relationship between the left and right inputs.  Value.Compare is a method that can be used to delegate this logic.

For examples, go to the description of [Table.Sort](table-sort.md).

### Count or Condition critieria

This criteria is generally used in ordering or row operations. It determines the number of rows returned in the table and can take two forms, a number or a condition:

- A number indicates how many values to return inline with the appropriate function

- If a condition is specified, the rows containing values that initially meet the condition is returned. Once a value fails the condition, no further values are considered.

Go to [Table.FirstN](table-firstn.md) or [Table.MaxN](table-maxn.md).

### Handling of extra values

This is used to indicate how the function should handle extra values in a row. This parameter is specified as a number, which maps to the options below.

```
ExtraValues.List = 0

ExtraValues.Error = 1

ExtraValues.Ignore = 2
```

For more information, go to [Table.FromList](table-fromlist.md).

### Missing column handling

This is used to indicate how the function should handle missing columns. This parameter is specified as a number, which maps to the options below.

```
MissingField.Error = 0;

MissingField.Ignore = 1;

MissingField.UseNull = 2;
```

This is used in column or transformation operations. For examples, go to [Table.TransformColumns](table-transformcolumns.md).

### Sort Order

This is used to indicate how the results should be sorted. This parameter is specified as a number, which maps to the options below.

```
Order.Ascending = 0

    Order.Descending = 1
```

### Equation criteria

Equation criteria for tables can be specified as either:

- A function value that is either:
  
  - A key selector that determines the column in the table to apply the equality criteria.

  - A comparer function that is used to specify the kind of comparison to apply. Built-in comparer functions can be specified; go t0 section for Comparer functions.

- A list of the columns in the table to apply the equality criteria.

For examples, go to the description for [Table.Distinct](table-distinct.md).  
