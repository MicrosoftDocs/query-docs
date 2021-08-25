---
description: "Learn more about: RATE"
title: "RATE function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend 
recommendations: false

---

# RATE

Returns the interest rate per period of an annuity. RATE is calculated by iteration and can have zero or more solutions. If the successive results of RATE do not converge to within 0.0000001 after 20 iterations, an error is returned.

## Syntax

```dax
RATE(<nper>, <pmt>, <pv>[, <fv>[, <type>[, <guess>]]])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|nper|The total number of payment periods in an annuity.|
|pmt|The payment made each period and cannot change over the life of the annuity. Typically, pmt includes principal and interest but no other fees or taxes.|
|pv|The present value — the total amount that a series of future payments is worth now.|
|fv|(Optional) The future value, or a cash balance you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (the future value of a loan, for example, is 0).|
|type|(Optional) The number 0 or 1 which indicates when payments are due. If type is omitted, it is assumed to be 0. The accepted values are listed below this table.|
|guess|(Optional) Your guess for what the rate will be. <br/> - If omitted, it is assumed to be 10%. <br/> - If RATE does not converge, try different values for guess. RATE usually converges if guess is between 0 and 1.|

The **type** parameter accepts the following values:

| **Set type equal to** | **If payments are due**        |
| --------------------- | ------------------------------ |
| 0 or omitted          | At the end of the period       |
| 1                     | At the beginning of the period |

## Return Value

The interest rate per period.

## Remarks

- Make sure that you are consistent about the units you use for specifying guess and nper. If you make monthly payments on a four-year loan at 12 percent annual interest, use 0.12/12 for guess and 4*12 for nper. If you make annual payments on the same loan, use 0.12 for guess and 4 for nper.

- type is rounded to the nearest integer.

- An error is returned if:
  - nper ≤ 0.
  - RATE does not converge to within 0.0000001 after 20 iterations

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Examples

| **Data** | **Description**    |
| -------- | ------------------ |
| 4        | Years of the loan  |
| -200    | Monthly payment    |
| 8000     | Amount of the loan |

### Example 1

The following DAX query:

```dax
EVALUATE
{
  RATE(4*12, -200, 8000)
}
```

Returns the monthly rate of the loan using the terms specified above.

| **[Value]**       |
| ------------------- |
| 0.00770147248820137 |

### Example 2

The following DAX query:

```dax
EVALUATE
{
  RATE(4*12, -200, 8000) * 12
}
```

Returns the annual rate of the loan using the terms specified above.

| **[Value]**      |
| ------------------ |
| 0.0924176698584164 |
