---
description: "Learn more about: ODDLPRICE"
title: "ODDLPRICE function (DAX) | Microsoft Docs"
author: jajin7
---

# ODDLPRICE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the price per \\$100 face value of a security having an odd (short or long) last coupon period.

## Syntax

```dax
ODDLPRICE(<settlement>, <maturity>, <last_interest>, <rate>, <yld>, <redemption>, <frequency>[, <basis>])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|`settlement`|The security's settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer.|
|`maturity`|The security's maturity date. The maturity date is the date when the security expires.|
|`last_interest`|The security's last coupon date.|
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

- settlement, maturity, and last_interest are truncated to integers.

- basis and frequency are rounded to the nearest integer.

- An error is returned if:
  - settlement, maturity, or last_interest is not a valid date.
  - maturity > settlement > last_interest is not satisfied.
  - rate < 0.
  - yld < 0.
  - redemption ≤ 0.
  - frequency is any number other than 1, 2, or 4.
  - basis < 0 or basis > 4.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following DAX query:

| **Data**         | **Argument description** |
| ---------------- | ------------------------ |
| February 7, 2008 | Settlement date          |
| June 15, 2008    | Maturity date            |
| October 15, 2007 | Last interest date       |
| 3.75%            | Percent coupon           |
| 4.05%            | Percent yield            |
| \\$100             | Redemptive value         |
| 2                | Frequency is semiannual  |
| 0                | 30/360 basis             |

```dax
EVALUATE
{
  ODDLPRICE(DATE(2008,2,7), DATE(2008,6,15), DATE(2007,10,15), 0.0375, 0.0405, 100, 2, 0)
}
```

Returns the price per \\$100 face value of a security that has an odd (short or long) last coupon period, using the terms specified above.

| **[Value]**    |
| ---------------- |
| 99.8782860147213 |
