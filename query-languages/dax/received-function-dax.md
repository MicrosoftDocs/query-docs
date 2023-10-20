---
description: "Learn more about: RECEIVED"
title: "RECEIVED function (DAX) | Microsoft Docs"
author: jajin7
---

# RECEIVED

Returns the amount received at maturity for a fully invested security.

## Syntax

```dax
RECEIVED(<settlement>, <maturity>, <investment>, <discount>[, <basis>])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|settlement|The security's settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer.|
|maturity|The security's maturity date. The maturity date is the date when the security expires.|
|investment|The amount invested in the security.|
|discount|The security's discount rate.|
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

The amount received at maturity.

## Remarks

- Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899.

- The settlement date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2008, and is purchased by a buyer six months later. The issue date would be January 1, 2008, the settlement date would be July 1, 2008, and the maturity date would be January 1, 2038, which is 30 years after the January 1, 2008, issue date.

- RECEIVED is calculated as follows:

  $$\text{RECEIVED} = \frac{\text{investment}}{1 - (\text{discount} \times \frac{\text{DIM}}{\text{B}})}$$

  where:

  - $\text{B}$ = number of days in a year, depending on the year basis.
  - $\text{DIM}$ = number of days from issue to maturity.

- settlement and maturity are truncated to integers.

- basis is rounded to the nearest integer.

- An error is returned if:
  - settlement or maturity is not a valid date.
  - settlement ≥ maturity.
  - investment ≤ 0.
  - discount ≤ 0.
  - basis < 0 or basis > 4.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following DAX query:

| **Data**       | **Description**         |
| -------------- | ----------------------- |
| 15-Feb-08      | Settlement (issue) date |
| 15-May-08      | Maturity date           |
| \\$1,000,000.00 | Investment              |
| 5.75%          | Percent discount rate   |
| 2              | Actual/360 basis        |

```dax
EVALUATE
{
  RECEIVED(DATE(2008,2,15), DATE(2008,5,15), 1000000.00, 0.0575, 2)
}
```

Returns the total amount to be received at maturity, for a bond with the terms specified above.

| **[Value]**   |
| --------------- |
| 1014584.6544071 |
