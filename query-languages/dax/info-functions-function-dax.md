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

A table with the following columns:

| Column | Description |
|--------|-------------|
| [FUNCTION_NAME] | The name of the DAX function |
| [DESCRIPTION] | A description of what the function does |
| [PARAMETER_LIST] | The list of parameters the function accepts |
| [RETURN_TYPE] | The data type that the function returns |
| [ORIGIN] | The origin or source of the function |
| [INTERFACE_NAME] | The interface name for the function |
| [LIBRARY_NAME] | The library containing the function |
| [DLL_NAME] | The DLL file containing the function implementation |
| [HELP_FILE] | The help file associated with the function |
| [HELP_CONTEXT] | The help context identifier |
| [OBJECT] | The object information for the function |
| [CAPTION] | The display caption for the function |
| [PARAMETERINFO] | Additional parameter information |
| [DIRECTQUERY_PUSHABLE] | Whether the function can be pushed down to DirectQuery sources |
| [VISUAL_CALCULATIONS_INFO] | Information about visual calculations support |

## Remarks

- The result can vary by engine version and compatibility level.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.FUNCTIONS()
```

## Example 2 - DAX query with filters

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
    SELECTCOLUMNS(
        FILTER(
            INFO.FUNCTIONS(),
            CONTAINSSTRING([FUNCTION_NAME], "DATE")
        ),
        "Function Name", [FUNCTION_NAME],
        "Description", [DESCRIPTION],
        "Return Type", [RETURN_TYPE]
    )
ORDER BY [Function Name]
```
## See also

[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.MEASURES](info-measures-function-dax.md)
[INFO functions overview](info-functions-dax.md)
