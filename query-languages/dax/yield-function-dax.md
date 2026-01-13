---
description: "Learn more about: YIELD"
title: "YIELD function (DAX)"
ms.topic: reference
author: jajin7
---

# YIELD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the yield on a security that pays periodic interest. Use YIELD to calculate bond yield.

## Syntax

```dax
YIELD(<settlement>, <maturity>, <rate>, <pr>, <redemption>, <frequency>[, <basis>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`settlement`|The security's settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer.|
|`maturity`|The security's maturity date. The maturity date is the date when the security expires.|
|`rate`|The security's annual coupon rate.|
|`pr`|The security's price per \\$100 face value.|
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

The yield on the security.

## Remarks

- Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899.

- The settlement date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2008, and is purchased by a buyer six months later. The issue date would be January 1, 2008, the settlement date would be July 1, 2008, and the maturity date would be January 1, 2038, which is 30 years after the January 1, 2008, issue date.

- If there is one coupon period or less until redemption, YIELD is calculated as follows:

  $$\text{YIELD} = \frac{(\frac{\text{redemption}}{100} + \frac{\text{rate}}{\text{frequency}}) - (\frac{\text{par}}{100} + (\frac{\text{A}}{\text{E}} \times \frac{\text{rate}}{\text{frequency}}))}{\frac{\text{par}}{100} + (\frac{\text{A}}{\text{E}} \times \frac{\text{rate}}{\text{frequency}})} \times \frac{\text{frequency} \times \text{E}}{\text{DSR}}$$

  where:

  - $\text{A}$ = number of days from the beginning of the coupon period to the settlement date (accrued days).
  - $\text{DSR}$ = number of days from the settlement date to the redemption date.
  - $\text{E}$ = number of days in the coupon period.

- If there is more than one coupon period until redemption, YIELD is calculated through a hundred iterations. The resolution uses the Newton method, based on the formula used for the function PRICE. The yield is changed until the estimated price given the yield is close to price.

- settlement and maturity are truncated to integers.

- frequency, and basis are rounded to the nearest integer.

- An error is returned if:
  - settlement or maturity is not a valid date.
  - settlement ≥ maturity.
  - rate < 0.
  - pr ≤ 0.
  - redemption ≤ 0.
  - frequency is any number other than 1, 2, or 4.
  - basis < 0 or basis > 4.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data**  | **Description**                     |
| --------- | ----------------------------------- |
| 15-Feb-08 | Settlement date                     |
| 15-Nov-16 | Maturity date                       |
| 5.75%     | Percent coupon                      |
| 95.04287  | Price                               |
| \\$100      | Redemption value                    |
| 2         | Frequency is semiannual (see above) |
| 0         | 30/360 basis (see above)            |

The following DAX query:

```dax
EVALUATE
{
  YIELD(DATE(2008,2,15), DATE(2016,11,15), 0.0575, 95.04287, 100, 2,0)
}
```

Returns the yield on a bond with the terms specified above.

| **[Value]**      |
| ------------------ |
| 0.0650000068807314 |
