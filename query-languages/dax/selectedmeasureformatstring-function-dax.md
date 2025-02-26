---
description: "Learn more about: SELECTEDMEASUREFORMATSTRING"
title: "SELECTEDMEASUREFORMATSTRING function (DAX)"
---
# SELECTEDMEASUREFORMATSTRING

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Used by expressions for calculation items to retrieve the format string of the measure that is in context.

## Syntax

```dax
SELECTEDMEASUREFORMATSTRING()
```

### Parameters

None

## Return value

A string holding the format string of the measure that is currently in context when the calculation item is evaluated.

## Remarks

- This function can only be referenced in expressions for calculation items in calculation groups. It is designed to be used by the **Format String Expression** property of calculation items.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following expression is evaluated by the Format String Expression property for a calculation item. If there is a single currency in filter context, the format string is retrieved from the DimCurrency[FormatString] column; otherwise the format string of the measure in context is used.

```dax
SELECTEDVALUE( DimCurrency[FormatString], SELECTEDMEASUREFORMATSTRING() )
```

## Related content

[SELECTEDMEASURE](selectedmeasure-function-dax.md)
[ISSELECTEDMEASURE](isselectedmeasure-function-dax.md) 
