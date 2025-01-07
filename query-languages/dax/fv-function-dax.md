---
description: "Learn more about: FV"
title: "FV function (DAX)"
author: jajin7
---

# FV

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Calculates the future value of an investment based on a constant interest rate. You can use FV with either periodic, constant payments, and/or a single lump sum payment.

## Syntax

```dax
FV(<rate>, <nper>, <pmt>[, <pv>[, <type>]])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`rate`|The interest rate per period.|
|`nper`|The total number of payment periods in an annuity.|
|`pmt`|The payment made each period; it cannot change over the life of the annuity. Typically, pmt contains principal and interest but no other fees or taxes.|
|`pv`|(Optional) The present value, or the lump-sum amount that a series of future payments is worth right now. If pv is omitted, it is assumed to be BLANK.|
|`type`|(Optional) The number 0 or 1 which indicates when payments are due. If type is omitted, it is assumed to be 0. The accepted values are listed below this table.|

The `type` parameter accepts the following values:

| **Set type equal to** | **If payments are due**        |
| --------------------- | ------------------------------ |
| 0 or omitted          | At the end of the period       |
| 1                     | At the beginning of the period |

**Note:** For a more complete description of the arguments in FV and for more information on annuity functions, see the PV function.

## Return Value

The future value of an investment.

## Remarks

- Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at 12 percent annual interest, use 0.12/12 for rate and 4*12 for nper. If you make annual payments on the same loan, use 0.12 for rate and 4 for nper.

- For all the arguments, cash you pay out, such as deposits to savings, is represented by negative numbers; cash you receive, such as dividend checks, is represented by positive numbers.

- type is rounded to the nearest integer.

- An error is returned if:
  - nper < 1

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data** | **Description**                                                                             |
| -------- | ------------------------------------------------------------------------------------------- |
| 6%       | Annual interest rate                                                                        |
| 10       | Number of payments                                                                          |
| -200    | Amount of the payment                                                                       |
| -500    | Present value                                                                               |
| 1        | Payment is due at the beginning of the period (0 indicates payment is due at end of period) |

The following DAX query:

```dax
EVALUATE
{
  FV(0.06/12, 10, -200, -500, 1)
}
```

Returns the future value of an investment using the terms specified above.

| **[Value]**    |
| ---------------- |
| 2581.40337406012 |
