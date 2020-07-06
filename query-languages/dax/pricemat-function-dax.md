---
title: "PRICEMAT function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend

---

# PRICEMAT

Returns the price per \\$100 face value of a security that pays interest at maturity.

## Syntax

```dax
PRICEMAT(<settlement>, <maturity>, <issue>, <rate>, <yld>[, <basis>])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|settlement|The security's settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer.|
|maturity|The security's maturity date. The maturity date is the date when the security expires.|
|issue|The security's issue date.|
|rate|The security's interest rate at date of issue.|
|yld|The security's annual yield.|
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

The price per \\$100 face value.

## Remarks

- Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899.

- The settlement date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2008, and is purchased by a buyer six months later. The issue date would be January 1, 2008, the settlement date would be July 1, 2008, and the maturity date would be January 1, 2038, which is 30 years after the January 1, 2008, issue date.

- PRICEMAT is calculated as follows:

  $$\text{PRICEMAT} = \frac{100 + (\frac{\text{DIM}}{\text{B}} \times \text{rate} \times 100)}{1 + (\frac{\text{DSM}}{\text{B}} \times \text{yld})} - (\frac{\text{A}}{\text{B}} \times \text{rate} \times 100)$$

  where:

  - $\text{B}$ = number of days in year, depending on year basis.
  - $\text{DSM}$ = number of days from settlement to maturity.
  - $\text{DIM}$ = number of days from issue to maturity.
  - $\text{A}$ = number of days from issue to settlement.

- settlement, maturity, and issue are truncated to integers.

- basis is rounded to the nearest integer.

- An error is returned if:
  - settlement, maturity, or issue is not a valid date.
  - maturity > settlement > issue is not satisfied.
  - rate < 0.
  - yld < 0.
  - basis < 0 or basis > 4.

## Example

The following DAX query:

| **Data**   | **Description**           |
| ---------- | ------------------------- |
| 2/15/2008  | Settlement date           |
| 4/13/2008  | Maturity date             |
| 11/11/2007 | Issue date                |
| 6.10%      | Percent semiannual coupon |
| 6.10%      | Percent yield             |
| 0          | 30/360 basis              |

```dax
EVALUATE
{
  PRICEMAT(DATE(2008,2,15), DATE(2008,4,13), DATE(2007,11,11), 0.061, 0.061, 0)
}
```

Returns the price per \\$100 face value of a security with the terms specified above.

| **[Value]**    |
| ---------------- |
| 99.9844988755569 |
