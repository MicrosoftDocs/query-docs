---
description: "Learn more about: ODDFYIELD"
title: "ODDFYIELD function (DAX)"
author: jajin7
---

# ODDFYIELD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the yield of a security that has an odd (short or long) first period.

## Syntax

```dax
ODDFYIELD(<settlement>, <maturity>, <issue>, <first_coupon>, <rate>, <pr>, <redemption>, <frequency>[, <basis>])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|`settlement`|The security's settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer.|
|`maturity`|The security's maturity date. The maturity date is the date when the security expires.|
|`issue`|The security's issue date.|
|`first_coupon`|The security's first coupon date.|
|`rate`|The security's interest rate.|
|`pr`|The security's price.|
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

The security's yield.

## Remarks

- Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899.

- The `settlement` date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2008, and is purchased by a buyer six months later. The issue date would be January 1, 2008, the settlement date would be July 1, 2008, and the maturity date would be January 1, 2038, which is 30 years after the January 1, 2008, issue date.

- ODDFYIELD is calculated using an iterative method. It uses the Newton method based on the formula used for the function ODDFPRICE. The yield is changed through 100 iterations until the estimated price with the given yield is close to the price. See ODDFPRICE for the formula that ODDFYIELD uses.

- settlement, maturity, issue, and first_coupon are truncated to integers.

- basis and frequency are rounded to the nearest integer.

- An error is returned if:
  - `settlement`, `maturity`, `issue`, or `first_coupon` is not a valid date.
  - `maturity` > `first_coupon` > `settlement` > `issue` is not satisfied.
  - `rate` < 0.
  - `pr` ≤ 0.
  - `redemption` ≤ 0.
  - `frequency` is any number other than 1, 2, or 4.
  - `basis` < 0 or `basis` > 4.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data**          | **Argument description** |
| ----------------- | ------------------------ |
| November 11, 2008 | Settlement date          |
| March 1, 2021     | Maturity date            |
| October 15, 2008  | Issue date               |
| March 1, 2009     | First coupon date        |
| 5.75%             | Percent coupon           |
| 84.50             | Price                    |
| 100               | Redemptive value         |
| 2                 | Frequency is semiannual  |
| 0                 | 30/360 basis             |

The following DAX query:

```dax
EVALUATE
{
  ODDFYIELD(DATE(2008,11,11), DATE(2021,3,1), DATE(2008,10,15), DATE(2009,3,1), 0.0575, 84.50, 100, 2, 0)
}
```

Returns the yield of a security that has an odd (short or long) first period, using the terms specified above.

| **[Value]**      |
| ------------------ |
| 0.0772455415972989 |
