---
description: "Learn more about: INDEX"
title: "INDEX function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax
ms.date: 04/10/2023
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---

# INDEX

Returns a row at an absolute position, specified by the position parameter, within the specified partition, sorted by the specified order. If the current partition can't be deduced to a single partition, multiple rows may be returned.
  
## Syntax  
  
```dax
INDEX(<position>[, <relation>][, <orderBy>][, <blanks>][, <partitionBy>][, <matchBy>])
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|position|The absolute position (1-based) from which to obtain the data: </br> - \<position> is positive: 1 is the first row, 2 is the second row, etc. </br> -  \<position> is negative: -1 is the last row, -2 is the second last row, etc. </br> When \<position> is out of the boundary, or zero, or BLANK(), INDEX will return an empty table. It can be any DAX expression that returns a scalar value.|
|relation|(Optional) A table expression from which the output is returned. </br> If specified, all columns in \<partitionBy> must come from it or a related table.  </br> If omitted: </br> - \<orderBy> must be explicitly specified. </br> - All \<orderBy> and \<partitionBy> expressions must be fully qualified column names and come from a single table. </br> - Defaults to ALLSELECTED() of all columns in \<orderBy> and \<partitionBy>.
|orderBy|(Optional) An ORDERBY() clause containing the expressions that define how each partition is sorted. </br>If omitted: </br>- \<relation> must be explicitly specified. </br>- Defaults to ordering by every column in \<relation> that is not already specified in \<partitionBy>.|
|blanks|(Optional) An enumeration that defines how to handle blank values when sorting. </br>The supported values are:<ul><li>DEFAULT (the default value), where the behavior for numerical/date values is blank values are ordered between zero and negative values. The behavior for strings is blank values are ordered before all strings, including empty strings.</li><li>FIRST, blanks are always ordered on the end, regardless of ascending or descending sorting order.</li><li>LAST, blanks are always ordered on the beginning, regardless of ascending or descending sorting order. </li></ul></br>Note, when \<blanks> parameter and blanks in ORDERBY() function on individual expression are both specified, \<blanks> on individual orderBy expression takes priority for the relevant orderBy expression, and orderBy expressions without \<blanks> being specified will honor \<blanks> parameter on parent Window function.|
|partitionBy|(Optional) A PARTITIONBY() clause containing the columns that define how \<relation> is partitioned. </br> If omitted, \<relation> is treated as a single partition. |
|matchBy|(Optional) A MATCHBY() clause containing the columns that define how to match data and identify the current row. |  


## Return value

A row at an absolute position.
  
## Remarks

Each \<partitionBy> and \<matchBy> column must have a corresponding outer value to help define the “current partition” on which to operate, with the following behavior:

- If there is exactly one corresponding outer column, its value is used.
- If there is no corresponding outer column:
  - INDEX will first determine all \<partitionBy> and \<matchBy> columns that have no corresponding outer column.
  - For every combination of existing values for these columns in INDEX’s parent context, INDEX is evaluated and a row is returned.
  - INDEX’s final output is a union of these rows.
- If there is more than one corresponding outer column, an error is returned.

If \<matchBy> is present, INDEX will try to use \<matchBy> and \<partitionBy> columns to identify the row.   
If \<matchBy> is not present and the columns specified within \<orderBy> and \<partitionBy> cannot uniquely identify every row in \<relation>:

- INDEX will try to find the least number of additional columns required to uniquely identify every row.
- If such columns can be found, INDEX will automatically append these new columns to \<orderBy>, and each partition is sorted using this new set of OrderBy columns.  
- If such columns cannot be found, an error is returned.

An empty table is returned if:

- The corresponding outer value of a PartitionBy column does not exist within \<relation>.
- The \<position> value refers to a position that does not exist within the partition.  

If INDEX is used within a calculated column defined on the same table as \<relation> and \<orderBy> is omitted, an error is returned.

## Example 1

The following DAX query:
  
```dax
EVALUATE INDEX(1, ALL(DimDate[CalendarYear]))
```

Returns the following table:

|DimDate[CalendarYear]  |
|---------|
|  2005   |

## Example 2

The following DAX query:

```dax
EVALUATE
SUMMARIZECOLUMNS (
    FactInternetSales[ProductKey],
    DimDate[MonthNumberOfYear],
    FILTER (
            VALUES(FactInternetSales[ProductKey]),
            [ProductKey] < 222
    ),
    "CurrentSales", SUM(FactInternetSales[SalesAmount]),
    "LastMonthSales",
    CALCULATE (
        SUM(FactInternetSales[SalesAmount]),
        INDEX(-1, ORDERBY(DimDate[MonthNumberOfYear]))
    )
)
ORDER BY [ProductKey], [MonthNumberOfYear]
```

Returns the following table:

|FactInternetSales[ProductKey]  |DimDate[MonthNumberOfYear]  |[CurrentSales] |[LastMonthSales]  |
|---------|---------|---------|---------|
|214     |    1     |   5423.45     |   8047.7      |
|214     |    2     |   4968.58     |   8047.7      |
|214     |    3     |   5598.4      |   8047.7      |
|214     |    4     |   5073.55     |   8047.7      |
|214     |    5     |   5248.5      |   8047.7      |
|214     |    6     |   7487.86     |   8047.7      |
|214     |    7     |   7382.89     |   8047.7      |
|214     |    8     |   6543.13     |   8047.7      |
|214     |    9     |   6788.06     |   8047.7      |
|214     |   10     |  6858.04      |   8047.7      |
|214     |   11     |  8607.54      |   8047.7      |
|214     |   12     |  8047.7       |   8047.7      |
|217     |   1      |  5353.47      |   7767.78     |
|217     |   2      |  4268.78      |   7767.78     |
|217     |   3      |  5773.35      |   7767.78     |
|217     |   4      |  5738.36      |   7767.78     |
|217     |   5      |  6158.24      |   7767.78     |
|217     |   6      |  6998         |   7767.78     |
|217     |   7      |  5563.41      |   7767.78     |
|217     |   8      |  5913.31      |   7767.78     |
|217     |   9      |  5913.31      |   7767.78     |
|217     |  10      |  6823.05      |   7767.78     |
|217     |  11      |  6683.09      |   7767.78     |
|217     |  12      |  7767.78      |   7767.78     |

## See also

[OFFSET](offset-function-dax.md)  
[ORDERBY](orderby-function-dax.md)  
[PARTITIONBY](partitionby-function-dax.md)  
[WINDOW](window-function-dax.md)  
[RANK](rank-function-dax.md)  
[ROWNUMBER](rownumber-function-dax.md)
