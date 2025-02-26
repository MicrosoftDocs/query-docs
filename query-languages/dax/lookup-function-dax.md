---
description: "Learn more about: LOOKUP"
title: "LOOKUP function (DAX) | Microsoft Docs"
---
# LOOKUP

[!INCLUDE[applies-to-visual-calculations](includes/applies-to-visual-calculations.md)]

Returns a value from a cell in a visual matrix by absolute navigation. You can specify a value as a filter for any axis on the visual matrix. Anything not specified is inferred from the context. If Lookup can’t result in single value, an error is returned.

## Syntax

```dax
LOOKUP(<expression>, <colref>, <expression>[, <colref>, <expression>]...)
```

### Parameters

|Term|Definition|
|--------|--------------|
|expression| The expression that we wants to get. |
|colref|(Optional) The column to be filtered. For example, when we want [Category] = "Bikes", we put [Category] here.|
|expression|(Optional) The value to filter. In above example, put "Bikes" here.|

## Return value

The value of **expression** after filters are applied.

If there isn't a match, an error is returned.

If multiple rows match the filters, an error is returned.

## Example 1

In this example, LOOKUP retrieves the sum of sale for filters: [Category] = "Bikes".
The first argument could be a column or a scalar expression.

```dax
Lookup Example 1 = LOOKUP(SUM([Sales Amount]),  [Category], "Bikes")
Lookup Example 2 = LOOKUP([Sales Amount], [Category], "Bikes")
```

The screenshot below shows the matrix with two visual calculations.

![DAX visual calculation](media/dax-queries/dax-visualcalc-lookup.png)

## Related content

[FIRST](first-function-dax.md)  
[LAST](last-function-dax.md)  
[PREVIOUS](previous-function-dax.md)  
[NEXT](next-function-dax.md)
