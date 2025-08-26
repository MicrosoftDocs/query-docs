---
description: "Learn more about: INFO.FUNCTIONS"
title: "INFO.FUNCTIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.FUNCTIONS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns information about the functions currently available for use in DAX. This corresponds to the MDSCHEMA_FUNCTIONS schema rowset.

## Syntax

```dax
INFO.FUNCTIONS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the MDSCHEMA_FUNCTIONS schema rowset for the current engine/compatibility level.

## Remarks

- The result can vary by engine version and compatibility level.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.FUNCTIONS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.FUNCTIONS(),
        "FUNCTION_NAME", [FUNCTION_NAME],
        "DESCRIPTION", [DESCRIPTION],
        "CAPTION", [CAPTION]
    )
```
## See also

[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.MEASURES](info-measures-function-dax.md)
[INFO functions overview](info-functions-dax.md)
