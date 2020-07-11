---
title: "ISPMT function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend

---

# ISPMT

Calculates the interest paid (or received) for the specified period of a loan (or investment) with even principal payments.

## Syntax

```dax
ISPMT(<rate>, <per>, <nper>, <pv>)
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|rate|The interest rate for the investment.|
|per|The period for which you want to find the interest. Must be between 0 and nper-1 (inclusive).|
|nper|The total number of payment periods for the investment.|
|pv|The present value of the investment. For a loan, pv is the loan amount.|

## Return Value

The interest paid (or received) for the specified period.

## Remarks

- Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at an annual interest rate of 12 percent, use 0.12/12 for rate and 4*12 for nper. If you make annual payments on the same loan, use 0.12 for rate and 4 for nper.

- For all the arguments, the cash you pay out, such as deposits to savings or other withdrawals, is represented by negative numbers; the cash you receive, such as dividend checks and other deposits, is represented by positive numbers.

- ISPMT counts each period beginning with zero, not one.

- Most loans use a repayment schedule with even periodic payments. The IPMT function returns the interest payment for a given period for this type of loan.

- Some loans use a repayment schedule with even principal payments. The ISPMT function returns the interest payment for a given period for this type of loan.

- An error is returned if:
  - nper = 0.

## Example

| **Data** | **Description**   |
| -------- | ----------------- |
| \\$4,000   | Present value     |
| 4        | Number of periods |
| 10%      | Rate              |

To illustrate when to use ISPMT, the amortization table below uses an even-principal repayment schedule with the terms specified above. The interest charge each period is equal to the rate times the unpaid balance for the previous period. And the payment each period is equal to the even principal plus the interest for the period.

| Period | Principal Payment | Interest Payment | Total Payment | Balance  |
| ------ | ----------------- | ---------------- | ------------- | -------- |
|        |                   |                  |               | 4,000.00 |
| 1      | 1,000.00          | 400.00           | 1,400.00      | 3,000.00 |
| 2      | 1,000.00          | 300.00           | 1,300.00      | 2,000.00 |
| 3      | 1,000.00          | 200.00           | 1,200.00      | 1,000.00 |
| 4      | 1,000.00          | 100.00           | 1,100.00      | 0.00     |

The following DAX query:

```dax
DEFINE
VAR NumPaymentPeriods = 4
VAR PaymentPeriods = GENERATESERIES(0, NumPaymentPeriods-1)
EVALUATE
ADDCOLUMNS (
  PaymentPeriods,
  "Interest Payment",
  ISPMT(0.1, [Value], NumPaymentPeriods, 4000)
)
```

Returns the interest paid during each period, using the even-principal repayment schedule and terms specified above. The values are negative to indicate that it is interest paid, not received.

| **[Value]** | **[Interest Payment]** |
| ------------- | ------------------------ |
| 0             | -400                    |
| 1             | -300                    |
| 2             | -200                    |
| 3             | -100                    |
