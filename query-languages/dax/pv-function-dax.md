---
description: "Learn more about: PV"
title: "PV function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend 
recommendations: false

---

# PV

Calculates the present value of a loan or an investment, based on a constant interest rate. You can use PV with either periodic, constant payments (such as a mortgage or other loan), and/or a future value that's your investment goal.

## Syntax

```dax
PV(<rate>, <nper>, <pmt>[, <fv>[, <type>]])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|rate|The interest rate per period. For example, if you obtain an automobile loan at a 10 percent annual interest rate and make monthly payments, your interest rate per month is 0.1/12, or 0.0083. You would enter 0.1/12, or 0.0083, into the formula as the rate.|
|nper|The total number of payment periods in an annuity. For example, if you get a four-year car loan and make monthly payments, your loan has 4*12 (or 48) periods. You would enter 48 into the formula for nper.|
|pmt|The payment made each period that cannot change over the life of the annuity. Typically, pmt includes principal and interest but no other fees or taxes. For example, the monthly payments on a \\$10,000, four-year car loan at 12 percent are \\$263.33. You would enter -263.33 into the formula as the pmt.|
|fv|(Optional) The future value, or a cash balance you want to attain after the last payment is made. If fv is omitted, it is assumed to be BLANK. For example, if you want to save \\$50,000 to pay for a special project in 18 years, then \\$50,000 is the future value. You could then make a conservative guess at an interest rate and determine how much you must save each month.|
|type|(Optional) The number 0 or 1 which indicates when payments are due. If type is omitted, it is assumed to be 0. The accepted values are listed below this table.|

The **type** parameter accepts the following values:

| **Set type equal to** | **If payments are due**        |
| --------------------- | ------------------------------ |
| 0 or omitted          | At the end of the period       |
| 1                     | At the beginning of the period |

## Return Value

The present value of a loan or investment.

## Remarks

- Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at 12 percent annual interest, use 0.12/12 for rate and 4*12 for nper. If you make annual payments on the same loan, use 0.12 for rate and 4 for nper.

- The following functions apply to annuities:
  - CUMIPMT
  - CUMPRINC
  - FV
  - IPMT
  - PMT
  - PPMT
  - PV
  - RATE
  - XIRR
  - XNPV

- An annuity is a series of constant cash payments made over a continuous period. For example, a car loan or a mortgage is an annuity. For more information, see the description for each annuity function.

- In annuity functions, cash you pay out, such as a deposit to savings, is represented by a negative number; cash you receive, such as a dividend check, is represented by a positive number. For example, a \\$1,000 deposit to the bank would be represented by the argument -1000 if you are the depositor and by the argument 1000 if you are the bank.

- One financial argument is solved in terms of the others.
  - If rate is not 0, then:

    $$\text{pv} \times (1 + \text{rate})^{\text{nper}} + \text{pmt}(1 + \text{rate} \times \text{type}) \times \bigg( \frac{(1 + \text{rate})^{\text{nper}} - 1}{\text{rate}} \bigg) + \text{fv} = 0$$

  - If rate is 0, then:

    $$(\text{pmt} \times \text{nper}) + \text{pv} + \text{fv} = 0$$

- type is rounded to the nearest integer.

- An error is returned if:
  - nper < 1

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data** | **Description**                                                   |
| -------- | ----------------------------------------------------------------- |
| \\$500.00  | Money paid out of an insurance annuity at the end of every month. |
| 8%       | Interest rate earned on the money paid out.                       |
| 20       | Years the money will be paid out.                                 |

The following DAX query:

```dax
EVALUATE
{
  PV(0.08/12, 12*20, 500.00, 0, 0)
}
```

Returns the present value of an annuity using the terms specified above.

| **[Value]**      |
| ------------------ |
| -59777.1458511878 |
