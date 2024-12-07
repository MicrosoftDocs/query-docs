---
description: "Learn more about: GROUPBY"
title: "GROUPBY function (DAX) | Microsoft Docs"
---
# GROUPBY

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]
  
The GROUPBY function is similar to the [SUMMARIZE](summarize-function-dax.md) function. However, GROUPBY does not do an implicit [CALCULATE](calculate-function-dax.md) for any extension columns that it adds. GROUPBY permits a new function, [CURRENTGROUP](currentgroup-function-dax.md), to be used inside aggregation functions in the extension columns that it adds. GROUPBY is used to perform multiple aggregations in a single table scan.
  
## Syntax  
  
```dax
GROUPBY (<table> [, <groupBy_columnName> [, <groupBy_columnName> [, …]]] [, <name>, <expression> [, <name>, <expression> [, …]]])
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`table`|Any DAX expression that returns a table of data.|  
|`groupBy_columnName`|The name of an existing column in the table (or in a related table,) by which the data is to be grouped. This parameter cannot be an expression.|  
|`name`|The name given to a new column that is being added to the list of GroupBy columns, enclosed in double quotes.|  
|`expression`|One of the X aggregation functions with the first argument being CURRENTGROUP(). See With CURRENTGROUP section below for the full list of supported X aggregation functions.|  
  
## Return value

A table with the selected columns for the groupBy_columnName arguments and the extension columns designated by the name arguments.  
  
## Remarks

- The GROUPBY function does the following:  
  
    1. Start with the specified table (and all related tables in the "to-one" direction).  
  
    2. Create a grouping using all of the GroupBy columns (which are required to exist in the table from step #1.).  
  
    3. Each group is one row in the result, but represents a set of rows in the original table.  
  
    4. For each group, evaluate the extension columns being added.  Unlike the SUMMARIZE function, an implied CALCULATE is not performed, and the group isn't placed into the filter context.  
  
- Each column for which you define a name must have a corresponding expression; otherwise, an error is returned. The first argument, name, defines the name of the column in the results. The second argument, expression, defines the calculation performed to obtain the value for each row in that column.  
  
- groupBy_columnName must be either in table or in a related table.  
  
- Each name must be enclosed in double quotation marks.  
  
- The function groups a selected set of rows into a set of summary rows by the values of one or more groupBy_columnName columns. One row is returned for each group.  

- GROUPBY is primarily used to perform aggregations over intermediate results from DAX table expressions. For efficient aggregations over physical tables in the model, consider using [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) or [SUMMARIZE](summarize-function-dax.md) function.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## With CURRENTGROUP

[CURRENTGROUP](currentgroup-function-dax.md) can only be used in an expression that defines an extension column within the GROUPBY function. In-effect, [CURRENTGROUP](currentgroup-function-dax.md) returns a set of rows from the table argument of GROUPBY that belong to the current row of the GROUPBY result. The [CURRENTGROUP](currentgroup-function-dax.md) function takes no arguments and is only supported as the first argument to one of the following aggregation functions: [AVERAGEX](averagex-function-dax.md), [COUNTAX](countax-function-dax.md), [COUNTX](countx-function-dax.md), [GEOMEANX](geomeanx-function-dax.md), [MAXX](maxx-function-dax.md), [MINX](minx-function-dax.md), [PRODUCTX](productx-function-dax.md), [STDEVX.S](stdevx-s-function-dax.md), [STDEVX.P](stdevx-s-function-dax.md), [SUMX](sumx-function-dax.md), [VARX.S](varx-s-function-dax.md), [VARX.P](varx-p-function-dax.md).  
  
### Example

The following example first calculates the total sales grouped by country and product category over physical tables by using the [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) function. It then uses the GROUPBY function to scan the intermediate result from the first step to find the maximum sales in each country across the product categories.
  
```dax
DEFINE  
VAR SalesByCountryAndCategory =  
SUMMARIZECOLUMNS(  
Geography[Country],
Product[Category],
"Total Sales", SUMX(Sales, Sales[Price] * Sales[Qty])  
)  
  
EVALUATE
GROUPBY(  
SalesByCountryAndCategory,
Geography[Country],
"Max Sales", MAXX(CURRENTGROUP(), [Total Sales])  
)  
```
  
## Related content

[SUMMARIZE function](summarize-function-dax.md)  
[SUMMARIZECOLUMNS function](summarizecolumns-function-dax.md)  
