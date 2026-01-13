---
description: "Learn more about: FIRSTNONBLANKVALUE"
title: "FIRSTNONBLANKVALUE function (DAX)"
ms.topic: reference
---
# FIRSTNONBLANKVALUE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Evaluates an expression filtered by the sorted values of a column and returns the first value of the expression that is not blank.

## Syntax

```dax
FIRSTNONBLANKVALUE(<column>, <expression>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`column`|A column or an expression that returns a single-column table.|
|`expression`|An expression evaluated for each value of `column`.|

## Return value

The first non-blank value of `expression` corresponding to the sorted values of `column`.

## Remarks

- The column argument can be any of the following:
  - A reference to any column.
  - A table with a single column.

- This function is different from FIRSTNONBLANK in that the `column` is added to the filter context for the evaluation of `expression`.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following DAX query,

```dax
EVALUATE 
SUMMARIZECOLUMNS(
  DimProduct[Class],
  "FNBV",
  FIRSTNONBLANKVALUE(
    DimDate[Date],
    SUM(FactInternetSales[SalesAmount])
   )
)
```

Returns,

|DimProduct[Class]|[FNBV]|
|-----------|---------------|----------|
|L|699.0982|
|H|13778.24|
|M|1000.4375|
||533.83|
