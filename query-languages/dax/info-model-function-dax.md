---
description: "Learn more about: INFO.MODEL"
title: "INFO.MODEL function (DAX)"
author: jeroenterheerdt
---
# INFO.MODEL

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about the model in the semantic model. This function provides metadata about the model itself and its properties.

## Syntax

```dax
INFO.MODEL ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Data Type | Description |
|--------|-----------|-------------|
| [ID] | Integer | Unique identifier for the model |
| [Name] | String | Name of the model |
| [Description] | String | Description of the model |
| [StorageLocation] | Integer | Storage location indicator |
| [DefaultMode] | Integer | Default processing mode for the model |
| [DefaultDataView] | Integer | Default data view setting |
| [Culture] | String | Culture identifier for the model (e.g., "en-US") |
| [Collation] | String | Collation setting for the model |
| [ModifiedTime] | DateTime | Date and time when the model was last modified |
| [StructureModifiedTime] | DateTime | Date and time when the model structure was last modified |
| [Version] | Integer | Version number of the model |
| [DataAccessOptions] | String | JSON object containing data access configuration options |
| [DefaultMeasureID] | Integer | ID of the default measure, if any |
| [DefaultPowerBIDataSourceVersion] | Integer | Default Power BI data source version |
| [ForceUniqueNames] | Boolean | Whether unique names are enforced |
| [DiscourageImplicitMeasures] | Boolean | Whether implicit measures are discouraged |
| [DataSourceVariablesOverrideBehavior] | Integer | Behavior for data source variable overrides |
| [DataSourceDefaultMaxConnections] | Integer | Default maximum connections for data sources |
| [SourceQueryCulture] | String | Culture used for source queries |
| [MAttributes] | String | Model attributes |
| [DiscourageCompositeModels] | Boolean | Whether composite models are discouraged |
| [AutomaticAggregationOptions] | String | Options for automatic aggregations |
| [DisableAutoExists] | Integer | Auto exists disable setting |
| [VersionMarker] | String | Version marker for the model |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.MODEL()
```
## See also

- [INFO.PROPERTIES](info-properties-function-dax.md)
- [INFO.EXPRESSIONS](info-expressions-function-dax.md)
- [INFO.CATALOGS](info-catalogs-function-dax.md)
- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
