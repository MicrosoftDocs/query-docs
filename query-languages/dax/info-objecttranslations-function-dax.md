---
description: "Learn more about: INFO.OBJECTTRANSLATIONS"
title: "INFO.OBJECTTRANSLATIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.OBJECTTRANSLATIONS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each object translation in the semantic model. This function provides metadata about translations for model objects.

## Syntax

```dax
INFO.OBJECTTRANSLATIONS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Data Type | Description |
|--------|-----------|-------------|
| [ID] | Integer | Unique identifier for the object translation |
| [CultureID] | Integer | ID of the culture this translation applies to |
| [ObjectID] | Integer | ID of the object being translated |
| [ObjectType] | Integer | Type of object being translated |
| [Property] | String | Property name that is being translated |
| [Value] | String | Translated value for the property |
| [ModifiedTime] | DateTime | Date and time when the translation was last modified |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.OBJECTTRANSLATIONS()
```