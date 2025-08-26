---
description: "Learn more about: INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES"
title: "INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each general segment map segment metadata storage in the semantic model. This function provides metadata about segment map storage characteristics.

## Syntax

```dax
INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|--------|-------------|
| [ID] | Unique identifier for the general segment map segment metadata storage |
| [SegmentMapStorageID] | Identifier linking to the segment map storage |
| [RecordCount] | Number of records in the segment |
| [Ordinal] | Ordinal position of the segment |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES(),
        "Segment Map Storage ID", [SegmentMapStorageID],
        "Record Count", [RecordCount],
        "Ordinal", [Ordinal]
    )
```

## See also

[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.MEASURES](info-measures-function-dax.md)
[INFO functions overview](info-functions-dax.md)
