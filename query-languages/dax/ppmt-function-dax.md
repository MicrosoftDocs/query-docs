---
description: "Learn more about: PPMT"
title: "PPMT function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend

---

# PPMT

Returns the payment on the principal for a given period for an investment based on periodic, constant payments and a constant interest rate.

## Syntax

```dax
PPMT(<rate>, <per>, <nper>, <pv>[, <fv>[, <type>]])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|rate|The interest rate for the loan.|
|per|Specifies the period. Must be between 1 and nper (inclusive).|
|nper|The total number of payment periods in an annuity.|
|pv|The present value — the total amount that a series of future payments is worth now.|
|fv|(Optional) The future value, or a cash balance you want to attain after the last payment is made. If fv is omitted, it is assumed to be BLANK.|
|type|(Optional) The number 0 or 1 which indicates when payments are due. If type is omitted, it is assumed to be 0. The accepted values are listed below this table.|

The **type** parameter accepts the following values:

| **Set type equal to** | **If payments are due**        |
| --------------------- | ------------------------------ |
| 0 or omitted          | At the end of the period       |
| 1                     | At the beginning of the period |

**Note:** For a more complete description of the arguments in PPMT, see the PV function.

## Return Value

The payment on the principal for a given period.

## Remarks

- Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at an annual interest rate of 12 percent, use 0.12/12 for rate and 4*12 for nper. If you make annual payments on the same loan, use 0.12 for rate and 4 for nper.

- type is rounded to the nearest integer.

- An error is returned if:
  - per < 1 or per > nper
  - nper < 1

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example 1

| **Data**  | **Argument description**     |
| --------- | ---------------------------- |
| 10%       | Annual interest rate         |
| 2         | Number of years for the loan |
| \\$2,000.00 | Amount of loan               |

The following DAX query:

```dax
EVALUATE
{
  PPMT(0.1/12, 1, 2*12, 2000.00)
}
```

Returns the principal payment made in the first month for a loan with the terms specified above.

| **[Value]**      |
| ------------------ |
| -75.6231860083663 |

## Example 2

| **Data**    | **Argument description**     |
| ----------- | ---------------------------- |
| 8%          | Annual interest rate         |
| 10          | Number of years for the loan |
| \\$200,000.00 | Amount of loan               |

The following DAX query:

```dax
EVALUATE
{
  PPMT(0.08, 10, 10, 200000.00)
}
```

Returns the principal payment made in the 10th year for a loan with the terms specified above.

| **[Value]**      |
| ------------------ |
| -27598.0534624214 |
