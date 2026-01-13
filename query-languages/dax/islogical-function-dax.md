---
description: "Learn more about: ISLOGICAL"
title: "ISLOGICAL function (DAX)"
ms.topic: reference
ms.custom: ExampleTypeGeneric
---
# ISLOGICAL

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Checks whether a value is a logical value, (`TRUE` or `FALSE`), and returns `TRUE` or `FALSE`.

## Syntax

```dax
ISLOGICAL(<value>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`value`|The value that you want to test.|

## Return value

`TRUE` if the value is a logical value; `FALSE` if any value other than `TRUE` OR `FALSE`.

## Remarks

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
- This function is an alias of [ISBOOLEAN](isboolean-function-dax.md).

## Example

The following DAX query shows the behavior of ISLOGICAL.

```dax
EVALUATE
{
    IF ( ISLOGICAL ( TRUE ), "Is Boolean type or Logical", "Is different type" ), // RETURNS: Is Boolean type or Logical
    IF ( ISLOGICAL ( FALSE ), "Is Boolean type or Logical", "Is different type" ), // RETURNS: Is Boolean type or Logical
    IF ( ISLOGICAL ( 42 ), "Is Boolean type or Logical", "Is different type" ) // RETURNS: Is different type
}
```

## Related content
- [ISBOOLEAN](isboolean-function-dax.md)
- [Information functions](information-functions-dax.md)
