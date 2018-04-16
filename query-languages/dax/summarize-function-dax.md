---
title: "SUMMARIZE Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# SUMMARIZE Function (DAX)
Returns a summary table for the requested totals over a set of groups.  
  
## Syntax  
  
```  
SUMMARIZE(<table>, <groupBy_columnName>[, <groupBy_columnName>]…[, <name>, <expression>]…)  
```  
  
#### Parameters  
table  
Any DAX expression that returns a table of data.  
  
groupBy_columnName  
(Optional) The qualified name of an existing column to be used to create summary groups based on the values found in it. This parameter cannot be an expression.  
  
name  
The name given to a total or summarize column, enclosed in double quotes.  
  
expression  
Any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row/context).  
  
## Return Value  
A table with the selected columns for the *groupBy_columnName* arguments and the summarized columns designed by the name arguments.  
  
## Remarks  
  
1.  Each column for which you define a name must have a corresponding expression; otherwise, an error is returned. The first argument, name, defines the name of the column in the results. The second argument, expression, defines the calculation performed to obtain the value for each row in that column.  
  
2.  groupBy_columnName must be either in *table* or in a related table to *table*.  
  
3.  Each name must be enclosed in double quotation marks.  
  
4.  The function groups a selected set of rows into a set of summary rows by the values of one or more groupBy_columnName columns. One row is returned for each group.  
  
## Example  
The following example returns a summary of the reseller sales grouped around the calendar year and the product category name, this result table allows you to do analysis over the reseller sales by year and product category.  
  
```  
SUMMARIZE(ResellerSales_USD  
      , DateTime[CalendarYear]  
      , ProductCategory[ProductCategoryName]  
      , "Sales Amount (USD)", SUM(ResellerSales_USD[SalesAmount_USD])  
      , "Discount Amount (USD)", SUM(ResellerSales_USD[DiscountAmount])  
      )  
```  
The following table shows a preview of the data as it would be received by any function expecting to receive a table:  
      
|**DateTime[CalendarYear]**|**ProductCategory[ProductCategoryName]**|**[Sales Amount (USD)]**|**[Discount Amount (USD)]**|  
|---------|---------|---------|---------|  
|2008|Bikes|12968255.42|36167.6592|  
|2005|Bikes|6958251.043|4231.1621|  
|2006|Bikes|18901351.08|178175.8399|  
|2007|Bikes|24256817.5|276065.992|  
|2008|Components|2008052.706|39.9266|  
|2005|Components|574256.9865|0|  
|2006|Components|3428213.05|948.7674|  
|2007|Components|5195315.216|4226.0444|  
|2008|Clothing|366507.844|4151.1235|  
|2005|Clothing|31851.1628|90.9593|  
|2006|Clothing|455730.9729|4233.039|  
|2007|Clothing|815853.2868|12489.3835|  
|2008|Accessories|153299.924|865.5945|  
|2005|Accessories|18594.4782|4.293|  
|2006|Accessories|86612.7463|1061.4872|  
|2007|Accessories|275794.8403|4756.6546|  
  
## Advanced SUMMARIZE options  
  
### SUMMARIZE with ROLLUP  
The addition of the ROLLUP() syntax modifies the behavior of the SUMMARIZE function by adding roll-up rows to the result on the groupBy_columnName columns.  
  
```  
SUMMARIZE(<table>, <groupBy_columnName>[, <groupBy_columnName>]…[, ROLLUP(<groupBy_columnName>[,< groupBy_columnName>…])][, <name>, <expression>]…)  
```  
  
#### ROLLUP parameters  
groupBy_columnName  
The qualified name of an existing column to be used to create summary groups based on the values found in it. This parameter cannot be an expression.  
  
**Note**: All other SUMMARIZE parameters are explained before and not repeated here for brevity.  
  
#### Remarks  
  
-   The columns mentioned in the ROLLUP expression cannot be referenced as part of a *groupBy_columnName* columns.  
  
#### Example  
The following example adds roll-up rows to the Group-By columns of the SUMMARIZE function call.  
  
```  
SUMMARIZE(ResellerSales_USD  
      , ROLLUP( DateTime[CalendarYear], ProductCategory[ProductCategoryName])  
      , "Sales Amount (USD)", SUM(ResellerSales_USD[SalesAmount_USD])  
      , "Discount Amount (USD)", SUM(ResellerSales_USD[DiscountAmount])  
)  
```  
The following table shows a preview of the data as it would be received by any function expecting to receive a table:  
  
|**DateTime[CalendarYear]**|**ProductCategory[ProductCategoryName]**|**[Sales Amount (USD)]**|**[Discount Amount (USD)]**|  
|---------|---------|---------|---------|  
|2008|Bikes|12968255.42|36167.6592|  
|2005|Bikes|6958251.043|4231.1621|  
|2006|Bikes|18901351.08|178175.8399|  
|2007|Bikes|24256817.5|276065.992|  
|2008|Components|2008052.706|39.9266|  
|2005|Components|574256.9865|0|  
|2006|Components|3428213.05|948.7674|  
|2007|Components|5195315.216|4226.0444|  
|2008|Clothing|366507.844|4151.1235|  
|2005|Clothing|31851.1628|90.9593|  
|2006|Clothing|455730.9729|4233.039|  
|2007|Clothing|815853.2868|12489.3835|  
|2008|Accessories|153299.924|865.5945|  
|2005|Accessories|18594.4782|4.293|  
|2006|Accessories|86612.7463|1061.4872|  
|2007|Accessories|275794.8403|4756.6546|  
|2008||15496115.89|41224.3038|  
|2005||7582953.67|4326.4144|  
|2006||22871907.85|184419.1335|  
|2007||30543780.84|297538.0745|  
|||76494758.25|527507.9262|  
  
### ROLLUPGROUP  
ROLLUPGROUP() can be used to calculate groups of subtotals. If used in-place of ROLLUP, ROLLUPGROUP will yield the same result by adding roll-up rows to the result on the groupBy_columnName columns. However, the addition of ROLLUPGROUP() inside a ROLLUP syntax can be used to prevent partial subtotals in roll-up rows.  
  
The following example shows only the grand total of all years and categories without the subtotal of each year with all categories:  
  
```  
SUMMARIZE(ResellerSales_USD  
      , ROLLUP(ROLLUPGROUP( DateTime[CalendarYear], ProductCategory[ProductCategoryName]))  
      , "Sales Amount (USD)", SUM(ResellerSales_USD[SalesAmount_USD])  
      , "Discount Amount (USD)", SUM(ResellerSales_USD[DiscountAmount])  
)  
```  
The following table shows a preview of the data as it would be received by any function expecting to receive a table:  
  
|**DateTime[CalendarYear]**|**ProductCategory[ProductCategoryName]**|**[Sales Amount (USD)]**|**[Discount Amount (USD)]**|  
|---------|---------|---------|---------|  
|2008|Bikes|12968255.42|36167.6592|  
|2005|Bikes|6958251.043|4231.1621|  
|2006|Bikes|18901351.08|178175.8399|  
|2007|Bikes|24256817.5|276065.992|  
|2008|Components|2008052.706|39.9266|  
|2005|Components|574256.9865|0|  
|2006|Components|3428213.05|948.7674|  
|2007|Components|5195315.216|4226.0444|  
|2008|Clothing|366507.844|4151.1235|  
|2005|Clothing|31851.1628|90.9593|  
|2006|Clothing|455730.9729|4233.039|  
|2007|Clothing|815853.2868|12489.3835|  
|2008|Accessories|153299.924|865.5945|  
|2005|Accessories|18594.4782|4.293|  
|2006|Accessories|86612.7463|1061.4872|  
|2007|Accessories|275794.8403|4756.6546|  
|||76494758.25|527507.9262|  
  
### SUMMARIZE with ISSUBTOTAL  
Enables the user to create another column, in the Summarize function, that returns True if the row contains sub-total values for the column given as argument to ISSUBTOTAL, otherwise returns False.  
  
```  
SUMMARIZE(<table>, <groupBy_columnName>[, <groupBy_columnName>]…[, ROLLUP(<groupBy_columnName>[,< groupBy_columnName>…])][, <name>, {<expression>|ISSUBTOTAL(<columnName>)}]…)  
```  
  
#### ISSUBTOTAL parameters  
columnName  
The name of any column in table of the SUMMARIZE function or any column in a related table to table.  
  
#### Return Value  
A **True** value if the row contains a sub-total value for the column given as argument, otherwise returns **False**  
  
#### Remarks  
  
-   ISSUBTOTAL can only be used in the expression part of a SUMMARIZE function.  
  
-   ISSUBTOTAL must be preceded by a matching *name* column.  
  
#### Example  
The following sample generates an ISSUBTOTAL() column for each of the ROLLUP() columns in the given SUMMARIZE() function call.  
  
```  
SUMMARIZE(ResellerSales_USD  
      , ROLLUP( DateTime[CalendarYear], ProductCategory[ProductCategoryName])  
      , "Sales Amount (USD)", SUM(ResellerSales_USD[SalesAmount_USD])  
      , "Discount Amount (USD)", SUM(ResellerSales_USD[DiscountAmount])  
      , "Is Sub Total for DateTimeCalendarYear", ISSUBTOTAL(DateTime[CalendarYear])  
      , "Is Sub Total for ProductCategoryName", ISSUBTOTAL(ProductCategory[ProductCategoryName])  
)  
```  
The following table shows a preview of the data as it would be received by any function expecting to receive a table:  
  
  
|**[Is Sub Total for DateTimeCalendarYear]**|**[Is Sub Total for ProductCategoryName]**|**DateTime[CalendarYear]**|**ProductCategory[ProductCategoryName]**|**[Sales Amount (USD)]**|**[Discount Amount (USD)]**|  
|---------|---------|---------|---------|---------|---------|  
|FALSE|FALSE|||||  
|FALSE|FALSE|2008|Bikes|12968255.42|36167.6592|  
|FALSE|FALSE|2005|Bikes|6958251.043|4231.1621|  
|FALSE|FALSE|2006|Bikes|18901351.08|178175.8399|  
|FALSE|FALSE|2007|Bikes|24256817.5|276065.992|  
|FALSE|FALSE|2008|Components|2008052.706|39.9266|  
|FALSE|FALSE|2005|Components|574256.9865|0|  
|FALSE|FALSE|2006|Components|3428213.05|948.7674|  
|FALSE|FALSE|2007|Components|5195315.216|4226.0444|  
|FALSE|FALSE|2008|Clothing|366507.844|4151.1235|  
|FALSE|FALSE|2005|Clothing|31851.1628|90.9593|  
|FALSE|FALSE|2006|Clothing|455730.9729|4233.039|  
|FALSE|FALSE|2007|Clothing|815853.2868|12489.3835|  
|FALSE|FALSE|2008|Accessories|153299.924|865.5945|  
|FALSE|FALSE|2005|Accessories|18594.4782|4.293|  
|FALSE|FALSE|2006|Accessories|86612.7463|1061.4872|  
|FALSE|FALSE|2007|Accessories|275794.8403|4756.6546|  
|FALSE|TRUE|||||  
|FALSE|TRUE|2008||15496115.89|41224.3038|  
|FALSE|TRUE|2005||7582953.67|4326.4144|  
|FALSE|TRUE|2006||22871907.85|184419.1335|  
|FALSE|TRUE|2007||30543780.84|297538.0745|  
|TRUE|TRUE|||76494758.25|527507.9262|  
  
