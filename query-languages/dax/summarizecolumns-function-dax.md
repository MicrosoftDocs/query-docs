---
description: "Learn more about: SUMMARIZECOLUMNS"
title: "SUMMARIZECOLUMNS function (DAX)"
---
# SUMMARIZECOLUMNS

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Returns a summary table over a set of groups.  
  
## Syntax  
  
```dax
SUMMARIZECOLUMNS( <groupBy_columnName> [, < groupBy_columnName >]…, [<filterTable>]…[, <name>, <expression>]…)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`groupBy_columnName`|A fully qualified column reference (Table[Column]) to a base table for which the distinct values are included in the returned table. Each groupBy_columnName column is cross-joined (different tables) or auto-existed (same table) with the subsequent specified columns.|  
|`filterTable`|A table expression which is added to the filter context of all columns specified as groupBy_columnName arguments. The values present in the filter table are used to filter before cross-join/auto-exist is performed.|  
|`name`|A string representing the column name to use for the subsequent expression specified.|  
|`expression`|Any DAX expression that returns a single value (not a table).|  
  
## Return value

A table which includes combinations of values from the supplied columns based on the grouping specified. Only rows for which at least one of the supplied expressions return a non-blank value are included in the table returned. If all expressions evaluate to BLANK/NULL for a row, that row is not included in the table returned.  
  
## Remarks

- This function does not guarantee any sort order for the results.  
  
- A column cannot be specified more than once in the groupBy_columnName parameter. For example, the following formula is invalid.  
  
  `SUMMARIZECOLUMNS( Sales[StoreId], Sales[StoreId] )`  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Filter context
  
Consider the following query:  
  
```dax
SUMMARIZECOLUMNS ( 
    'Sales Territory'[Category], 
    FILTER('Customer', 'Customer' [First Name] = "Alicia") 
)
```
  
In this query, without a measure the groupBy columns do not contain any columns from the FILTER expression (for example, from Customer table). The filter is not applied to the groupBy columns. The Sales Territory and Customer tables may be indirectly related through the Reseller sales fact table. Since they're not directly related, the filter expression is a no-op and the groupBy columns are not impacted.  
  
However, with this query:  
  
```dax
SUMMARIZECOLUMNS ( 
    'Sales Territory'[Category], 'Customer' [Education], 
    FILTER('Customer', 'Customer'[First Name] = "Alicia") 
)
```  
  
The groupBy columns contain a column which is impacted by the filter and that filter is applied to the groupBy results.  
  
## With IGNORE

The [IGNORE](ignore-function-dax.md) syntax can be used to modify the behavior of the SUMMARIZECOLUMNS function by omitting specific expressions from the BLANK/NULL evaluation. Rows for which all expressions not using [IGNORE](ignore-function-dax.md) return BLANK/NULL will be excluded independent of whether the expressions which do use [IGNORE](ignore-function-dax.md) evaluate to BLANK/NULL or not. [IGNORE](ignore-function-dax.md) can only be used within a SUMMARIZECOLUMNS expression.

### Example

```dax
SUMMARIZECOLUMNS( 
    Sales[CustomerId], "Total Qty", 
    IGNORE( SUM( Sales[Qty] ) ), 
    "BlankIfTotalQtyIsNot3", IF( SUM( Sales[Qty] )=3, 3 ) 
)
```
  
This rolls up the Sales[CustomerId] column, creating a subtotal for all customers in the given grouping. Without [IGNORE](ignore-function-dax.md), the result is:  
  
|CustomerId|Total Qty|BlankIfTotalQtyIsNot3|  
|--------------|------------|-------------------------|  
|A|5||  
|B|3|3|  
|C|3|3|  
  
With [IGNORE](ignore-function-dax.md),
  
|CustomerId|Total Qty|BlankIfTotalQtyIsNot3|  
|--------------|------------|-------------------------|  
|B|3|3|  
|C|3|3|  
  
All expression ignored,
  
```dax
SUMMARIZECOLUMNS( 
    Sales[CustomerId], "Blank", 
    IGNORE( BLANK() ), "BlankIfTotalQtyIsNot5", 
    IGNORE( IF( SUM( Sales[Qty] )=5, 5 ) ) 
)
```
  
Even though both expressions return blank for some rows, they're included since there are no unignored expressions which return blank.  
  
|CustomerId|Blank|BlankIfTotalQtyIsNot5|  
|--------------|------------|-------------------------|  
|A||5|  
|B|||  
|C|||  

## With NONVISUAL

The [NONVISUAL](nonvisual-function-dax.md) function marks a value filter in SUMMARIZECOLUMNS function as not affecting measure values, but only applying to groupBy columns. [NONVISUAL](nonvisual-function-dax.md) can only be used within a SUMMARIZECOLUMNS expression.

### Example

```dax
DEFINE
MEASURE FactInternetSales[Sales] = SUM(FactInternetSales[Sales Amount])
EVALUATE
SUMMARIZECOLUMNS
(
    DimDate[CalendarYear],
    NONVISUAL(TREATAS({2007, 2008}, DimDate[CalendarYear])),
    "Sales", [Sales],
    "Visual Total Sales", CALCULATE([Sales], ALLSELECTED(DimDate[CalendarYear]))
)
ORDER BY [CalendarYear]
```

Returns the result where [Visual Total Sales] is the total across all years:

|DimDate[CalendarYear]  |[Sales]  |[Visual Total Sales]  |
|---------|---------|---------|
|2007    |    9,791,060.30     |   29,358,677.22      |
|2008     |     9,770,899.74    |    29,358,677.22     |

In contrast, the same query *without* the NONVISUAL function:

```dax
DEFINE
MEASURE FactInternetSales[Sales] = SUM(FactInternetSales[Sales Amount])
EVALUATE
SUMMARIZECOLUMNS
(
    DimDate[CalendarYear],
    TREATAS({2007, 2008}, DimDate[CalendarYear]),
    "Sales", [Sales],
    "Visual Total Sales", CALCULATE([Sales], ALLSELECTED(DimDate[CalendarYear]))
)
ORDER BY [CalendarYear]
```

Returns the result where [Visual Total Sales] is the total across the two selected years:

|DimDate[CalendarYear]  |[Sales]  |[Visual Total Sales]  |
|---------|---------|---------|
|2007    |    9,791,060.30     |   19,561,960.04      |
|2008     |     9,770,899.74    |    19,561,960.04     |
  
## With ROLLUPADDISSUBTOTAL

The addition of the [ROLLUPADDISSUBTOTAL](rollupaddissubtotal-function-dax.md) syntax modifies the behavior of the SUMMARIZECOLUMNS function by adding rollup/subtotal rows to the result based on the groupBy_columnName columns. [ROLLUPADDISSUBTOTAL](rollupaddissubtotal-function-dax.md) can only be used within a SUMMARIZECOLUMNS expression.
  
### Example with single subtotal
  
```dax
DEFINE
VAR vCategoryFilter =
  TREATAS({"Accessories", "Clothing"}, Product[Category])
VAR vSubcategoryFilter = 
  TREATAS({"Bike Racks", "Mountain Bikes"}, Product[Subcategory])
EVALUATE
  SUMMARIZECOLUMNS
  (
    ROLLUPADDISSUBTOTAL
    (
      Product[Category], "IsCategorySubtotal", vCategoryFilter,
      Product[Subcategory], "IsSubcategorySubtotal", vSubcategoryFilter
    ),
    "Total Qty", SUM(Sales[Qty])
  )
  ORDER BY
  [IsCategorySubtotal] DESC, [Category],
  [IsSubcategorySubtotal] DESC, [Subcategory]

```
  
Returns the following table,
  
|Category  |Subcategory  |IsCategorySubtotal  |IsSubcategorySubtotal  |Total Qty
|---------|---------|---------|---------|---------|
|      |         |   True      |    True     |    60398     |
|Accessories     |         |    False     |    True     |   36092      |
|Accessories     |   Bike Racks      |   False      |   False      |    328     |
|Bikes    |   Mountain Bikes      |   False      |   False      |    4970     |
|Clothing     |         |  False       |    True     |    9101     |
  
### Example with multiple subtotals
  
```dax
SUMMARIZECOLUMNS ( 
    Regions[State], ROLLUPADDISSUBTOTAL ( Sales[CustomerId], "IsCustomerSubtotal" ), 
    ROLLUPADDISSUBTOTAL ( Sales[Date], "IsDateSubtotal"), "Total Qty", SUM( Sales[Qty] ) 
)
```
  
Sales is grouped by state, by customer, by date, with subtotals for 1. Sales by state, by date 2. Sales by State, by Customer 3. Rolled up on both customer and date leading to sales by state.  
  
Returns the following table,
  
|CustomerID|IsCustomerSubtotal|State|Total Qty|Date|IsDateSubtotal|  
|--------------|----------------------|---------|-------------|--------|------------------|  
|A|`FALSE`|WA|5|7/10/2014||  
|B|`FALSE`|WA|1|7/10/2014||  
|B|`FALSE`|WA|2|7/11/2014||  
|C|`FALSE`|OR|2|7/10/2014||  
|C|`FALSE`|OR|1|7/11/2014||  
||`TRUE`|WA|6|7/10/2014||  
||`TRUE`|WA|2|7/11/2014||  
||`TRUE`|OR|2|7/10/2014||  
||`TRUE`|OR|1|7/11/2014||  
|A|`FALSE`|WA|5||`TRUE`|  
|B|`FALSE`|WA|3||`TRUE`|  
|C|`FALSE`|OR|3||`TRUE`|  
||`TRUE`|WA|8||`TRUE`|  
||`TRUE`|OR|3||`TRUE`|  
  
## With ROLLUPGROUP

Like with the [SUMMARIZE](summarize-function-dax.md) function, [ROLLUPGROUP](rollupgroup-function-dax.md) can be used together with [ROLLUPADDISSUBTOTAL](rollupaddissubtotal-function-dax.md) to specify which summary groups/granularities (subtotals) to include, reducing the number of subtotal rows returned. [ROLLUPGROUP](rollupgroup-function-dax.md) can only be used within a SUMMARIZECOLUMNS or [SUMMARIZE](summarize-function-dax.md) expression.
  
### Example with multiple subtotals
  
```dax
SUMMARIZECOLUMNS( 
    ROLLUPADDISSUBTOTAL( Sales[CustomerId], "IsCustomerSubtotal" ), 
    ROLLUPADDISSUBTOTAL(ROLLUPGROUP(Regions[City], Regions[State]), "IsCityStateSubtotal"),"Total Qty", SUM( Sales[Qty] ) 
)
```  
  
Still grouped by City and State, but rolled together when reporting a subtotal returns the following table,

|State|CustomerId|IsCustomerSubtotal|Total Qty|City|IsCityStateSubtotal|  
|---------|--------------|----------------------|-------------|--------|-----------------------|  
|WA|A|`FALSE`|2|Bellevue|`FALSE`|  
|WA|B|`FALSE`|2|Bellevue|`FALSE`|  
|WA|A|`FALSE`|3|Redmond|`FALSE`|  
|WA|B|`FALSE`|1|Redmond|`FALSE`|  
|OR|C|`FALSE`|3|Portland|`FALSE`|  
|WA||`TRUE`|4|Bellevue|`FALSE`|  
|WA||`TRUE`|4|Redmond|`FALSE`|  
|OR||`TRUE`|3|Portland|`FALSE`|  
||A|`FALSE`|5||`FALSE`|  
||B|`FALSE`|3||`TRUE`|  
||C|`FALSE`|3||`TRUE`|  
|||`TRUE`|11||`TRUE`|  

## Contextual SummarizeColumns ##
### Background
Until February 2023, SUMMARIZECOLUMNS did not support evaluation within a context transition at all. In products released before that month, this limitation made SUMMARIZECOLUMNS not useful in most of the measures – it was not possible to call a measure SUMMARIZECOLUMNS in any case of context transition, including other SUMMARIZECOLUMNS statements. 

From February 2023, the context transition was supported in a few scenarios, but not in all the conditions. The supported and restricted cases are as follows:

| SummarizeColumns Type | External Filter with single column | External Filter with more than one column | External GroupBy Columns  |
| -------- | ------- | ------- | ------- |
| SummarizeColumns with GroupBy only | OK | OK | OK |
| SummarizeColumns with Filters/Measures | OK | ERROR | ERROR |

From June 2024, we are enabling contextual SummarizeColumns which allows SummarizeColumns to be evaluated in any context transition, SummarizeColumns in measure is now fully supported:

| SummarizeColumns Type | External Filter with single column | External Filter with more than one column | External GroupBy Columns  |
| -------- | ------- | ------- | ------- |
| SummarizeColumns with GroupBy only | OK | OK | OK |
| SummarizeColumns with Filters/Measures | OK | OK | OK |

However, this update also includes changes to the behavior of SummarizeColumns, which may alter the results of existing expressions: 

### SelfValue semantics for external filters ###
We are introducing a semantic concept named SelfValue, which alters how filters from external tables interact with GroupBy columns in SummarizeColumns. This change disallows filters from a different table to affect the GroupBy columns, even if the tables are related through a filter-by relationship.
An example illustrating the impact of this change involves the following expression:

```
CalculateTable(
  SummarizeColumns(
      'Reseller Sales'[ResellerKey], 
      'Reseller Sales'[ProductKey]
  ), 
  Treatas({(229)}, 'Product'[Product Key])
)
```

Before this update, the TreatAs filter would apply to the GroupBy operation within SummarizeColumns, leveraging the relationship between 'Product'[Product Key] and 'Reseller Sales'[ProductKey]. Consequently, the query results would only include rows where 'Reseller Sales'[ProductKey] equals 229.
However, after the update, GroupBy columns within SummarizeColumns will no longer be filtered by columns from external tables, even if a relationship exists between them. Therefore, in the example above, the GroupBy column 'Reseller Sales'[ProductKey] will not be filtered by the 'Product'[ProductKey] column. As a result, the query will include rows where 'Reseller Sales'[ProductKey] is not equal to 229.

If you prefer to retain the previous behavior, you can rewrite the expression using Summarize instead of SummarizeColumns, as shown below:
```
CalculateTable(
    SUMMARIZE(
        'Reseller Sales',
        [ResellerKey],
        [ProductKey]
    ),
    Treatas({(229)}, 'Product'[Product Key])
)
```
This rewritten expression preserves the original semantics where the GroupBy operation is not affected by the SelfValue restriction introduced by the update.

### Row validation for groupby columns fully covered by Treatas ###

Prior to this update, within a SummarizeColumns function, if all GroupBy columns from a specific table were fully covered by a single Treatas filter from that same table, as shown below:

```
SummarizeColumns(
  Geography[Country], 
  Geography[State], 
  Treatas(
      {("United States", "Alberta")}, 
      Geography[Country], 
      Geography[State]
  )
)
```
The result of the above query would include whatever rows were specified in the Treatas filter, regardless of whether they were valid or not. For instance, the result would be a single-row table ("United States", "Alberta"), even if no such row with [Country] = "United States" and [State] = "Alberta" existed in the 'Geography' table. 

This issue was known and has been addressed by the update. After the update, such invalid rows will be filtered out, and only valid rows from the GroupBy table will be returned. Therefore, the result for the query above would be empty, as there are no valid rows matching the specified [Country] and [State] values in the 'Geography' table.

### Disallow mixed Keepfilters/overriddefilters on same table/cluster ###

The recent update has introduced a temporary restriction that triggers an error message stating:
```   
"SummarizeColumns filters with keepfilters behavior and overridefilters behavior are mixed within one cluster, which is not allowed. Consider adding keepfilters() to all filters of summarizecolumns." 
```
This error occurs when both normal filters (which override existing filters) and filters with KeepFilters specified are present within the same table/cluster. For example:
```
Evaluate CalculateTable(
  SummarizeColumns(
      Product[Color],
      KeepFilters(
          TreatAs(
              {( "Washington")}
              , Geography[State]
          )
      ),
      TreatAs(
          {("United States"), ("Canada")}
          , Geography[Country]
      )
  )
  ,TreatAs({("Alberta")}, Geography[State])
  ,TreatAs({("Canada")}, Geography[Country])
)
```
In the above expression, there are two filters on the 'Geography' table: one with KeepFilters specified and one without. These filters overlap with external filters on different columns. Currently, this configuration is not allowed because internally, the two filters are clustered into one, and the system cannot determine the correct filter overriding behavior for the clustered filter overall in such cases.

Please note that this restriction is temporary. We are actively developing solutions to remove this limitation in future updates. If you encounter this error, we advise adjusting the filters within SummarizeColumns by adding or removing KeepFilters as necessary to ensure consistent overriding behavior on each table.

## Related content

[SUMMARIZE](summarize-function-dax.md)
