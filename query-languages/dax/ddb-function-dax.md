---
description: "Learn more about: DDB"
title: "DDB function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend 
recommendations: false

---

# DDB

Returns the depreciation of an asset for a specified period using the double-declining balance method or some other method you specify.

## Syntax

```dax
DDB(<cost>, <salvage>, <life>, <period>[, <factor>])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|cost|The initial cost of the asset.|
|salvage|The value at the end of the depreciation (sometimes called the salvage value of the asset). This value can be 0.|
|life|The number of periods over which the asset is being depreciated (sometimes called the useful life of the asset).|
|period|The period for which you want to calculate the depreciation. Period must use the same units as life. Must be between 1 and life (inclusive).|
|factor|(Optional) The rate at which the balance declines. If factor is omitted, it is assumed to be 2 (the double-declining balance method).|

## Return Value

The depreciation over the specified period.

## Remarks

- The double-declining balance method computes depreciation at an accelerated rate. Depreciation is highest in the first period and decreases in successive periods. DDB uses the following formula to calculate depreciation for a period:

  $$\text{Min}((\text{cost} - \text{total depreciation from prior periods}) \times (\frac{\text{factor}}{\text{life}}),(\text{cost} - \text{salvage} - \text{total depreciation from prior periods}))$$

- Change factor if you do not want to use the double-declining balance method.

- Use the VDB function if you want to switch to the straight-line depreciation method when depreciation is greater than the declining balance calculation.

- period is rounded to the nearest integer.

- An error is returned if:
  - cost < 0.
  - salvage < 0.
  - life < 1.
  - period < 1 or period > life.
  - factor ≤ 0.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Examples

### Example 1

The following DAX query:

```dax
EVALUATE
{
  DDB(1000000, 0, 10, 5, 1.5)
}
```

Returns an asset's depreciation in the 5$^{th}$ year, assuming it will be worth \\$0 after 10 years. This calculation uses a factor of 1.5.

| **[Value]** |
| ------------- |
| 78300.9375    |

### Example 2

The following calculates the total depreciation of all assets in different years over their lifetimes. This calculation uses the default factor of 2 (the double-declining balance method).

```dax
DEFINE
VAR NumDepreciationPeriods = MAX(Asset[LifeTimeYears])
VAR DepreciationPeriods = GENERATESERIES(1, NumDepreciationPeriods)
EVALUATE
  ADDCOLUMNS (
  DepreciationPeriods,
  "Current Period Total Depreciation",
  SUMX (
    FILTER (
      Asset,
      [Value] <= [LifetimeYears]
    ),
    DDB([InitialCost], [SalvageValue], [LifetimeYears], [Value])
  )
)
```
