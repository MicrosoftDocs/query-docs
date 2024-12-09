---
description: "Learn more about: PRICE"
title: "PRICE function (DAX)"
author: jajin7
---

# PRICE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the price per \\$100 face value of a security that pays periodic interest.

## Syntax

```dax
PRICE(<settlement>, <maturity>, <rate>, <yld>, <redemption>, <frequency>[, <basis>])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|`settlement`|The security's settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer.|
|`maturity`|The security's maturity date. The maturity date is the date when the security expires.|
|`rate`|The security's annual coupon rate.|
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

- settlement and maturity are truncated to integers.

- basis and frequency are rounded to the nearest integer.

- An error is returned if:
  - settlement or maturity is not a valid date.
  - settlement ≥ maturity.
  - rate < 0.
  - yld < 0.
  - redemption ≤ 0.
  - frequency is any number other than 1, 2, or 4.
  - basis < 0 or basis > 4.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

**Important:**

- When N > 1 (N is the number of coupons payable between the settlement date and redemption date), **PRICE** is calculated as follows:

  $$\text{PRICE} = \bigg[ \frac{\text{redemption}}{(1 + \frac{\text{yld}}{\text{frequency}})^{(N - 1 + \frac{\text{DSC}}{\text{E}})})} \bigg] + \bigg[ \sum^{N}\_{k=1} \frac{100 \times \frac{\text{rate}}{\text{frequency}}}{(1 + \frac{\text{yld}}{\text{frequency}})^{(k - 1 + \frac{\text{DSC}}{\text{E}})}} \bigg] -  \bigg[ 100 \times \frac{\text{rate}}{\text{frequency}} \times \frac{\text{A}}{\text{E}} \bigg]$$

- When N = 1 (N is the number of coupons payable between the settlement date and redemption date), **PRICE** is calculated as follows:

  $$\text{DSR} = \text{E} - \text{A}$$

  $$\text{T1} = 100 \times \frac{\text{rate}}{\text{frequency}} + \text{redemption}$$

  $$\text{T2} = \frac{\text{yld}}{\text{frequency}} \times \frac{\text{DSR}}{\text{E}} + 1$$

  $$\text{T3} = 100 \times \frac{\text{rate}}{\text{frequency}} \times \frac{\text{A}}{\text{E}}$$

  $$\text{PRICE} = \frac{\text{T1}}{\text{T2}} - \text{T3}$$

  where:

  - $\text{DSC}$ = number of days from settlement to next coupon date.
  - $\text{E}$ = number of days in coupon period in which the settlement date falls.
  - $\text{A}$ = number of days from beginning of coupon period to settlement date.

## Example

| **Data**   | **Argument description**  |
| ---------- | ------------------------- |
| 2/15/2008  | Settlement date           |
| 11/15/2017 | Maturity date             |
| 5.75%      | Percent semiannual coupon |
| 6.50%      | Percent yield             |
| \\$100       | Redemption value          |
| 2          | Frequency is semiannual   |
| 0          | 30/360 basis              |

The following DAX query:

```dax
EVALUATE
{
  PRICE(DATE(2008,2,15), DATE(2017,11,15), 0.0575, 0.065, 100, 2, 0)
}
```

Returns the bond price, for a bond using the terms specified above.

| **[Value]**    |
| ---------------- |
| 94.6343616213221 |
