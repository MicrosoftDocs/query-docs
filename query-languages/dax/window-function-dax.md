---
description: "Learn more about: WINDOW"
title: "WINDOW function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax
ms.date: 11/14/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---

# WINDOW

Returns multiple rows which are positioned within the given interval.

## Syntax  
  
```dax
WINDOW ( from[, from_type], to[, to_type][, <relation>][, <orderBy>][, <blanks>][, <partitionBy>] )
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|from|Indicates where the window starts. It can be any DAX expression that returns a scalar value. </br>The behavior depends on the \<from_type> parameter: </br> - If \<from_type> is REL, the number of rows to go back (negative value) or forward (positive value) from the current row to get the first row in the window. </br> - If \<from_type> is ABS, and \<from> is positive, then it’s the position of the start of the window from beginning of the partition. Indexing is 1-based. For example, 1 means window starts from the beginning of the partition.  If \<from> is negative, then it’s the position of the start of the window from the end of the partition. -1 means the last row in the partition.  |
|from_type |Modifies behavior of the \<from> parameter. Possible values are ABS (absolute) and REL (relative). Default is REL.|
|to|Same as \<from>, but indicates the end of the window. The last row is included in the window.|
|to_type|Same as \<from_type>, but modifies the behavior of \<to>.|
|relation|(Optional) A table expression from which the output row is returned. </br>If specified, all columns in \<orderBy> and \<partitionBy> must come from it. </br>If omitted: </br>- \<orderBy> must be explicitly specified.</br>- All \<orderBy> and \<partitionBy> columns must be fully qualified and come from a single table. </br>- Defaults to ALLSELECTED() of all columns in \<orderBy> and \<partitionBy>.|
|orderBy|(Optional) An ORDERBY() clause containing the columns that define how each partition is sorted. </br>If omitted: </br>- \<relation> must be explicitly specified. </br>- Defaults to ordering by every column in \<relation> that is not already specified in \<partitionBy>.|
|blanks|(Optional) An enumeration that defines how to handle blank values when sorting. </br>This parameter is reserved for future use. </br>Currently, the only supported value is KEEP (default), where the behavior for numerical/date values is blank values are ordered between zero and negative values. The behavior for strings is blank values are ordered before all strings, including empty strings.|
|partitionBy|(Optional) A PARTITIONBY() clause containing the columns that define how \<relation> is partitioned. If omitted, \<relation> is treated as a single partition.|

## Return value

All rows from the window.

## Remarks

Each \<orderBy> and \<partitionBy> column must have a corresponding outer value to help define the current row on which to operate. If \<from_type> and \<to_type> both have value ABS, then the following applies only to the \<partitionBy> columns:

- If there is exactly one corresponding outer column, its value is used.
- If there is no corresponding outer column:
  - WINDOW will first determine all \<orderBy> and \<partitionBy> columns that have no corresponding outer column.
  - For every combination of existing values for these columns in WINDOW’s parent context, WINDOW is evaluated, and the corresponding rows is returned.
  - WINDOW final output is a union of these rows. 
- If there is more than one corresponding outer column, an error is returned.

If the columns specified within \<orderBy> and \<partitionBy> cannot uniquely identify every row in \<relation>, then:

- WINDOW will try to find the least number of additional columns required to uniquely identify every row.
- If such columns can be found, WINDOW will automatically append these new columns to \<orderBy>, and each partition is sorted using this new set of orderBy columns.  
- If such columns cannot be found, an error is returned.

An empty table is returned if:

- The corresponding outer value of an \<orderBy> or \<partitionBy> column does not exist within \<relation>.
- The whole window is outside the partition, or the beginning of the window is after its ending.

If WINDOW is used within a calculated column defined on the same table as \<relation>, and \<orderBy> is omitted, an error is returned.

If the beginning of the window turns out be before the first row, then it’s set to the first row. Similarly, if the end of the window is after the last row of the partition, then it's set to the last row.

## Example

The following measure:
  
```dax
3-day Average Price = 
AVERAGEX(
    WINDOW(
        -2,REL,0,REL,
        SUMMARIZE(ALLSELECTED('Sales'), 'Date'[Date], 'Product'[Product]),
        ORDERBY('Date'[Date]),
        KEEP,
        PARTITIONBY('Product'[Product])
    ), 
    CALCULATE(AVERAGE(Sales[Unit Price]))
)

```

Returns the 3-day average of unit prices for each product. Note the 3-day window consists of three days in which the product has sales, not necessarily three consecutive calendar days.

## See also

[INDEX](index-function-dax.md)  
[OFFSET](offset-function-dax.md)  
[ORDERBY](orderby-function-dax.md)  
[PARTITIONBY](partitionby-function-dax.md)  
