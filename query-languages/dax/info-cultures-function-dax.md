---
description: "Learn more about: INFO.CULTURES"
title: "INFO.CULTURES function (DAX)"
author: jeroenterheerdt
---
# INFO.CULTURES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each culture in the semantic model. This function provides metadata about the cultures and locales supported by the model.

## Syntax

```dax
INFO.CULTURES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| [ID] | Integer | Unique identifier for the culture |
| [ModelID] | Integer | Identifier of the semantic model |
| [Name] | String | Name of the culture (e.g., en-US) |
| [LinguisticMetadataID] | Integer | Identifier for linguistic metadata associated with the culture |
| [ModifiedTime] | DateTime | Date and time when the culture was last modified |
| [StructureModifiedTime] | DateTime | Date and time when the culture structure was last modified |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.CULTURES()
```
