---
description: "Learn more about: ERROR"
title: "ERROR function"
ms.topic: reference
---
# ERROR

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Raises an error with an error message.

## Syntax

```dax
ERROR(<text>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`text`|A text string containing an error message.|

## Return value

None

## Remarks

- The ERROR function can be placed in a DAX expression anywhere a scalar value is expected.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example 1

The following DAX query:

```dax
DEFINE
MEASURE DimProduct[Measure] =
        IF(
            SELECTEDVALUE(DimProduct[Color]) = "Red",
            ERROR("red color encountered"),
            SELECTEDVALUE(DimProduct[Color])
        )
EVALUATE SUMMARIZECOLUMNS(DimProduct[Color], "Measure", [Measure])
ORDER BY [Color]
```

Fails and raises and error message containing "red color encountered".

## Example 2

The following DAX query:

```dax
DEFINE
MEASURE DimProduct[Measure] =
        IF(
            SELECTEDVALUE(DimProduct[Color]) = "Magenta",
            ERROR("magenta color encountered"),
            SELECTEDVALUE(DimProduct[Color])
        )
EVALUATE SUMMARIZECOLUMNS(DimProduct[Color], "Measure", [Measure])
ORDER BY [Color]
```

Returns the following table:

DimProduct[Color]  |[Measure]
---------|---------
Black     |        Black
Blue     |       Blue
Grey     |      Grey
Multi     |    Multi
NA     |        NA
Red     |     Red
Silver     |     Silver
Silver\Black     |   Silver\Black
White    |       White
Yellow    |        Yellow

Because Magenta is not one of the product colors, the ERROR function is not executed.
