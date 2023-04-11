---
description: "Learn more about: ROWNUMBER"
title: "ROWNUMBER function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax
ms.date: 04/10/2023
ms.topic: reference
author: rahulten
ms.author: owend
recommendations: false

---
# ROWNUMBER

Returns the unique ranking for the current context within the specified partition, sorted by the specified order. If a match cannot be found then then rownumber is blank.
  
## Syntax  
  
```dax
ROWNUMBER ( [<relation>][, <orderBy>][, <blanks>][, <partitionBy>] )
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|relation|(Optional) A table expression from which the output row is returned. </br>If specified, all columns in \<orderBy> and \<partitionBy> must come from it. </br>If omitted: </br>- \<orderBy> must be explicitly specified.</br>- All \<orderBy> and \<partitionBy> columns must be fully qualified and come from a single table. </br>- Defaults to ALLSELECTED() of all columns in \<orderBy> and \<partitionBy>.|
|orderBy|(Optional) An ORDERBY() clause containing the columns that define how each partition is sorted. </br>If omitted: </br>- \<relation> must be explicitly specified. </br>- Defaults to ordering by every column in \<relation> that is not already specified in \<partitionBy>.|
|blanks|(Optional) An enumeration that defines how to handle blank values when sorting. </br>This parameter is reserved for future use. </br>Currently, the only supported value is KEEP (default), where the behavior for numerical/date values is blank values are ordered between zero and negative values. The behavior for strings is blank values are ordered before all strings, including empty strings.|
|partitionBy|(Optional) A PARTITIONBY() clause containing the columns that define how \<relation> is partitioned. </br> If omitted, \<relation> is treated as a single partition. |
  
## Return value

The rownumber number for the current context.
  
## Remarks

Each \<orderBy> and \<partitionBy> column must have a corresponding outer value to help define the current row on which to operate, with the following behavior:

- If there is exactly one corresponding outer column, its value is used.
- If there is no corresponding outer column, then:
  - ROWNUMBER will first determine all \<orderBy> and \<partitionBy> columns that have no corresponding outer column.
  - For every combination of existing values for these columns in ROWNUMBER parent context, ROWNUMBER is evaluated and a row is returned.
  - ROWNUMBER’s final output is a union of these rows.
- If there is more than one corresponding outer column, an error is returned.

If the columns specified within \<orderBy> and \<partitionBy> cannot uniquely identify every row in \<relation>, then:

- ROWNUMBER will try to find the least number of additional columns required to uniquely identify every row.
- If such columns can be found, ROWNUMBER will
  - Try to find the least number of additional columns required to uniquely identify every row.
  - Automatically append these new columns to \<orderBy> clause.
  - Sort each partition using this new set of orderBy columns.
- If such columns cannot be found and the function detects a tie at runtime, an error is returned.

## Example

The following DAX query:
  
```dax
EVALUATE
ADDCOLUMNS(
    'DimGeography',
    "UniqueRank",
    ROWNUMBER(
    	'DimGeography',
    	ORDERBY(
    		'DimGeography'[StateProvinceName], desc,
    		'DimGeography'[City], asc),
    	PARTITIONBY(
    		'DimGeography'[EnglishCountryRegionName])))
ORDER BY [EnglishCountryRegionName] asc, [StateProvinceName] desc, [City] asc
```

Returns a table that uniquely ranks each geography with the same EnglishCountryRegionName, by their StateProvinceName and City.

## See also

[INDEX](index-function-dax.md)  
[ORDERBY](orderby-function-dax.md)  
[PARTITIONBY](partitionby-function-dax.md)  
[WINDOW](window-function-dax.md)  
[RANK](rank-function-dax.md)
