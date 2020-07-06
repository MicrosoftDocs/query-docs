---
title: "SYD function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend

---

# SYD

Returns the sum-of-years' digits depreciation of an asset for a specified period.

## Syntax

```dax
SYD(<cost>, <salvage>, <life>, <per>)
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|cost|The initial cost of the asset.|
|salvage|The value at the end of the depreciation (sometimes called the salvage value of the asset).|
|life|The number of periods over which the asset is depreciated (sometimes called the useful life of the asset).|
|per|The period. Must use the same units as life. Must be between 1 and life (inclusive).|

## Return Value

The sum-of-years' digits depreciation for the specified period.

## Remarks

- SYD is calculated as follows:

    $$\text{SYD} = \frac{(\text{cost} - \text{salvage}) \times (\text{life} - \text{per} + 1) \times 2}{(\text{life}) \times (\text{life} + 1)}$$

- An error is returned if:
  - life < 1.
  - per < 1 or per > life.

## Examples

| **Data**    | **Description**   |
| ----------- | ----------------- |
| \\$30,000.00 | Initial cost      |
| \\$7,500.00  | Salvage value     |
| 10          | Lifespan in years |

### Example 1

The following DAX query:

```dax
EVALUATE
{
  SYD(30000.00, 7500.00, 10, 1)
}
```

Returns an asset's sum-of-years' digits depreciation allowance for the first year, given the terms specified above.

| **[Value]**    |
| ---------------- |
| 4090.90909090909 |

### Example 2

The following DAX query:

```dax
EVALUATE
{
  SYD(30000.00, 7500.00, 10, 10)
}
```

Returns an asset's sum-of-years' digits depreciation allowance for the tenth (final) year, given the terms specified above.

| **[Value]**    |
| ---------------- |
| 409.090909090909 |
