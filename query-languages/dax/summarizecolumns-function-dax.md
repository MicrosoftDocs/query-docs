---
title: "SUMMARIZECOLUMNS Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# SUMMARIZECOLUMNS Function (DAX)

Returns a summary table over a set of groups.  
  
## Syntax  
  
```dax
SUMMARIZECOLUMNS( <groupBy_columnName> [, < groupBy_columnName >]…, [<filterTable>]…[, <name>, <expression>]…)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|groupBy_columnName|A fully qualified column reference (Table[Column]) to a base table for which the distinct values are included in the returned table. Each groupBy_columnName column is cross-joined (different tables) or auto-existed (same table) with the subsequent specified columns.|  
|filterTable|A table expression which is added to the filter context of all columns specified as groupBy_columnName arguments. The values present in the filter table are used to filter before cross-join/auto-exist is performed.|  
|name|A string representing the column name to use for the subsequent expression specified.|  
|expression|Any DAX expression that returns a single value (not a table).|  
  
## Return value  
A table which includes combinations of values from the supplied columns, based on the grouping specified. Only rows for which at least one of the supplied expressions return a non-blank value are included in the table returned. If all expressions evaluate to BLANK/NULL for a row, that row is not included in the table returned.  
  
## Remarks  
SUMMARIZECOLUMNS does not guarantee any sort order for the results.  
  
A column cannot be specified more than once in the groupBy_columnName parameter. For example, the following formulas are invalid.  
  
`SUMMARIZECOLUMNS( Sales[StoreId], Sales[StoreId] )`  
  
**Filter context**  
  
Consider the following query:  
  
```dax
SUMMARIZECOLUMNS ( 'Sales Territory'[Category], FILTER('Customer', 'Customer' [First Name] = “Alicia”) )
``` 
  
In this query, without a measure the groupBy columns do not contain any columns from the Filter expression (i.e. from Customer table). The filter is not applied to the groupBy columns. The Sales Territory and the Customer table may be indirectly related through the Reseller sales fact table. Since they're not directly related, the filter expression is a no-op and the groupBy columns are not impacted.  
  
However, with this query:  
  
```dax
SUMMARIZECOLUMNS ( 'Sales Territory'[Category], 'Customer' [Education], FILTER('Customer', 'Customer'[First Name] = “Alicia”) )
```  
  
The groupBy columns contain a column which is impacted by the filter and that filter is applied to the groupBy results.  
  
## Options  
  
### IGNORE  
The IGNORE() syntax can be used to modify the behavior of the SUMMARIZECOLUMNS function by omitting specific expressions from the BLANK/NULL evaluation. Rows for which all expressions not using IGNORE return BLANK/NULL will be excluded independent of whether the expressions which do use IGNORE evaluate to BLANK/NULL or not.  
  
#### Syntax  

```dax
IGNORE(<expression>)
``` 
  
**With SUMMARIZECOLUMNS**  
  
```dax
SUMMARIZECOLUMNS(<groupBy_columnName>[, < groupBy_columnName >]…, [<filterTable>]…[, <name>, IGNORE(…)]…)
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|expression|Any DAX expression that returns a single value (not a table).|  
  
#### Return value  
This function does not return a value.  
  
#### Remarks  
IGNORE can be used as an expression argument to SUMMARIZECOLUMNS.  
  
#### Example  

```dax
SUMMARIZECOLUMNS( Sales[CustomerId], "Total Qty", IGNORE( SUM( Sales[Qty] ) ), “BlankIfTotalQtyIsNot3”, IF( SUM( Sales[Qty] )=3, 3 ) )
``` 
  
This rolls up the Sales[CustomerId] column, creating a subtotal for all customers in the given grouping. Without IGNORE, the result is:  
  
|CustomerId|TotalQty|BlankIfTotalQtyIsNot3|  
|--------------|------------|-------------------------|  
|A|5||  
|B|3|3|  
|C|3|3|  
  
**With IGNORE**  
  
|CustomerId|TotalQty|BlankIfTotalQtyIsNot3|  
|--------------|------------|-------------------------|  
|B|3|3|  
|C|3|3|  
  
**All expression ignored**  
  
```dax
SUMMARIZECOLUMNS( Sales[CustomerId], "Blank", IGNORE( Blank() ), “BlankIfTotalQtyIsNot5”, IGNORE( IF( SUM( Sales[Qty] )=5, 5 ) ) )
``` 
  
Even though both expressions return blank for some rows, they're included since there are no non-ignored expressions which return blank.  
  
|CustomerId|TotalQty|BlankIfTotalQtyIsNot3|  
|--------------|------------|-------------------------|  
|A||5|  
|B|||  
|C|||  


### NONVISUAL

Marks a value filter in SUMMARIZECOLUMNS function as not affecting measure values, but only applying to group-by columns.

#### Syntax

```dax
NONVISUAL(<expression>)
```
#### Return value

A table of values.

#### Example

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

**Result**

Returns the result where [Visual Total Sales] is the total across all years:

|DimDate[CalendarYear]  |[Sales]  |[Visual Total Sales]  |
|---------|---------|---------|
|2007    |    9,791,060.30     |   29,358,677.22      |
|2008     |     9,770,899.74    |    29,358,677.22     |

In contrast, the same query without the NONVISUAL function:

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

**Result**

Returns the result where [Visual Total Sales] is the total across the two selected years:

|DimDate[CalendarYear]  |[Sales]  |[Visual Total Sales]  |
|---------|---------|---------|
|2007    |    9,791,060.30     |   19,561,960.04      |
|2008     |     9,770,899.74    |    19,561,960.04     |
  
### ROLLUPADDISSUBTOTAL()  
The addition of the ROLLUPADDISSUBTOTAL() syntax modifies the behavior of the SUMMARIZECOUMNS function by adding roll-up/subtotal rows to the result based on the `groupBy_columnName` columns.  
  
#### Syntax  
```dax
ROLLUPADDISSUBTOTAL ( [<filter> …, ] <groupBy_columnName>, <isSubtotal_columnName>[, <filter> …][, <groupBy_columnName >, <isSubtotal_columnName>[, <filter> …]…] ) 
```  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|groupBy_columnName|The qualified name of an existing column to be used to create summary groups based on the values found in it. This parameter cannot be an expression.|  
|isSubtotal_columnName|The name of the Boolean column to be added to the result, indicating whether or not a row is a subtotal over the groupBy column (or columns when used with ROLLUPGROUP). This value is calculated using the ISSUBTOTAL function.|  
|filter    | A table expression which is added to the filter context at the current grouping level. A filter before the first group-by column is applied at the grand total level.
  
#### Return value  
The function does not return a value. It only specifies the set of columns to be subtotaled.  
  
#### Example  
**Single subtotal**  
  
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
  
**Result**  
  
|Category  |Subcategory  |IsCategorySubtotal  |IsSubcategorySubtotal  |Total Qty 
|---------|---------|---------|---------|---------|
|      |         |   True      |    True     |    60398     |
|Accessories     |         |    False     |    True     |   36092      |
|Accessories     |   Bike Racks      |   False      |   False      |    328     |
|Bikes    |   Mountain Bikes      |   False      |   False      |    4970     |
|Clothing     |         |  False       |    True     |    9101     |
  
**Multiple subtotals**  
  
```dax
SUMMARIZECOUMNS ( Regions[State], ROLLUPADDISSUBTOTAL ( Sales[CustomerId], "IsCustomerSubtotal" ), ROLLUPADDISSUBTOTAL ( Sales[Date], "IsDateSubtotal"), "Total Qty", SUM( Sales[Qty] ) )
``` 
  
Sales is grouped by state, by customer, by date, with subtotals for 1. Sales by state, by date 2. Sales by State, by Customer 3. Rolled up on both customer and date leading to sales by state.  
  
**Result**  
  
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
  
### ROLLUPGROUP()  
Like with the SUMMARIZE function, ROLLUPGROUP can be used together with ROLLUPADDISSUBTOTAL to specify which summary groups/granularities (subtotals) to include (reducing the number of subtotal rows returned).  
  
#### Syntax  

```dax
ROLLUPGROUP(<groupBy_columnName>, <groupBy_columnName>)
``` 
  
**With ROLLUPADDISSUBTOTAL**  
  
```dax
ROLLUPADDISSUBTOTAL( ROLLUPGROUP(…), isSubtotal_columnName[, <groupBy_columnName>…] )
``` 
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|groupBy_columnName|The qualified name of an existing column to be used to create summary groups based on the values found in it. The set of group by columns supplied to ROLLUPGROUP function will define the granularity to return subtotal rows for (same behavior as when ROLLUP and ROLLUPGROUP are used with the SUMMARIZE function). This parameter  cannot be an expression.|  
  
#### Return value  
The function does not return a value. It marks a set of columns to be grouped during subtotaling by ROLLUPADDISSUBTOTAL.  
  
#### Remarks  
ROLLUPGROUP can only be used as an groupBy_columnName argument to ROLLUPADDISSUBTOTAL or the SUMMARIZE function.  
  
#### Example  
**Multiple subtotals**  
  
```dax
SUMMARIZECOLUMNS( ROLLUPADDISSUBTOTAL( Sales[CustomerId], "IsCustomerSubtotal" ), ROLLUPADDISSUBTOTAL(ROLLUPGROUP(Regions[City], Regions[State]), “IsCityStateSubtotal”),"Total Qty", SUM( Sales[Qty] ) )
```  
  
Still grouped by City and State, but rolled together when reporting a subtotal.  
  
**Result**  
  
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
  
## See Also  
[SUMMARIZE Function &#40;DAX&#41;](summarize-function-dax.md)  
  
