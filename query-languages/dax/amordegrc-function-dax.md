---
description: "Learn more about: AMORDEGRC"
title: "AMORDEGRC function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend

---

# AMORDEGRC

Returns the depreciation for each accounting period. This function is provided for the French accounting system. If an asset is purchased in the middle of the accounting period, the prorated depreciation is taken into account. The function is similar to AMORLINC, except that a depreciation coefficient is applied in the calculation depending on the life of the assets.

## Syntax

```dax
AMORDEGRC(<cost>, <date_purchased>, <first_period>, <salvage>, <period>, <rate>[, <basis>])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|cost|The cost of the asset.|  
|date_purchased|The date of the purchase of the asset.|
|first_period|The date of the end of the first period.|
|salvage|The salvage value at the end of the life of the asset.|
|period|The period.|
|rate|The rate of depreciation.|
|basis|(Optional) The type of day count basis to use. If basis is omitted, it is assumed to be 0. The accepted values are listed below this table.|

The **basis** parameter accepts the following values:

| **Basis**    | **Date system**                      |
| ------------ | ------------------------------------ |
| 0 or omitted | 360 days (NASD method)               |
| 1            | Actual                               |
| 3            | 365 days in a year                   |
| 4            | 360 days in a year (European method) |

## Return Value

The depreciation for each accounting period.

## Remarks

- Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899.

- This function will return the depreciation until the last period of the life of the assets or until the cumulated value of depreciation is greater than the cost of the assets minus the salvage value.

- The depreciation coefficients are:

  | **Life of assets (1/rate)** | **Depreciation coefficient** |
  | --------------------------- | ---------------------------- |
  | Between 3 and 4 years       | 1.5                          |
  | Between 5 and 6 years       | 2                            |
  | More than 6 years           | 2.5                          |

- The depreciation rate will grow to 50 percent for the period preceding the last period and will grow to 100 percent for the last period.

- period and basis are rounded to the nearest integer.

- An error is returned if:
  - cost < 0.
  - first_period or date_purchased is not a valid date.
  - date_purchased > first_period.
  - salvage < 0 or salvage > cost.
  - period < 0.
  - rate ≤ 0.
  - The life of assets is between 0 (zero) and 1, 1 and 2, 2 and 3, or 4 and 5.
  - basis is any number other than 0, 1, 3, or 4.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data**         | **Description**          |
| ---------------- | ------------------------ |
| 2400             | Cost                     |
| 19-August-2008   | Date purchased           |
| 31-December-2008 | End of the first period  |
| 300              | Salvage value            |
| 1                | Period                   |
| 15%              | Depreciation rate        |
| 1                | Actual basis (see above) |

The following DAX query:

```dax
EVALUATE
{
  AMORDEGRC(2400, DATE(2008,8,19), DATE(2008,12,31), 300, 1, 0.15, 1)
}
```

Returns the first period's depreciation, given the terms specified above.

| **[Value]** |
| ------------- |
| 776           |
