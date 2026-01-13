---
description: "Learn more about: QUARTER"
title: "QUARTER function (DAX)"
ms.topic: reference
---

# QUARTER

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the quarter as a number from 1 (January – March) to 4 (October – December).

## Syntax

```dax
QUARTER(<date>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`date`|A date.|

## Return value

An integer number from 1 to 4.

## Remarks

If the input value is BLANK, the output value is also BLANK.

## Example 1

The following DAX query:

```dax
EVALUATE { QUARTER(DATE(2019, 2, 1)), QUARTER(DATE(2018, 12, 31)) } 
```

Returns:

|[Value]  |
|---------|
|1    |
|4    |

## Example 2

The following DAX query:

```dax
EVALUATE
ADDCOLUMNS(
    FILTER(
        VALUES(
            FactInternetSales[OrderDate]), 
            [OrderDate] >= DATE(2008, 3, 31) && [OrderDate] <= DATE(2008, 4, 1)
        ), 
    "Quarter", QUARTER([OrderDate])
)
```

Returns:

|FactInternetSales[OrderDate]  | [Quarter]  |
|---------|---------|
|3/31/2008    |  1  |
|  4/1/2008  |  2   |

## Related content

[YEAR](year-function-dax.md)
[MONTH](month-function-dax.md)
[DAY](day-function-dax.md)
