---
title: "SUMMARIZECOLUMNS Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
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
  
## Return Value  
A table which includes combinations of values from the supplied columns, based on the grouping specified. Only rows for which at least one of the supplied expressions return a non-blank value are included in the table returned. If all expressions evaluate to BLANK/NULL for a row, that row is not included in the table returned.  
  
## Remarks  
SUMMARIZECOLUMNS does not guarantee any sort order for the results.  
  
A column cannot be specified more than once in the groupBy_columnName parameter. For example, the following formulas are invalid.  
  
`SUMMARIZECOLUMNS( Sales[StoreId], Sales[StoreId] )`  
  
**Filter context**  
  
Consider the following query:  
  
`SUMMARIZECOLUMNS ( 'Sales Territory'[Category], FILTER('Customer', 'Customer' [First Name] = “Alicia”) )`  
  
In this query, without a measure the groupBy columns do not contain any columns from the Filter expression (i.e. from Customer table). The filter is not applied to the groupBy columns. The Sales Territory and the Customer table may be indirectly related through the Reseller sales fact table. Since they're not directly related, the filter expression is a no-op and the groupBy columns are not impacted.  
  
However, with this query:  
  
`SUMMARIZECOLUMNS ( 'Sales Territory'[Category], 'Customer' [Education], FILTER('Customer', 'Customer'[First Name] = “Alicia”) )`  
  
The groupBy columns contain a column which is impacted by the filter and that filter is applied to the groupBy results.  
  
## Options  
  
### IGNORE  
The IGNORE() syntax can be used to modify the behavior of the SUMMARIZECOLUMNS function by omitting specific expressions from the BLANK/NULL evaluation. Rows for which all expressions not using IGNORE return BLANK/NULL will be excluded independent of whether the expressions which do use IGNORE evaluate to BLANK/NULL or not.  
  
#### Syntax  
`IGNORE(<expression>)`  
  
**With SUMMARIZECOLUMNS**  
  
`SUMMARIZECOLUMNS(<groupBy_columnName>[, < groupBy_columnName >]…, [<filterTable>]…[, <name>, IGNORE(…)]…)`  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|expression|Any DAX expression that returns a single value (not a table).|  
  
#### Return value  
This function does not return a value.  
  
#### Remarks  
IGNORE can be used as an expression argument to SUMMARIZECOLUMNS.  
  
#### Example  
`SUMMARIZECOLUMNS( Sales[CustomerId], "Total Qty", IGNORE( SUM( Sales[Qty] ) ), “BlankIfTotalQtyIsNot3”, IF( SUM( Sales[Qty] )=3, 3 ) )`  
  
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
  
`SUMMARIZECOLUMNS( Sales[CustomerId], "Blank", IGNORE( Blank() ), “BlankIfTotalQtyIsNot5”, IGNORE( IF( SUM( Sales[Qty] )=5, 5 ) ) )`  
  
Even though both expressions return blank for some rows, they're included since there are no non-ignored expressions which return blank.  
  
|CustomerId|TotalQty|BlankIfTotalQtyIsNot3|  
|--------------|------------|-------------------------|  
|A||5|  
|B|||  
|C|||  
  
### ROLLUPADDISSUBTOTAL()  
The addition of the ROLLUPADDISSUBTOTAL() syntax modifies the behavior of the SUMMARIZECOUMNS function by adding roll-up/subtotal rows to the result based on the `groupBy_columnName` columns.  
  
#### Syntax  
`ROLLUPADDISSUBTOTAL ( <groupBy_columnName>, <isSubtotal_columnName>[, <groupBy_columnName >, <isSubtotal_columnName>…] )`  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|groupBy_columnName|The qualified name of an existing column to be used to create summary groups based on the values found in it. This parameter cannot be an expression.|  
|isSubtotal_columnName|The name of the Boolean column to be added to the result, indicating whether or not a row is a subtotal over the groupBy column (or columns when used with ROLLUPGROUP). This value is calculated using the ISSUBTOTAL function.|  
  
#### Return Value  
The function does not return a value. It only specifies the set of columns to be subtotaled.  
  
#### Example  
**Single subtotal**  
  
`SUMMARIZECOUMNS (Regions[State], ROLLUPADDISSUBTOTAL ( Sales[CustomerId], “IsCustomerSubtotal” ), Sales[Date], "Total Qty", SUM( Sales[Qty] ))`  
  
**Result**  
  
|CustomerID|IsCustomerSubtotal|State|Total Qty|  
|--------------|----------------------|---------|-------------|  
|A|FALSE|WA|5|  
|B|FALSE|WA|3|  
|C|FALSE|OR|3|  
||TRUE|WA|8|  
||TRUE|OR|3|  
  
**Multiple subtotals**  
  
`SUMMARIZECOUMNS ( Regions[State], ROLLUPADDISSUBTOTAL ( Sales[CustomerId], "IsCustomerSubtotal" ), ROLLUPADDISSUBTOTAL ( Sales[Date], "IsDateSubtotal"), "Total Qty", SUM( Sales[Qty] ) )`  
  
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
`ROLLUPGROUP(<groupBy_columnName>, <groupBy_columnName>)`  
  
**With ROLLUPADDISSUBTOTAL**  
  
`ROLLUPADDISSUBTOTAL( ROLLUPGROUP(…), isSubtotal_columnName[, <groupBy_columnName>…] )`  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|groupBy_columnName|The qualified name of an existing column to be used to create summary groups based on the values found in it. The set of group by columns supplied to ROLLUPGROUP function will define the granularity to return subtotal rows for (same behavior as when ROLLUP and ROLLUPGROUP are used with the SUMMARIZE function). This parameter  cannot be an expression.|  
  
#### Return Value  
The function does not return a value. It marks a set of columns to be grouped during subtotaling by ROLLUPADDISSUBTOTAL.  
  
#### Remarks  
ROLLUPGROUP can only be used as an groupBy_columnName argument to ROLLUPADDISSUBTOTAL or the SUMMARIZE function.  
  
#### Example  
**Multiple subtotals**  
  
`SUMMARIZECOLUMNS( ROLLUPADDISSUBTOTAL( Sales[CustomerId], "IsCustomerSubtotal" ), ROLLUPADDISSUBTOTAL(ROLLUPGROUP(Regions[City], Regions[State]), “IsCityStateSubtotal”),"Total Qty", SUM( Sales[Qty] ) )`  
  
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
  
