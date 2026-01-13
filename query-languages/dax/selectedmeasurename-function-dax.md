---
description: "Learn more about: SELECTEDMEASURENAME"
title: "SELECTEDMEASURENAME function (DAX)"
ms.topic: reference
---
# SELECTEDMEASURENAME

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Used by expressions for calculation items to determine the measure that is in context by name.

## Syntax

```dax
SELECTEDMEASURENAME()
```

### Parameters

None

## Return value

A string value holding the name of the measure that is currently in context when the calculation item is evaluated. 

## Remarks

- Can only be referenced in the expression for a calculation item.

- This function is often used for debugging purposes when authoring calculation groups.

## Example

The following calculation item expression checks if the current measure is Expense Ratio and conditionally applies calculation logic. Since the check is based on a string comparison, it is not subject to formula fixup and will not benefit from object renaming being automatically reflected. For a similar comparison that would benefit from formula fixup, please see the ISSLECTEDMEASURE function instead. 

```dax
IF (
    SELECTEDMEASURENAME = "Expense Ratio",
    SELECTEDMEASURE (),
    DIVIDE ( SELECTEDMEASURE (), COUNTROWS ( DimDate ) )
)
```

## Related content

[SELECTEDMEASURE](selectedmeasure-function-dax.md)
[ISSELECTEDMEASURE](isselectedmeasure-function-dax.md) 
