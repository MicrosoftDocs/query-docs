---
description: "Learn more about: DB"
title: "DB function (DAX) | Microsoft Docs"
author: jajin7
---

# DB

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the depreciation of an asset for a specified period using the fixed-declining balance method.

## Syntax

```dax
DB(<cost>, <salvage>, <life>, <period>[, <month>])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|`cost`|The initial cost of the asset.|
|`salvage`|The value at the end of the depreciation (sometimes called the salvage value of the asset). This value can be 0.|
|`life`|The number of periods over which the asset is being depreciated (sometimes called the useful life of the asset).|
|`period`|The period for which you want to calculate the depreciation. Period must use the same units as life. Must be between 1 and life (inclusive).|
|`month`|(Optional) The number of months in the first year. If month is omitted, it is assumed to be 12.|

## Return Value

The depreciation over the specified period.

## Remarks

- The fixed-declining balance method computes depreciation at a fixed rate. DB uses the following formulas to calculate depreciation for a period:

  $$(\text{cost} - \text{total depreciation from prior periods}) \times \text{rate}$$

  where:

  - $\text{rate} = 1 - ((\frac{\text{salvage}}{\text{cost}})^{(\frac{1}{\text{life}})})\text{, rounded to three decimal places}$

- Depreciation for the first and last periods is a special case.
  - For the first period, DB uses this formula:

      $$\frac{\text{cost} \times \text{rate} \times \text{month}}{12}$$

  - For the last period, DB uses this formula:

      $$\frac{(\text{cost} - \text{total depreciation from prior periods}) \times \text{rate} \times (12 - \text{month})}{12}$$

- period and month are rounded to the nearest integer.

- An error is returned if:
  - cost < 0.
  - salvage < 0.
  - life < 1.
  - period < 1 or period > life.
  - month < 1 or month > 12.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Examples

### Example 1

The following DAX query:

```dax
EVALUATE
{
  DB(1000000, 0, 6, 1, 2)
}
```

Returns an asset's depreciation in the last two months of the first year, assuming it will be worth \\$0 after 6 years.

| **[Value]**    |
| ---------------- |
| 166666.666666667 |

### Example 2

The following calculates the total depreciation of all assets in different years over their lifetimes. Here, the first year only includes 7 months of depreciation, and the last year only includes 5 months.

```dax
DEFINE
VAR NumDepreciationPeriods = MAX(Asset[LifeTimeYears])+1
VAR DepreciationPeriods = GENERATESERIES(1, NumDepreciationPeriods)
EVALUATE
ADDCOLUMNS (
  DepreciationPeriods,
  "Current Period Total Depreciation",
  SUMX (
    FILTER (
      Asset,
      [Value] <= [LifetimeYears]+1
    ),
    DB([InitialCost], [SalvageValue], [LifetimeYears], [Value], 7)
  )
)
```
