---
description: "Learn more about: INTRATE"
title: "INTRATE function (DAX) | Microsoft Docs"
---

# INTRATE

Returns the interest rate for a fully invested security.

## Syntax

```dax
INTRATE(<settlement>, <maturity>, <investment>, <redemption>[, <basis>])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|settlement|The security's settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer.|
|maturity|The security's maturity date. The maturity date is the date when the security expires.|
|investment|The amount invested in the security.|
|redemption|The amount to be received at maturity.|
|basis|(Optional) The type of day count basis to use. If basis is omitted, it is assumed to be 0. The accepted values are listed below this table.|

The **basis** parameter accepts the following values:

| **Basis**    | **Day count basis** |
| ------------ | ------------------- |
| 0 or omitted | US (NASD) 30/360    |
| 1            | Actual/actual       |
| 2            | Actual/360          |
| 3            | Actual/365          |
| 4            | European 30/360     |

## Return Value

The interest rate.

## Remarks

- Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899.

- The settlement date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2008, and is purchased by a buyer six months later. The issue date would be January 1, 2008, the settlement date would be July 1, 2008, and the maturity date is January 1, 2038, which is 30 years after the January 1, 2008, issue date.

- INTRATE is calculated as follows:

  $$\text{INTRATE} = \frac{\text{redemption} - \text{investment}}{\text{investment}} \times \frac{\text{B}}{\text{DIM}}$$

  where:

  - $\text{B}$ = number of days in a year, depending on the year basis.
  - $\text{DIM}$ = number of days from settlement to maturity.

- settlement and maturity are truncated to integers.

- basis is rounded to the nearest integer.

- An error is returned if:
  - settlement or maturity is not a valid date.
  - settlement ≥ maturity.
  - investment ≤ 0.
  - redemption ≤ 0.
  - basis < 0 or basis > 4.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data**   | **Description**  |
| ---------- | ---------------- |
| 2/15/2008  | Settlement date  |
| 5/15/2008  | Maturity date    |
| \\$1,000,000 | Investment       |
| \\$1,014,420 | Redemption value |
| 2          | Actual/360 basis |

The following DAX query:

```dax
EVALUATE
{
  INTRATE(DATE(2008,2,15), DATE(2008,5,15), 1000000, 1014420, 2)
}
```

Returns the discount rate for a bond using the terms specified above.

| **[Value]** |
| ------------- |
| 0.05768       |
