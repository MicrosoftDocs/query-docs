---
description: "Learn more about: NONVISUAL"
title: "NONVISUAL function (DAX)"
ms.topic: reference
---
# NONVISUAL

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Marks a value filter in a [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) expression as non-visual. This function can only be used within a [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) expression.

## Syntax

```dax
NONVISUAL(<expression>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`expression`|Any DAX expression that returns a single value (not a table).|

## Return value

A table of values.

## Remarks

- Marks a value filter in [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) as not affecting measure values, but only applying to group-by columns.

- This function can only be used within a [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) expression. It's used as either a filterTable argument of the [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) function or a groupLevelFilter argument of the [ROLLUPADDISSUBTOTAL](rollupaddissubtotal-function-dax.md) or [ROLLUPISSUBTOTAL](rollupissubtotal-function-dax.md) function.

## Example

See [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md).
