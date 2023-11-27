---
description: "Learn more about: SUMMARIZECOLUMNS"
title: "SUMMARIZECOLUMNS function (DAX) | Microsoft Docs"
---
# SUMMARIZECOLUMNS

Returns a summary table over a set of groups.  
  
## Syntax  
  
```dax
SUMMARIZECOLUMNS( <groupBy_columnName> [, < groupBy_columnName >]…, [<filterTable>]…[, <name>, <expression>]…)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|groupBy_columnName|A fully qualified column reference (Table[Column]) to a base table for which the distinct values are included in the returned table. Each groupBy_columnName column is cross-joined (different tables) or auto-existed (same table) with the subsequent specified columns.|  
|filterTable|A table expression which is added to the filter context of all columns specified as groupBy_columnName arguments. The values present in the filter table are used to filter before cross-join/auto-exist is performed.|  
|name|A string representing the column name to use for the subsequent expression specified.|  
|expression|Any DAX expression that returns a single value (not a table).|  
  
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
  
|CustomerId|TotalQty|BlankIfTotalQtyIsNot3|  
|--------------|------------|-------------------------|  
|A|5||  
|B|3|3|  
|C|3|3|  
  
With [IGNORE](ignore-function-dax.md),
  
|CustomerId|TotalQty|BlankIfTotalQtyIsNot3|  
|--------------|------------|-------------------------|  
|B|3|3|  
|C|3|3|  
  
All expression ignored,
  
```dax
SUMMARIZECOLUMNS( 
    Sales[CustomerId], "Blank", 
    IGNORE( Blank() ), "BlankIfTotalQtyIsNot5", 
    IGNORE( IF( SUM( Sales[Qty] )=5, 5 ) ) 
)
```
  
Even though both expressions return blank for some rows, they're included since there are no unignored expressions which return blank.  
  
|CustomerId|TotalQty|BlankIfTotalQtyIsNot3|  
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
SUMMARIZECOUMNS ( 
    Regions[State], ROLLUPADDISSUBTOTAL ( Sales[CustomerId], "IsCustomerSubtotal" ), 
    ROLLUPADDISSUBTOTAL ( Sales[Date], "IsDateSubtotal"), "Total Qty", SUM( Sales[Qty] ) 
)
```
  
Sales is grouped by state, by customer, by date, with subtotals for 1. Sales by state, by date 2. Sales by State, by Customer 3. Rolled up on both customer and date leading to sales by state.  
  
Returns the following table,
  
|CustomerID|IsCustomerSubtotal|State|Total Qty|Date|IsDateSubtotal|  
|--------------|----------------------|---------|-------------|--------|------------------|  
|A|FALSE|WA|5|7/10/2014||  
|B|FALSE|WA|1|7/10/2014||  
|B|FALSE|WA|2|7/11/2014||  
|C|FALSE|OR|2|7/10/2014||  
|C|FALSE|OR|1|7/11/2014||  
||TRUE|WA|6|7/10/2014||  
||TRUE|WA|2|7/11/2014||  
||TRUE|OR|2|7/10/2014||  
||TRUE|OR|1|7/11/2014||  
|A|FALSE|WA|5||TRUE|  
|B|FALSE|WA|3||TRUE|  
|C|FALSE|OR|3||TRUE|  
||TRUE|WA|8||TRUE|  
||TRUE|OR|3||TRUE|  
  
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
|WA|A|FALSE|2|Bellevue|FALSE|  
|WA|B|FALSE|2|Bellevue|FALSE|  
|WA|A|FALSE|3|Redmond|FALSE|  
|WA|B|FALSE|1|Redmond|FALSE|  
|OR|C|FALSE|3|Portland|FALSE|  
|WA||TRUE|4|Bellevue|FALSE|  
|WA||TRUE|4|Redmond|FALSE|  
|OR||TRUE|3|Portland|FALSE|  
||A|FALSE|5||FALSE|  
||B|FALSE|3||TRUE|  
||C|FALSE|3||TRUE|  
|||TRUE|11||TRUE|  
  
## Related content

[SUMMARIZE](summarize-function-dax.md)
