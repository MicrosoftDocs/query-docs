---
description: "Learn more about: TREATAS"
title: "TREATAS function"
ms.topic: reference
---
# TREATAS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Applies the result of a table expression as filters to columns from an unrelated table. 

## Syntax

```dax
TREATAS(table_expression, <column>[, <column>[, <column>[,…]]])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`table_expression`|An expression that results in a table.|
|`column`|One or more existing columns. It cannot be an expression. |

## Return value

A table that contains all the rows in column(s) that are also in table_expression.

## Remarks

- The number of columns specified must match the number of columns in the table expression and be in the same order.

- If a value returned in the table expression does not exist in the column, it is ignored. For example, TREATAS({"Red", "Green", "Yellow"}, DimProduct[Color]) sets a filter on column DimProduct[Color] with three values "Red", "Green", and "Yellow". If "Yellow" does not exist in  DimProduct[Color], the effective filter values would be "Red" and "Green".

- Best for use when a relationship does not exist between the tables. If you have multiple relationships between the tables involved, consider using [USERELATIONSHIP](userelationship-function-dax.md) instead.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

In the following example, the model contains two unrelated product tables. If a user applies a filter to DimProduct1[ProductCategory] selecting Bikes, Seats, Tires, the same filter, Bikes, Seats, Tires is applied to DimProduct2[ProductCategory].

```dax
CALCULATE(
    SUM(Sales[Amount]),
    TREATAS(
        VALUES(DimProduct1[ProductCategory]),
        DimProduct2[ProductCategory]
    )
)
```

## Related content

[INTERSECT](intersect-function-dax.md)
[FILTER](filter-function-dax.md)
[USERELATIONSHIP](userelationship-function-dax.md)
