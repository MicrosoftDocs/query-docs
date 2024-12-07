---
description: "Learn more about: ADDMISSINGITEMS"
title: "ADDMISSINGITEMS function (DAX) | Microsoft Docs"
---
# ADDMISSINGITEMS

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Adds rows with empty values to a table returned by [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md).
  
## Syntax  
  
```dax
ADDMISSINGITEMS ( [<showAll_columnName> [, <showAll_columnName> [, … ] ] ], <table> [, <groupBy_columnName> [, [<filterTable>] [, <groupBy_columnName> [, [<filterTable>] [, … ] ] ] ] ] ] )
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`showAll_columnName`| (Optional) A column for which to return items with no data for the measures used. If not specified, all columns are returned.|  
|`table`|A SUMMARIZECOLUMNS table.|  
|`groupBy_columnName`|(Optional) A column to group by in the supplied table argument.|
|`filterTable`|(Optional) A table expression that defines which rows are returned.|  

## Return value

A table with one or more columns.

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## With SUMMARIZECOLUMNS

A table returned by [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) will include only rows with values. By wrapping a [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) expression within an ADDMISSINGITEMS expression, rows containing no values are also returned.

### Example

Without ADDMISSINGITEMS, the following query:

```dax
SUMMARIZECOLUMNS( 
    'Sales'[CustomerId], 
    "Total Qty", SUM ( Sales[TotalQty] )
)
```

Returns,

|CustomerId|TotalQty|
|--------------|------------|
|A|5|
|B|3|
|C|3|
|E|2|

With ADDMISSINGITEMS, the following query:

```dax
EVALUATE
ADDMISSINGITEMS (
    'Sales'[CustomerId],
    SUMMARIZECOLUMNS( 
        'Sales'[CustomerId],
        "Total Qty", SUM ( Sales[TotalQty] )
    ),
    'Sales'[CustomerId]
)
```

Returns,

|CustomerId|TotalQty|
|--------------|------------|
|A|5|
|B|3|
|C|3|
|D| |
|E|2|
|F| |
