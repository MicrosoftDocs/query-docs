---
description: "Learn more about: INFO.CALCULATIONGROUPS"
title: "INFO.CALCULATIONGROUPS function (DAX)"
author: jeroenterheerdt
---
# INFO.CALCULATIONGROUPS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each calculation group in the semantic model. This function provides metadata about calculation groups and their properties.

## Syntax

```dax
INFO.CALCULATIONGROUPS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| [ID] | Integer | The unique identifier of the calculation group |
| [TableID] | Integer | The unique identifier of the table that contains the calculation group |
| [Description] | String | The description of the calculation group |
| [ModifiedTime] | DateTime | The date and time when the calculation group was last modified |
| [Precedence] | Integer | The precedence value of the calculation group for evaluation order |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.CALCULATIONGROUPS()
```