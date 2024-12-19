---
description: "Learn more about: SLN"
title: "SLN function (DAX)"
author: jajin7
---

# SLN

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the straight-line depreciation of an asset for one period.

## Syntax

```dax
SLN(<cost>, <salvage>, <life>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`cost`|The initial cost of the asset.|
|`salvage`|The value at the end of the depreciation (sometimes called the salvage value of the asset).|
|`life`|The number of periods over which the asset is depreciated (sometimes called the useful life of the asset).|

## Return Value

The straight-line depreciation for one period.

## Remarks

- An error is returned if:
  life = 0.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data** | **Description**      |
| -------- | -------------------- |
| \\$30,000  | Cost                 |
| \\$7,500   | Salvage value        |
| 10       | Years of useful life |

The following DAX query:

```dax
EVALUATE
{
  SLN(30000, 7500, 10)
}
```

Returns the yearly depreciation allowance using the terms specified above.

| **[Value]** |
| ------------- |
| 2250          |
