---
description: "Learn more about: NPER"
title: "NPER function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend 
recommendations: false

---

# NPER

Returns the number of periods for an investment based on periodic, constant payments and a constant interest rate.

## Syntax

```dax
NPER(<rate>, <pmt>, <pv>[, <fv>[, <type>]])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|rate|The interest rate per period.|
|pmt|The payment made each period; it cannot change over the life of the annuity. Typically, pmt contains principal and interest but no other fees or taxes.|
|pv|The present value, or the lump-sum amount that a series of future payments is worth right now.|
|fv|(Optional) The future value, or a cash balance you want to attain after the last payment is made. If fv is omitted, it is assumed to be BLANK.|
|type|(Optional) The number 0 or 1 and indicates when payments are due. If type is omitted, it is assumed to be 0. The accepted values are listed below this table.|

The **type** parameter accepts the following values:

| **Set type equal to** | **If payments are due**        |
| --------------------- | ------------------------------ |
| 0 or omitted          | At the end of the period       |
| 1                     | At the beginning of the period |

## Return Value

The number of periods for an investment.

## Remarks

- type is rounded to the nearest integer.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data** | **Description**                                           |
| -------- | --------------------------------------------------------- |
| 12%      | Annual interest rate                                      |
| -100    | Payment made each period                                  |
| -1000   | Present value                                             |
| 10000    | Future value                                              |
| 1        | Payment is due at the beginning of the period (see above) |

The following DAX query:

```dax
EVALUATE
{
  NPER(0.12/12, -100, -1000, 10000, 1)
}
```

Returns the number of periods for the investment described by the terms specified above.

| **[Value]**    |
| ---------------- |
| 59.6738656742946 |
