---
description: "Learn more about: CUMIPMT"
title: "CUMIPMT function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend

---

# CUMIPMT

Returns the cumulative interest paid on a loan between start_period and end_period.

## Syntax

```dax
CUMIPMT(<rate>, <nper>, <pv>, <start_period>, <end_period>, <type>)
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|rate|The interest rate.|  
|nper|The total number of payment periods.|
|pv|The present value.|
|start_period|The first period in the calculation. Must be between 1 and end_period (inclusive).|
|end_period|The last period in the calculation. Must be between start_period and nper (inclusive).|
|type|The timing of the payment. The accepted values are listed below this table.|

The **type** parameter accepts the following values:

| **Type** | **Timing**                             |
| -------- | -------------------------------------- |
| 0 (zero) | Payment at the end of the period       |
| 1        | Payment at the beginning of the period |

## Return Value

The cumulative interest paid in the specified period.

## Remarks

- Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at an annual interest rate of 10 percent, use 0.1/12 for rate and 4*12 for nper. If you make annual payments on the same loan, use 0.1 for rate and 4 for nper.

- start_period, end_period, and type are rounded to the nearest integer.

- An error is returned if:
  - rate ≤ 0.
  - nper < 1.
  - pv ≤ 0.
  - start_period < 1 or start_period > end_period.
  - end_period < start_period or end_period > nper.
  - type is any number other than 0 or 1.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Examples

| **Data** | **Description**      |
| -------- | -------------------- |
| 9%       | Annual interest rate |
| 30       | Years of the loan    |
| 125000   | Present value        |

### Example 1

The following DAX query:

```dax
EVALUATE
{
  CUMIPMT(0.09/12, 30*12, 125000, 13, 24, 1)
}
```

Returns the total interest paid in the second year of payments, periods 13 through 24, assuming that the payments are made at the beginning of each month.

| **[Value]**      |
| ------------------ |
| -11052.3395838718 |

### Example 2

The following DAX query:

```dax
EVALUATE
{
  CUMIPMT(0.09/12, 30*12, 125000, 1, 1, 0)
}
```

Returns the interest paid in a single payment in the first month, assuming that the payment is made at the end of the month.

| **[Value]** |
| ------------- |
| -937.5       |
