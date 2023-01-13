---
description: "Learn more about: OFFSET"
title: "OFFSET function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax
ms.date: 11/15/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---

# OFFSET

Returns a single row that is positioned either before or after the *current row* within the same table, by a given offset. If the current row cannot be deduced to a single row, multiple rows may be returned.
  
## Syntax  
  
```dax
OFFSET ( <delta>[, <relation>][, <orderBy>][, <blanks>][, <partitionBy>] )
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|delta|The number of rows before (negative value) or after (positive value) the current row from which to obtain the data.  It can be any DAX expression that returns a scalar value. |
|relation|(Optional) A table expression from which the output row is returned. </br>If specified, all columns in \<orderBy> and \<partitionBy> must come from it. </br>If omitted: </br>- \<orderBy> must be explicitly specified.</br>- All \<orderBy> and \<partitionBy> columns must be fully qualified and come from a single table. </br>- Defaults to ALLSELECTED() of all columns in \<orderBy> and \<partitionBy>.|
|orderBy|(Optional) An ORDERBY() clause containing the columns that define how each partition is sorted. </br>If omitted: </br>- \<relation> must be explicitly specified. </br>- Defaults to ordering by every column in \<relation> that is not already specified in \<partitionBy>.|
|blanks|(Optional) An enumeration that defines how to handle blank values when sorting. </br>This parameter is reserved for future use. </br>Currently, the only supported value is KEEP (default), where the behavior for numerical/date values is blank values are ordered between zero and negative values. The behavior for strings is blank values are ordered before all strings, including empty strings.|
|partitionBy|(Optional) A PARTITIONBY() clause containing the columns that define how \<relation> is partitioned. </br> If omitted, \<relation> is treated as a single partition. |
  
## Return value

One or more rows from \<relation>.  
  
## Remarks

Each \<orderBy> and \<partitionBy> column must have a corresponding outer value to help define the current row on which to operate, with the following behavior:

- If there is exactly one corresponding outer column, its value is used.
- If there is no corresponding outer column, then:
  - OFFSET will first determine all \<orderBy> and \<partitionBy> columns that have no corresponding outer column.
  - For every combination of existing values for these columns in OFFSET’s parent context, OFFSET is evaluated and a row is returned.
  - OFFSET’s final output is a union of these rows.
- If there is more than one corresponding outer column, an error is returned.

If the columns specified within \<orderBy> and \<partitionBy> can't uniquely identify every row in \<relation>, then:

- OFFSET will try to find the least number of additional columns required to uniquely identify every row.
- If such columns can be found, OFFSET will automatically append these new columns to \<orderBy>, and each partition is sorted using this new set of OrderBy columns.  
- If such columns cannot be found, an error is returned.

An empty table is returned if:

- The corresponding outer value of an OrderBy or PartitionBy column does not exist within \<relation>.
- The \<delta> value causes a shift to a row that does not exist within the partition.  

If OFFSET is used within a calculated column defined on the same table as \<relation>, and \<orderBy> is omitted, an error is returned.

## Example 1

The following DAX query:
  
```dax
DEFINE
VAR vRelation = SUMMARIZECOLUMNS ( 
                    DimProductCategory[EnglishProductCategoryName], 
                    DimDate[CalendarYear], 
                    "CurrentYearSales", SUM(FactInternetSales[SalesAmount]) 
                  )
EVALUATE
ADDCOLUMNS (
    vRelation, 
    "PreviousYearSales", 
    SELECTCOLUMNS(
        OFFSET ( 
                -1, 
                vRelation, 
                ORDERBY([CalendarYear]), 
                PARTITIONBY([EnglishProductCategoryName])
        ),
        [Current Sales]
    )
)

```

Returns a table that summarizes the total sales for each product category and calendar year, as well as the total sales for that category in the previous year.

## Example 2

The following DAX query:

```dax
DEFINE
MEASURE DimProduct[CurrentYearSales] = SUM(FactInternetSales[SalesAmount])
MEASURE DimProduct[PreviousYearSales] = CALCULATE(SUM(FactInternetSales[SalesAmount]), OFFSET(-1, , ORDERBY(DimDate[CalendarYear])))
EVALUATE
SUMMARIZECOLUMNS (
    DimDate[CalendarYear],
    "CurrentYearSales", DimProduct[CurrentYearSales],
    "PreviousYearSales", DimProduct[PreviousYearSales]
)
```

Uses OFFSET() in a measure to return a table that summarizes the total sales for each calendar year and the total sales for the previous year.

## See also

[INDEX](index-function-dax.md)  
[ORDERBY](orderby-function-dax.md)  
[PARTITIONBY](partitionby-function-dax.md)  
[WINDOW](window-function-dax.md)  
[RANK](rank-function-dax.md)  
[ROWNUMBER](rownumber-function-dax.md)
