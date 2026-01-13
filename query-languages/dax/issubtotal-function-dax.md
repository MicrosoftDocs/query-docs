---
description: "Learn more about: ISSUBTOTAL"
title: "ISSUBTOTAL function (DAX)"
ms.topic: reference
---
# ISSUBTOTAL

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Creates another column in a [SUMMARIZE](summarize-function-dax.md) expression that returns True if the row contains subtotal values for the column given as argument, otherwise returns False.

## Syntax

```dax
ISSUBTOTAL(<columnName>)
```

With [SUMMARIZE](summarize-function-dax.md),

```dax
SUMMARIZE(<table>, <groupBy_columnName>[, <groupBy_columnName>]…[, ROLLUP(<groupBy_columnName>[,< groupBy_columnName>…])][, <name>, {<expression>|ISSUBTOTAL(<columnName>)}]…)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`columnName`  |The name of any column in table of the SUMMARIZE function or any column in a related table to table.  |

## Return value

A True value if the row contains a subtotal value for the column given as argument, otherwise returns False.

## Remarks

- This function can only be used in the expression of a [SUMMARIZE](summarize-function-dax.md) function.

- This function must be preceded by the name of the Boolean column.

## Example

See [SUMMARIZE](summarize-function-dax.md).
