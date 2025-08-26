---
description: "Learn more about: INFO.MEASURES"
title: "INFO.MEASURES function (DAX)"
author: jeroenterheerdt
---
# INFO.MEASURES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each measure in the semantic model, with columns that match the schema rowset for measure objects (for example, name, expression, and state).

## Syntax

```dax
INFO.MEASURES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|--------|-------------|
| [ID] | Unique identifier for the measure |
| [TableID] | Identifier of the table containing the measure |
| [Name] | Name of the measure |
| [Description] | Description of the measure |
| [DataType] | Data type of the measure result |
| [Expression] | DAX expression defining the measure calculation |
| [FormatString] | Format string for displaying measure values |
| [IsHidden] | Boolean indicating if the measure is hidden from client tools |
| [State] | Current state of the measure (e.g., Ready, Processing, Error) |
| [ModifiedTime] | Timestamp of when the measure was last modified |
| [StructureModifiedTime] | Timestamp of when the measure structure was last modified |
| [KPIID] | Identifier of the KPI associated with this measure (if applicable) |
| [IsSimpleMeasure] | Boolean indicating if this is a simple measure |
| [ErrorMessage] | Error message if the measure is in an error state |
| [DisplayFolder] | Display folder for organizing measures in client tools |
| [DetailRowsDefinitionID] | Identifier of the detail rows definition for this measure |
| [DataCategory] | Data category classification for the measure |
| [LineageTag] | Lineage tag for tracking data lineage |
| [SourceLineageTag] | Source lineage tag from the original data source |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.MEASURES()
```

## See also

[INFO.CALCULATIONGROUPS](info-calculationgroups-function-dax.md)
[INFO.CALCULATIONITEMS](info-calculationitems-function-dax.md)
[INFO.KPIS](info-kpis-function-dax.md)
[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
