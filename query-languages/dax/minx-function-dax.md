---
description: "Learn more about: MINX"
title: "MINX function (DAX)"
ms.topic: reference
---
# MINX

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the lowest value that results from evaluating an expression for each row of a table.

## Syntax

```dax
MINX(<table>, < expression>,[<variant>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`table`|The table containing the rows for which the expression will be evaluated.|
|`expression`|The expression to be evaluated for each row of the table.|
|`variant`|(Optional) If `TRUE`, and if there are variant or mixed value types, the lowest value based on ORDER BY ASC is returned.|

## Return value

The lowest value.

## Remarks

- The MINX function takes as its first argument a table or an expression that returns a table. The second argument contains the expression that is evaluated for each row of the table.

- Blank values are skipped. `TRUE`/`FALSE` values are not supported.

- If the expression has variant or mixed value types such as text and number, then by default MINX considers only numbers. If `<variant> = TRUE`, the minimum value is returned.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example 1

The following example filters the InternetSales table and returns only rows for a specific sales territory. The formula then finds the minimum value in the Freight column.

```dax
= MINX( FILTER(InternetSales, [SalesTerritoryKey] = 5),[Freight])
```

## Example 2

The following example uses the same filtered table as in the previous example, but instead of merely looking up values in the column for each row of the filtered table, the function calculates the sum of two columns, Freight and TaxAmt, and returns the lowest value resulting from that calculation.

```dax
= MINX( FILTER(InternetSales, InternetSales[SalesTerritoryKey] = 5), InternetSales[Freight] + InternetSales[TaxAmt])
```

In the first example, the names of the columns are unqualified. In the second example, the column names are fully qualified.

## Related content

[MIN function](min-function-dax.md)
[MINA function](mina-function-dax.md)
[Statistical functions](statistical-functions-dax.md)
