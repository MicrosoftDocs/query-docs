---
description: "Learn more about: OFFSET"
title: "OFFSET function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax
ms.date: 10/17/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---

# OFFSET

Returns a single row that is positioned either before or after the current row by a given offset, within the same table.
  
## Syntax  
  
```dax
OFFSET ( <delta>[, <relation>][, <orderBy>][, <partitionBy>] )  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|delta|The number of rows before (negative value) or after (positive value) the current row from which to obtain the data.  It can be any DAX expression that returns a scalar value. |
|relation|(Optional) A table expression from which the output row will be returned. <br>If specified, all columns in \<orderBy> and \<partitionBy> must come from it. <br>If omitted: <br>- \<orderBy> must be explicitly specified.<br>- All \<orderBy> and \<partitionBy> columns must be fully qualified and come from a single table. <br>- Defaults to ALLSELECTED() of all columns in \<orderBy> and \<partitionBy>.|
|orderBy|(Optional) An ORDERBY() clause containing the columns that define how each partition is sorted. <br>If omitted: <br>- \<relation> must be explicitly specified. <br>- Defaults to ordering by every column in \<relation>.
|partitionBy|(Optional) A PARTITIONBY() clause containing the columns that define how \<relation> is partitioned. <br> If omitted, \<relation> will be treated as a single partition. |
  
## Return value

A single row from \<relation>.  
  
## Remarks

- \<orderBy> columns must have a corresponding outer column to help define the “current row” on which to operate. 
    - If there is no corresponding outer column:
        - If all \<orderBy> columns with no corresponding outer column are from the same table, one row will be returned for every possible combination of existing values of these columns.
        - Otherwise, an error will be returned.
    - If there is more than one corresponding outer column, an error will be returned.

- \<partitionBy> columns must have a corresponding outer column to help define the “current row” on which to operate. If there isn't exactly one corresponding outer column, an error will be returned.

- If the data in an \<orderBy> or \<partitionBy> column is a strict subset of its corresponding outer column, an error will be returned.

- OFFSET can be non-deterministic if there are columns in \<relation> that are neither \<orderBy> nor \<partitionBy> columns. For example, given the following table:

    |Product  |Country  |Sales  |
    |---------|---------|---------|
    |Bike     |    Canada     |    1000     |
    |Bike     |    Canada     |    200     |
    |Bike     |    USA     |    5000     |
    |Bike     |    USA     |    300     |

    The following DAX query:
    
    ```dax
    OFFSET(-1, Table, ORDERBY([Country]), PARTITIONBY([Product])
    ```
    
    For the last two rows, either of the first two rows may be returned as the “previous” row.  

## Example 1

The following DAX query:
  
```dax
DEFINE
VAR vRelation = SUMMARIZECOLUMNS ( 
                    DimProductCategory[EnglishProductCategoryName], 
                    DimDate[CalendarYear], 
                    "Current Sales", SUM(FactInternetSales[SalesAmount]) 
                    )
EVALUATE
ADDCOLUMNS (
    vRelation, 
    "LY Sales", 
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

[]()  
[]()  
