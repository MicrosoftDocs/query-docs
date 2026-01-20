---
description: "Learn more about: ISBOOLEAN"
title: "ISBOOLEAN function (DAX)"
ms.topic: reference
ms.custom: ExampleTypeGeneric
---
# ISBOOLEAN

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Checks whether a value is a logical value, (`TRUE` or `FALSE`), and returns `TRUE` or `FALSE`.

## Syntax

```dax
ISBOOLEAN(<value>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`value`|The value that you want to test.|

## Return value

`TRUE` if the value is a logical value; `FALSE` if any value other than `TRUE` OR `FALSE`.

## Remarks

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
- This function is an alias of [ISLOGICAL](islogical-function-dax.md).

## Example

The following DAX query shows the behavior of ISBOOLEAN.

```dax
EVALUATE
{
    IF ( ISBOOLEAN ( TRUE ), "Is Boolean type or Logical", "Is different type" ), // RETURNS: Is Boolean type or Logical
    IF ( ISBOOLEAN ( FALSE ), "Is Boolean type or Logical", "Is different type" ), // RETURNS: Is Boolean type or Logical
    IF ( ISBOOLEAN ( 42 ), "Is Boolean type or Logical", "Is different type" ) // RETURNS: Is different type
}
```

## Related content
- [ISLOGICAL](islogical-function-dax.md)
- [Information functions](information-functions-dax.md)
