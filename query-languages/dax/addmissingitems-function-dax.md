---
title: "ADDMISSINGITEMS function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 09/01/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ADDMISSINGITEMS

Adds rows with empty values to a table returned by [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md).
  
## Syntax  
  
```dax
ADDMISSINGITEMS ( [<ShowAll_ColumnName> [, <ShowAll_ColumnName> [, … ] ] ], <Table> [, <GroupBy_ColumnName> [, [<FilterTable>] [, <GroupBy_ColumnName> [, [<FilterTable>] [, … ] ] ] ] ] ] )
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|ShowAllColumnName| (Optional) A column for which to return items with no data for the measures used. If not specified, all columns are returned.|  
|Table|A SUMMARIZECOLUMNS table.|  
|GroupBy_ColumnName|(Optional) A column to group by in the supplied table argument.|
|FilterTable|(Optional) A table expression that defines which rows are returned.|  

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
ADMISSINGITEMS (
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
