---
description: "Learn more about: INFO.USERDEFINEDFUNCTIONS"
title: "INFO.USERDEFINEDFUNCTIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.USERDEFINEDFUNCTIONS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each user-defined function in the semantic model, with columns that match the schema rowset for user-defined function objects (for example, name, expression, and state).

## Syntax

```dax
INFO.USERDEFINEDFUNCTIONS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|--------|-------------|
| [ID] | Unique identifier for the user-defined function |
| [ModelID] | Identifier of the model containing the user-defined function |
| [Name] | Name of the user-defined function |
| [Description] | Description of the user-defined function |
| [Expression] | DAX expression defining the user-defined function |
| [IsHidden] | Boolean indicating if the user-defined function is hidden from client tools |
| [State] | Current state of the user-defined function (e.g., Ready, Error) |
| [ErrorMessage] | Error message if the user-defined function is in an error state |
| [ModifiedTime] | Timestamp of when the user-defined function was last modified |
| [StructureModifiedTime] | Timestamp of when the user-defined function structure was last modified |
| [LineageTag] | Lineage tag for tracking data lineage |
| [SourceLineageTag] | Source lineage tag from the original data source |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.USERDEFINEDFUNCTIONS()
```

## See also

- [INFO.FUNCTIONS](info-functions-function-dax.md)
- [INFO.MEASURES](info-measures-function-dax.md)