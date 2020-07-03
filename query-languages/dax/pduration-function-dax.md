---
title: "PDURATION function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend

---

# PDURATION

Returns the number of periods required by an investment to reach a specified value.

## Syntax

```dax
PDURATION(<rate>, <pv>, <fv>)
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|rate|The interest rate per period.|
|pv|The present value of the investment.|
|fv|The desired future value of the investment.|

## Return Value

The number of periods.

## Remarks

- PDURATION uses the following equation:

    $$\text{PDURATION} = \frac{log(\text{fv}) - log(\text{pv})}{log(1 + \text{rate})}$$

- An error is returned if:
  - rate ≤ 0.
  - pv ≤ 0.
  - fv ≤ 0.

## Examples

### Example 1

The following DAX query:

```dax
EVALUATE
{
  PDURATION(0.025, 2000, 2200)
}
```

Returns the number of years required for an investment of \$2000, earning 2.5% annually, to reach \$2200.

| **[Value]**    |
| ---------------- |
| 3.85986616262266 |

### Example 2

The following DAX query:

```dax
EVALUATE
{
  PDURATION(0.025/12, 1000, 1200)
}
```

Returns the number of months required for an investment of \$1000, earning 2.5% annually, to reach \$1200.

| **[Value]**    |
| ---------------- |
| 87.6054764193714 |
