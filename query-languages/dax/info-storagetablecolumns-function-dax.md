---
description: "Learn more about: INFO.STORAGETABLECOLUMNS"
title: "INFO.STORAGETABLECOLUMNS function (DAX)"
author: jeroenterheerdt
---
# INFO.STORAGETABLECOLUMNS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about all table storage in the semantic model. This information helps you understand the model.

## Syntax

```dax
INFO.STORAGETABLECOLUMNS([<Restriction name>, <Restriction value>], ...)
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
|[ATTRIBUTE_NAME]|The name of the attribute|
|[TABLE_ID]|The ID of the table|
|[COLUMN_ID]|The ID of the column|
|[COLUMN_TYPE]|The type of the column. The values are as follows:<br/>BASIC_DATA – This column contains data provided by an external data source.<br/>CALCULATED_DATA – This column contains data created by calculations.<br/>RELATIONSHIP – This column contains information about relationship between tables.<br/>HIERARCHY_POSITION_TO_DATAID –This column contains information mapping position of a value in the hierarchy to the Data ID.<br/>HIERARCHY_DATAID_TO_POSITION –This column contains information mapping a Data ID to the position of a valuein the hierarchy.<br/>UNKNOWN – The column type is not known.|
|[COLUMN_ENCODING]|The encoding method used on the column. The method can be one of the following:<br/>0 – The system automatically selects a column encoding.<br/>1 – The column uses hash encoding.<br/>2 – The column uses value encoding.|
|[DATATYPE]|The type of the column data. The values are as follows:<br/>N/A – Indicates that no data type information is available.<br/>DBTYPE_EMPTY - Indicates that no value was specified.<br/>DBTYPE_I2 - Indicates a two-byte signed integer.<br/>DBTYPE_I4 - Indicates a four-byte signed integer.<br/>DBTYPE_R4 - Indicates a single-precision floating-point value.<br/>DBTYPE_R8 - Indicates a double-precision floating-point value.<br/>DBTYPE_CY - Indicates a currency value. Currency is a fixed-point number that has four digits to the right of the decimal point and that is stored in an eight-byte signed integer scaled by 10,000.<br/>DBTYPE_DATE - Indicates a date value. Date values are stored as Double, the whole part of which is th enumber of days since December 30, 1899, and the fractional part of which is the fraction of a day.<br/>DBTYPE_BSTR - Indicates  anull-terminated character string (Unicode).<br/>DBTYPE_ERROR - Indicates a 32-bit error code.<br/>DBTYPE_BOOL - Indicates a Boolean value.<br/>DBTYPE_DECIMAL - Indicates an exact numeric value with a fixed precision and scale. The scale is between 0 and 28.<br/>DBTYPE_I1 - Indicates a one-byte signed integer.<br/>DBTYPE_UI1 - Indicates a one-byte unsigned integer.<br/>DBTYPE_UI2 - Indicates a two-byte unsigned integer.<br/>DBTYPE_UI4 - Indicates a four-byte unsigned integer.<br/>DBTYPE_I8 - Indicates an eight-byte signed integer.<br/>DBTYPE_UI8 - Indicates an eight-byte unsigned integer.<br/>DBTYPE_GUID - Indicates a GUID.<br/>DBTYPE_BYTES - Indicates a binary value.<br/>DBTYPE_STR - Indicates a string value.<br/>DBTYPE_WSTR - Indicates a null-terminated Unicode character string.<br/>DBTYPE_NUMERIC - Indicates an exact numeric value with a fixed precision and scale. The scale is between  0and 38.<br/>DBTYPE_DBDATE - Indicates a date value (yyyymmdd).<br/>DBTYPE_DBTIME - Indicates a time value (hhmmss).<br/>DBTYPE_DBTIMESTAMP - Indicates a date-time stamp (yyyymmddhhmmss plus a fraction in billionths)|
|[ISKEY]|Indicates whether the column is a key column|
|[ISUNIQUE]|Indicates whether the column contains unique values|
|[ISNULLABLE]|Indicates whether the column can contain NULL values|
|[ISROWNUMBER]|Indicates whether the column is a Row Number column|
|[DICTIONARY_SIZE]|Indicates the amount of memory that is used by the dictionary data structure associated with the column, in bytes. The dictionary data structure maps column data IDs to the actual values|
|[DICTIONARY_ISPAGEABLE]|Indicates the Vertipaq Data Paging (VDP) state of the dictionary, which specifies whether the dictionary is pageable. If the VDPstate of the dictionary is unknown, the default value is NULL. Otherwise, the value is a Boolean|
|[DICTIONARY_ISRESIDENT]|Indicates the VDP state of the dictionary, which specifies whether the dictionary is resident. If the VDP state of the dictionary is unknown, the default value is NULL. Otherwise, the value is a Boolean|
|[DICTIONARY_TEMPERATURE]|Indicates the scaled numeric value of the frequency of dictionary access. The value is based on the most recent access time and usage. This column has a numeric value only if the dictionary is pageable and has been loaded at least once; otherwise, the value is NULL|
|[DICTIONARY_LAST_ACCESSED]|Indicates the most recent time the dictionary was accessed. For non-pageable tables in the dictionary, the DICTIONARY_LAST_ACCESSED value is NULL. For pageable tables in the dictionary, DICTIONARY_LAST_ACCESSED value NULL denotes the table has not been loaded since server startup|

## Remarks

Can only be run by users with write permission on the semantic model and not when live connected to the semantic model in Power BI Desktop. This function can be used in [DAX queries](/dax/dax-queries), and can't be used in calculations.

## Example 1 - DAX query

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.STORAGETABLECOLUMNS()
```
## See also

- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
- [INFO.MEASURES](info-measures-function-dax.md)
- [INFO functions overview](info-functions-dax.md)
