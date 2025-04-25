---
description: "Learn more about: INFO.STORAGETABLECOLUMNSEGMENTS"
title: "INFO.STORAGETABLECOLUMNSEGMENTS function (DAX)"
author: jeroenterheerdt
---
# INFO.STORAGETABLECOLUMNSEGMENTS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about all table storage in the semantic model. This information helps you understand the model.

## Syntax

```dax
INFO.STORAGETABLECOLUMNSEGMENTS([<Restriction name>, <Restriction value>], ...)
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

|Column|Description|
|---|---|
|[DATABASE_NAME]|The name of the database|
|[CUBE_NAME]|The name of the cube|
|[MEASURE_GROUP_NAME]|The name of the measure group|
|[DIMENSION_NAME]|The name of the dimension|
|[TABLE_ID]|The ID of the table|
|[COLUMN_ID]|The ID of the column|
|[SEGMENT_NUMBER]|The numeric value of the segment|
|[TABLE_PARTITION_NUMBER]|The numeric value of the partition table|
|[RECORDS_COUNT]|The number of records|
|[ALLOCATED_SIZE]|The size of allocated data|
|[USED_SIZE]|The size of the data used|
|[COMPRESSION_TYPE]|The type of compression. This value is always "NOSPLIT" and for internal use only|
|[BITS_COUNT]|The count of bits required to store the Data IDs|
|[BOOKMARK_BITS_COUNT]|The bookmark count of BITS|
|[VERTIPAQ_STATE]|The state of the VertiPaq compression for this columnsegment. The value is one of the following:<br/>**COMPLETED** – The VertiPaqcompression completed successfully<br/> **TIMEBOXED** – The VertiPaqcompression was timeboxed<br/> **SKIPPED** – The VertiPaqcompression was skipped|
|[ISPAGEABLE]|When true, may indicate that the segment is pageable; otherwise, false. If the pagingfeature is not supported on the server, the value is NULL|
|[ISRESIDENT]|When true, may indicate that the segment is resident; otherwise, false. If the pagingfeature is not supported on the server, the value is NULL|
|[TEMPERATURE]|When the segment is pageable and is resident, may indicate the scaled numericvalue of the frequency of segment access considering the last access time andusage; otherwise, NULL|
|[LAST_ACCESSED]|For a pageable segment, may indicate the last accesstime of a segment if it has been paged in at least once; otherwise, NULL. Fora non-pageable segment, the value is always NULL|


## Remarks

Can only be ran by users with write permission on the semantic model and not when live connected to the semantic model in Power BI Desktop. This function can be used in [DAX queries](/dax/dax-queries), and can't be used in calculations.

## Example 1 - DAX query

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.STORAGETABLECOLUMNSEGMENTS()
```