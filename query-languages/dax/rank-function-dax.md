---
description: "Learn more about: RANK"
title: "RANK function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax
ms.date: 04/10/2023
ms.topic: reference
author: rahulten
ms.author: owend
recommendations: false

---

# RANK

Returns the ranking for the current context within the specified partition, sorted by the specified order. If a match cannot be found then then rank is blank.
  
## Syntax  
  
```dax
RANK ( [<ties>][, <relation>][, <orderBy>][, <blanks>][, <partitionBy>][, <matchBy>] )
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|ties|(Optional) Defines how to handle the ranking when two or more rows are tied. </br>If specified, the supported value is either DENSE, or SKIP. </br>If omitted:</br>- Defaults to SKIP |
|relation|(Optional) A table expression from which the output row is returned. </br>If specified, all columns in \<orderBy> and \<partitionBy> must come from it. </br>If omitted: </br>- \<orderBy> must be explicitly specified.</br>- All \<orderBy> and \<partitionBy> columns must be fully qualified and come from a single table. </br>- Defaults to ALLSELECTED() of all columns in \<orderBy> and \<partitionBy>.|
|orderBy|(Optional) An ORDERBY() clause containing the columns that define how each partition is sorted. </br>If omitted: </br>- \<relation> must be explicitly specified. </br>- Defaults to ordering by every column in \<relation> that is not already specified in \<partitionBy>.|
|blanks|(Optional) An enumeration that defines how to handle blank values when sorting. </br>This parameter is reserved for future use. </br>Currently, the only supported value is KEEP (default), where the behavior for numerical/date values is blank values are ordered between zero and negative values. The behavior for strings is blank values are ordered before all strings, including empty strings.|
|partitionBy|(Optional) A PARTITIONBY() clause containing the columns that define how \<relation> is partitioned. </br> If omitted, \<relation> is treated as a single partition. |
|matchBy|(Optional) A MATCHBY() clause containing the columns that define how to match data and identify the current row. |
  
## Return value

The rank number for the current context.
  
## Remarks

- Each \<orderBy> and \<partitionBy> column must have a corresponding outer value to help define the current row on which to operate, with the following behavior:

  - If there is exactly one corresponding outer column, its value is used.
  - If there is no corresponding outer column, then:
    - RANK will first determine all \<orderBy> and \<partitionBy> columns that have no corresponding outer column.
    - For every combination of existing values for these columns in RANK parent context, RANK is evaluated and a row is returned.
    - RANK’s final output is a rank number.
- If \<matchBy> is present, then RANK will try to use columns in \<matchBy> and \<partitionBy> to idenfity the current row.
- If \<matchBy> is not present and the columns specified within \<orderBy> and \<partitionBy> cannot uniquely identify every row in \<relation>, then two or more rows may have the same ranking and the ranking will be determined by the ties parameter.
- RANK returns a blank value for total rows. It's recommended that you test your expression thoroughly.
- RANK does not compare to RANKX as SUM compares to SUMX.

## Example

The following DAX query:
  
```dax
EVALUATE
ADDCOLUMNS(
    'DimGeography',
    "Rank",
    RANK(
    	DENSE,
    	'DimGeography',
    	ORDERBY(
    		'DimGeography'[StateProvinceName], desc,
    		'DimGeography'[City], asc),
    	PARTITIONBY(
    		'DimGeography'[EnglishCountryRegionName])))
ORDER BY [EnglishCountryRegionName] asc, [StateProvinceName] desc, [City] asc
```

Returns a table that ranks each geography with the same EnglishCountryRegionName, by their StateProvinceName and City.

## See also

[INDEX](index-function-dax.md)  
[ORDERBY](orderby-function-dax.md)  
[PARTITIONBY](partitionby-function-dax.md)  
[WINDOW](window-function-dax.md)  
[ROWNUMBER](rownumber-function-dax.md)
