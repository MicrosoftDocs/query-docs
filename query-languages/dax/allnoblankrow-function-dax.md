---
description: "Learn more about: ALLNOBLANKROW"
title: "ALLNOBLANKROW function (DAX)"
ms.topic: reference

---
# ALLNOBLANKROW

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

From the parent table of a relationship, returns all rows but the blank row, or all distinct values of a column but the blank row, and disregards any context filters that might exist.

## Syntax

```dax
ALLNOBLANKROW( {<table> | <column>[, <column>[, <column>[,…]]]} )
```

### Parameters

|Term|Definition|
|--------|--------------|
|`table`|The table over which all context filters are removed.|
|`column`|A column over which all context filters are removed.|

Only one parameter must be passed; the parameter is either a table or a column.

## Return value

A table, when the passed parameter was a table, or a column of values, when the passed parameter was a column.

## Remarks

- The ALLNOBLANKROW function only filters the blank row that a parent table, in a relationship, will show when there are one or more rows in the child table that have non-matching values to the parent column. See the example below for a thorough explanation.

- The following table summarizes the variations of `ALL` that are provided in DAX, and their differences:

    |Function and usage|Description|
    |----------------------|---------------|
    |`ALL(Column)`|Removes all filters from the specified column in the table; all other filters in the table, over other columns, still apply.|
    |`ALL(Table)`|Removes all filters from the specified table.|
    |`ALLEXCEPT(Table,Col1,Col2...)`|Overrides all context filters in the table except over the specified columns.|
    |`ALLNOBLANK(table|column)`| From the parent table of a relationship, returns all rows but the blank row, or all distinct values of a column but the blank row, and disregards any context filters that might exist|

    For a general description of how the ALL function works, together with step-by-step examples that use ALL(Table) and ALL(Column), see [ALL function](all-function-dax.md).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

In the sample data, the ResellerSales_USD table contains one row that has no values and therefore cannot be related to any of the parent tables in the relationships within the workbook. You will use this table in a PivotTable so that you can see the blank row behavior and how to handle counts on unrelated data.

Step 1: Verify the unrelated data 

Open the **Power Pivot window**, then select the ResellerSales_USD table. In the ProductKey column, filter for blank values. One row will remain. In that row, all column values should be blank except for SalesOrderLineNumber.

Step 2: Create a PivotTable

Create a new PivotTable, then drag the column, datetime.[Calendar Year], to the Row Labels pane. The following table shows the expected results:

|Row Labels|
|--------------|
|2005|
|2006|
|2007|
|2008|
||
|Grand Total|

Note the blank label between **2008** and **Grand Total**. This blank label represents the Unknown member, which is a special group that is created to account for any values in the child table that have no matching value in the parent table, in this example the datetime.[Calendar Year] column.

When you see this blank label in the PivotTable, you know that in some of the tables that are related to the column, datetime.[Calendar Year], there are either blank values or non-matching values. The parent table is the one that shows the blank label, but the rows that do not match are in one or more of the child tables.

The rows that get added to this blank label group are either values that do not match any value in the parent table-- for example, a date that does not exist in the datetime table-- or null values, meaning no value for date at all. In this example we have placed a blank value in all columns of the child sales table. Having more values in the parent table than in the children tables does not cause a problem.

Step 3: Count rows using ALL and ALLNOBLANK 

Add the following two measures to the datetime table, to count the table rows: **Countrows ALLNOBLANK of datetime**, **Countrows ALL of datetime**. The formulas that you can use to define these measures are:

```dax
// Countrows ALLNOBLANK of datetime
= COUNTROWS(ALLNOBLANKROW('DateTime'))

// Countrows ALL of datetime
= COUNTROWS(ALL('DateTime'))

// Countrows ALLNOBLANKROW of ResellerSales_USD
= COUNTROWS(ALLNOBLANKROW('ResellerSales_USD'))

// Countrows ALL of ResellerSales_USD
= COUNTROWS(ALL('ResellerSales_USD'))
```

On a blank PivotTable add datetime.[Calendar Year] column to the row labels, and then add the newly created measures.  The results should look like the following table:

|Row Labels|Countrows ALLNOBLANK of datetime|Countrows ALL of datetime|
|--------------|------------------------------------|-----------------------------|
|2005|1280|1281|
|2006|1280|1281|
|2007|1280|1281|
|2008|1280|1281|
||1280|1281|
|Grand Total|1280|1281|

The results show a difference of 1 row in the table rows count. However, if you open the **Power Pivot window** and select the datetime table, you cannot find any blank row in the table because the special blank row mentioned here is the Unknown member.

Step 4: Verify that the count is accurate

In order to prove that the ALLNOBLANKROW does not count any truly blank rows, and only handles the special blank row on the parent table only, add the following two measures to the ResellerSales_USD table: **Countrows ALLNOBLANKROW of ResellerSales_USD**, **Countrows ALL of ResellerSales_USD**.

Create a new PivotTable, and drag the column, datetime.[Calendar Year], to the Row Labels pane. Now add the measures that you just created. The results should look like the following:

|Row Labels|Countrows ALLNOBLANKROW of ResellerSales_USD|Countrows ALL of ResellerSales_USD|
|--------------|-------------------------------------------------|---------------------------------------|
|2005|60856|60856|
|2006|60856|60856|
|2007|60856|60856|
|2008|60856|60856|
||60856|60856|
|Grand Total|60856|60856|

Now the two measures have the same results. That is because the ALLNOBLANKROW function does not count truly blank rows in a table, but only handles the blank row that is a special case generated in a parent table, when one or more of the child tables in the relationship contain non-matching values or blank values.

## Related content

- [Filter functions](filter-functions-dax.md)
- [ALL function](all-function-dax.md)
- [FILTER function](filter-function-dax.md)
