---
description: "Learn more about: ODDFPRICE"
title: "ODDFPRICE function (DAX)"
author: jajin7
---

# ODDFPRICE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the price per \\$100 face value of a security having an odd (short or long) first period.

## Syntax

```dax
ODDFPRICE(<settlement>, <maturity>, <issue>, <first_coupon>, <rate>, <yld>, <redemption>, <frequency>[, <basis>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`settlement`|The security's settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer.|
|`maturity`|The security's maturity date. The maturity date is the date when the security expires.|
|`issue`|The security's issue date.|
|`first_coupon`|The security's first coupon date.|
|`rate`|The security's interest rate.|
|`yld`|The security's annual yield.|
|`redemption`|The security's redemption value per \\$100 face value.|
|`frequency`|The number of coupon payments per year. For annual payments, frequency = 1; for semiannual, frequency = 2; for quarterly, frequency = 4.|
|`basis`|(Optional) The type of day count basis to use. If basis is omitted, it is assumed to be 0. The accepted values are listed below this table.|

The `basis` parameter accepts the following values:

| `Basis`    | **Day count basis** |
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

- ODDFPRICE is calculated as follows:

  **Odd short first coupon:**

  $$\text{ODDFPRICE} = \bigg[ \frac{\text{redemption}}{(1 + \frac{\text{yld}}{\text{frequency}})^{(N - 1 + \frac{\text{DSC}}{\text{E}})}} \bigg] + \bigg[ \frac{100 \times \frac{\text{rate}}{\text{frequency}} \times \frac{\text{DFC}}{\text{E}}}{(1 + \frac{\text{yld}}{\text{frequency}})^{(\frac{\text{DSC}}{\text{E}})}} \bigg] + \bigg[ \sum^{N}\_{k=2} \frac{100 \times \frac{\text{rate}}{\text{frequency}}}{(1 + \frac{\text{yld}}{\text{frequency}})^{(k - 1 + \frac{\text{DSC}}{\text{E}})}} \bigg] - \Big[ 100 \times \frac{\text{rate}}{\text{frequency}} \times \frac{\text{A}}{\text{E}} \Big] $$

  where:

  - $\text{A}$ = number of days from the beginning of the coupon period to the settlement date (accrued days).
  - $\text{DSC}$ = number of days from the settlement to the next coupon date.
  - $\text{DFC}$ = number of days from the beginning of the odd first coupon to the first coupon date.
  - $\text{E}$ = number of days in the coupon period.
  - $\text{N}$ = number of coupons payable between the settlement date and the redemption date. (If this number contains a fraction, it is raised to the next whole number.)

  **Odd long first coupon:**

  $$\text{ODDFPRICE} = \bigg[ \frac{\text{redemption}}{(1 + \frac{\text{yld}}{\text{frequency}})^{(\text{N} + \text{N}\_{q} + \frac{\text{DSC}}{\text{E}})}} \bigg] + \bigg[ \frac{100 \times \frac{\text{rate}}{\text{frequency}} \times \Big[ \sum^{\text{NC}}\_{i=1} \frac{\text{DC}\_{i}}{\text{NL}\_{i}} \Big]  }{(1 + \frac{\text{yld}}{\text{frequency}})^{(\text{N}\_{q} + \frac{\text{DSC}}{\text{E}})}} \bigg] + \bigg[ \sum^{\text{N}}\_{k=1} \frac{100 \times \frac{\text{rate}}{\text{frequency}}}{(1 + \frac{\text{yld}}{\text{frequency}})^{(k - \text{N}\_{q} + \frac{\text{DSC}}{\text{E}})}} \bigg] - \Big[ 100 \times \frac{\text{rate}}{\text{frequency}} \times \sum^{\text{NC}}\_{i=1} \frac{\text{A}\_{i}}{\text{NL}\_{i}} \Big]$$

  where:

  - $\text{A}\_{i}$ = number of days from the beginning of the $i^{th}$, or last, quasi-coupon period within odd period.
  - $\text{DC}\_{i}$ = number of days from dated date (or issue date) to first quasi-coupon ($i = 1$) or number of days in quasi-coupon ($i = 2$,..., $i = \text{NC}$).
  - $\text{DSC}$ = number of days from settlement to next coupon date.
  - $\text{E}$ = number of days in coupon period.
  - $\text{N}$ = number of coupons payable between the first real coupon date and redemption date. (If this number contains a fraction, it is raised to the next whole number.)
  - $\text{NC}$ = number of quasi-coupon periods that fit in odd period. (If this number contains a fraction, it is raised to the next whole number.)
  - $\text{NL}\_{i}$ = normal length in days of the full $i^{th}$, or last, quasi-coupon period within odd period.
  - $\text{N}\_{q}$ = number of whole quasi-coupon periods between settlement date and first coupon.

- settlement, maturity, issue, and first_coupon are truncated to integers.

- basis and frequency are rounded to the nearest integer.

- An error is returned if:
  - settlement, maturity, issue, or first_coupon is not a valid date.
  - maturity > first_coupon > settlement > issue is not satisfied.
  - rate < 0.
  - yld < 0.
  - redemption ≤ 0.
  - frequency is any number other than 1, 2, or 4.
  - basis < 0 or basis > 4.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data**   | **Argument description** |
| ---------- | ------------------------ |
| 11/11/2008 | Settlement date          |
| 3/1/2021   | Maturity date            |
| 10/15/2008 | Issue date               |
| 3/1/2009   | First coupon date        |
| 7.85%      | Percent coupon           |
| 6.25%      | Percent yield            |
| \\$100.00    | Redemptive value         |
| 2          | Frequency is semiannual  |
| 1          | Actual/actual basis      |

The following DAX query:

```dax
EVALUATE
{
  ODDFPRICE(DATE(2008,11,11), DATE(2021,3,1), DATE(2008,10,15), DATE(2009,3,1), 0.0785, 0.0625, 100.00, 2, 1)
}
```

Returns the price per \\$100 face value of a security having an odd (short or long) first period, using the terms specified above.

| **[Value]**    |
| ---------------- |
| 113.597717474079 |
