---
description: "Learn more about: INFO.LINGUISTICMETADATA"
title: "INFO.LINGUISTICMETADATA function (DAX)"
author: jeroenterheerdt
---
# INFO.LINGUISTICMETADATA

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each linguistic metadata entry in the semantic model. This function provides metadata about linguistic metadata definitions.

## Syntax

```dax
INFO.LINGUISTICMETADATA ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|--------|-------------|
| [ID] | Unique identifier for the linguistic metadata entry |
| [CultureID] | Identifier of the culture associated with this metadata |
| [Content] | Content of the linguistic metadata |
| [ModifiedTime] | Timestamp of when the linguistic metadata was last modified |
| [ContentType] | Type of content stored in the linguistic metadata |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.LINGUISTICMETADATA()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _LinguisticMetadata =
		SELECTCOLUMNS(
			INFO.LINGUISTICMETADATA(),
			"LinguisticMetadataID", [ID],
			"CultureID", [CultureID],
			"Content", [Content]
		)
	VAR _Cultures = 
		SELECTCOLUMNS(
			INFO.CULTURES(),
			"CultureID", [ID],
			"Culture Name", [Name]
		)
	VAR _CombinedTable =
		NATURALLEFTOUTERJOIN(
			_LinguisticMetadata,
			_Cultures
		)
	RETURN
		SELECTCOLUMNS(
			_CombinedTable,
			"Culture Name", [Culture Name],
			"Content Type", [ContentType],
			"Modified Time", [ModifiedTime]
		)
	ORDER BY [Culture Name]
```

## See also

[INFO.CULTURES](info-cultures-function-dax.md)
[INFO.OBJECTTRANSLATIONS](info-objecttranslations-function-dax.md)
[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.MEASURES](info-measures-function-dax.md)
