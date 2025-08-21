---
description: "Learn more about: INFO.FUNCTIONS"
title: "INFO.FUNCTIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.FUNCTIONS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns information about the functions currently available for use in DAX. This corresponds to the MDSCHEMA_FUNCTIONS schema rowset.

## Syntax

```dax
INFO.FUNCTIONS()
```

## Return value

A table whose columns match the MDSCHEMA_FUNCTIONS schema rowset for the current engine/compatibility level.

## Remarks

- The result can vary by engine version and compatibility level.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

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