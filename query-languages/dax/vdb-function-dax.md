---
description: "Learn more about: VDB"
title: "VDB function (DAX)"
author: jajin7
---

# VDB

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the depreciation of an asset for any period you specify, including partial periods, using the double-declining balance method or some other method you specify. VDB stands for variable declining balance.

## Syntax

```dax
VDB(<cost>, <salvage>, <life>, <start_period>, <end_period>[, <factor>[, <no_switch>]])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`cost`|The initial cost of the asset.|
|`salvage`|The value at the end of the depreciation (sometimes called the salvage value of the asset). This value can be 0.|
|`life`|The number of periods over which the asset is being depreciated (sometimes called the useful life of the asset).|
|`start_period`|The starting period for which you want to calculate the depreciation. Start_period must use the same units as life. Must be between 1 and life (inclusive).|
|`end_period`|The ending period for which you want to calculate the depreciation. End_period must use the same units as life. Must be between start_period and life (inclusive).|
|`factor`|(Optional) The rate at which the balance declines. If factor is omitted, it is assumed to be 2 (the double-declining balance method). Change factor if you do not want to use the double-declining balance method. For a description of the double-declining balance method, see DDB.|
|`no_switch`|(Optional) A logical value specifying whether to switch to straight-line depreciation when depreciation is greater than the declining balance calculation. If omitted, it is assumed to be `FALSE`. <br/> - If no_switch evaluates to `TRUE`  VDB does not switch to straight-line depreciation, even when the depreciation is greater than the declining balance calculation. <br/> - If no_switch evaluates to `FALSE` or is omitted, VDB switches to straight-line depreciation when depreciation is greater than the declining balance calculation.|

## Return Value

The depreciation over the specified period.

## Remarks

- An error is returned if:
  - cost < 0.
  - salvage < 0.
  - life < 1.
  - start_period < 1 or start_period > end_period.
  - end_period < start_period or end_period > life.
  - factor < 0.
  - no_switch does not evaluate to either `TRUE` or `FALSE`.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Examples

| **Data** | **Description**   |
| -------- | ----------------- |
| 2400     | Initial cost      |
| 300      | Salvage value     |
| 10       | Lifetime in years |

### Example 1

The following DAX query:

```dax
EVALUATE
{
  VDB(2400, 300, 10*365, 0, 1)
}
```

Returns an asset's first day's depreciation using a factor of 2.

| **[Value]**    |
| ---------------- |
| 1.31506849315068 |

### Example 2

The following DAX query:

```dax
EVALUATE
{
  VDB(2400, 300, 10*12, 6, 18, 3)
}
```

Returns an asset's depreciation between the 6$^{th}$ month and the 18$^{th}$ month. This calculation uses a factor of 3.

| **[Value]**    |
| ---------------- |
| 540.185558199698 |

### Example 3

The following DAX query:

```dax
EVALUATE
{
  VDB(2400, 300, 10, 0, 0.875, 1.5)
}
```

Returns an asset's depreciation in the first fiscal year that you own it, assuming that tax laws limit you to 150% depreciation of the declining balance. The asset is purchased in the middle of the first quarter of the fiscal year.

| **[Value]** |
| ------------- |
| 315           |
