---
title: "GROUPBY function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# GROUPBY
  
The GROUPBY function is similar to the SUMMARIZE function. However, GROUPBY does not do an implicit CALCULATE for any extension columns that it adds. GROUPBY permits a new function, CURRENTGROUP(), to be used inside aggregation functions in the extension columns that it adds. GROUPBY attempts to reuse the data that has been grouped making it highly performant.  
  
## Syntax  
  
```dax
GROUPBY (<table>, [<groupBy_columnName1>], [<name>, <expression>]… )  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|Any DAX expression that returns a table of data.|  
|groupBy_columnName|The name of an existing column in the table (or in a related table,) by which the data is to be grouped. This parameter cannot be an expression.|  
|name|The name given to a new column that is being added to the list of GroupBy columns, enclosed in double quotes.|  
|expression|Any DAX expression that returns a single scalar value, where the expression is to be evaluated for each set of GroupBy values.<br /><br />**Note:** The expression used in GroupBy may include any of the "X" aggregation functions, such as SUMX, AVERAGEX, MINX, MAXX, etc. and when one of these function is used in this way, we allow the table argument (which normally must be a table expression) to be replaced by a special CURRENTGROUP() function as described elsewhere in this document.<br /><br />Restrictions on expression:<br /><br />-   The CALCULATE function (and therefore measures) are not allowed in the expression.<br />-   The CURRENTGROUP function may only be used at the top level of table scans in the expression. That is, SUMX(&lt;table&gt;,SUMX(CURRENTGROUP(…), …)) is not allowed. ABS( SUMX(CURRENTGROUP(), [Column] ) ) is allowed, since ABS does not perform a scan.|  
  
## Return value

A table with the selected columns for the groupBy_columnName arguments and the grouped by columns designated by the name arguments.  
  
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

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## With CURRENTGROUP

[CURRENTGROUP](currentgroup-function-dax.md) can only be used in an expression that defines a column within the GROUPBY function. In-effect, [CURRENTGROUP](currentgroup-function-dax.md) returns a set of rows from the table argument of GROUPBY that belong to the current row of the GROUPBY result. The [CURRENTGROUP](currentgroup-function-dax.md) function takes no arguments and is only supported as the first argument to one of the following aggregation functions: AVERAGEX, COUNTAX, COUNTX, GEOMEANX, MAXX, MINX, PRODUCTX, STDEVX.S, STDEVX.P, SUMX, VARX.S, VARX.P.  
  
### Example

Assume a data model has four tables:  Sales, Customer, Product, Geography where Sales is on the "many" side of a relationship to each of the other three tables:  
  
```dax
GROUPBY (  
Sales,
Geography[Country],
Product[Category],
"Total Sales", SUMX( CURRENTGROUP(), Sales[Price] * Sales[Qty])  
)  
```

This will start with the Sales table, extended with all the columns from all the related tables.Then it will build a result with three columns.  
  
- The first column is each of the countries for which there is a sale.  
  
- The second column is each product category for which there is a sale in that country.  
  
- The third column is the sum of sales amount (as calculated from price*qty) for the selected country and product category.  
  
Suppose we've built the previous result.  We can use GROUPBY again, to find the maximum category sales figure within each country as shown here:  
  
```dax
DEFINE  
VAR SalesByCountryAndCategory =  
GROUPBY (  
Sales,
Geography[Country],
Product[Category],
"Total Sales", SUMX( CURRENTGROUP(), Sales[Price] * Sales[Qty])  
)  
  
Evaluate GROUPBY (  
SalesByCountryAndCategory,
Geography[Country],
 "Max Sales", MAXX( CURRENTGROUP(), [Total Sales])  
)  
```
  
## See also

[SUMMARIZE function](summarize-function-dax.md)  
[SUMMARIZECOLUMNS function](summarizecolumns-function-dax.md)  
