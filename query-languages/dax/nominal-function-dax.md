---
description: "Learn more about: NOMINAL"
title: "NOMINAL function (DAX)"
ms.topic: reference
author: jajin7
---

# NOMINAL

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the nominal annual interest rate, given the effective rate and the number of compounding periods per year.

## Syntax

```dax
NOMINAL(<effect_rate>, <npery>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`effect_rate`|The effective interest rate.|
|`npery`|The number of compounding periods per year.|

## Return Value

The nominal annual interest rate.

## Remarks

- The relationship between NOMINAL and EFFECT is shown in the following equation:

    $$\text{EFFECT} = \Big( 1 + \frac{\text{nominal\_rate}}{\text{npery}} \Big)^{\text{npery}} - 1$$

- npery is rounded to the nearest integer.

- An error is returned if:
  - effect_rate ≤ 0.
  - npery < 1.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data** | **Description**                        |
| -------- | -------------------------------------- |
| 5.3543%  | Effective interest rate                |
| 4        | Number of compounding periods per year |

The following DAX query:

```dax
EVALUATE
{
  NOMINAL(0.053543, 4)
}
```

Returns the nominal interest rate, using the terms specified above.

| **[Value]**     |
| ----------------- |
| 0.052500319868356 |
