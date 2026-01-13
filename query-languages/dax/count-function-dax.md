---
description: "Learn more about: COUNT"
title: "COUNT function (DAX)"
ms.topic: reference
---
# COUNT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Counts the number of rows in the specified column that contain non-blank values.

## Syntax

```dax
COUNT(<column>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`column`|The column that contains the values to be counted.|

## Return value

A whole number.

## Remarks

- The only argument allowed to this function is a column. The COUNT function counts rows that contain the following kinds of values:

  - Numbers
  - Dates
  - Strings

- When the function finds no rows to count, it returns a blank.

- Blank values are skipped. `TRUE`/`FALSE` values are not supported.

- If you want to evaluate a column of `TRUE`/`FALSE` values, use the COUNTA function.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

- For best practices when using COUNT, see [Use COUNTROWS instead of COUNT](best-practices/dax-countrows.md).

## Example

The following example shows how to count the number of values in the column, ShipDate.

```dax
= COUNT([ShipDate])
```

To count logical values or text, use the COUNTA or COUNTAX functions.

## Related content

[COUNTA function](counta-function-dax.md)
[COUNTAX function](countax-function-dax.md)
[COUNTX function](countx-function-dax.md)
[Statistical functions](statistical-functions-dax.md)
