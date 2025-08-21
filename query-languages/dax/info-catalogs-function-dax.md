---
description: "Learn more about: INFO.CATALOGS"
title: "INFO.CATALOGS function (DAX)"
author: jeroenterheerdt
---
# INFO.CATALOGS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each catalog in the semantic model. This function provides metadata about the catalogs available in the current context.

## Syntax

```dax
INFO.CATALOGS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column name | Data type | Description |
|-------------|-----------|-------------|
| [CATALOG_NAME] | String | The name of the catalog |
| [DESCRIPTION] | String | The description of the catalog |
| [ROLES] | String | The roles associated with the catalog |
| [DATE_MODIFIED] | DateTime | The date and time when the catalog was last modified |
| [COMPATIBILITY_LEVEL] | Integer | The compatibility level of the catalog |
| [TYPE] | Integer | The type of the catalog |
| [VERSION] | Integer | The version of the catalog |
| [DATABASE_ID] | String | The unique identifier of the database |
| [DATABASE_GUID] | String | The GUID of the database |
| [DATE_QUERIED] | DateTime | The date and time when the catalog was queried |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.CATALOGS()
```