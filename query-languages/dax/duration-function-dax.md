---
description: "Learn more about: DURATION"
title: "DURATION function (DAX) | Microsoft Docs"
author: jajin7
---

# DURATION

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the Macauley duration for an assumed par value of \\$100. Duration is defined as the weighted average of the present value of cash flows, and is used as a measure of a bond price's response to changes in yield.

## Syntax

```dax
DURATION(<settlement>, <maturity>, <coupon>, <yld>, <frequency>[, <basis>])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|settlement|The security's settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer.|
|maturity|The security's maturity date. The maturity date is the date when the security expires.|
|coupon|The security's annual coupon rate.|
|yld|The security's annual yield.|
|frequency|The number of coupon payments per year. For annual payments, frequency = 1; for semiannual, frequency = 2; for quarterly, frequency = 4.|
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

The Macauley duration.

## Remarks

- Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899.

- The settlement date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2008, and is purchased by a buyer six months later. The issue date would be January 1, 2008, the settlement date would be July 1, 2008, and the maturity date is January 1, 2038, which is 30 years after the January 1, 2008, issue date.

- settlement and maturity are truncated to integers.

- frequency, and basis are rounded to the nearest integer.

- An error is returned if:
  - settlement or maturity is not a valid date.
  - settlement ≥ maturity.
  - coupon < 0.
  - yld < 0
  - frequency is any number other than 1, 2, or 4.
  - basis < 0 or basis > 4.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data**   | **Description**                     |
| ---------- | ----------------------------------- |
| 07/01/2018 | Settlement date                     |
| 01/01/2048 | Maturity date                       |
| 8.0%       | Percent coupon                      |
| 9.0%       | Percent yield                       |
| 2          | Frequency is semiannual (see above) |
| 1          | Actual/actual basis (see above)     |

The following DAX query:

```dax
EVALUATE
{
  DURATION(DATE(2018,7,1), DATE(2048,1,1), 0.08, 0.09, 2, 1)
}
```

Returns the Macauley duration for a bond with the terms specified above.

| **[Value]**    |
| ---------------- |
| 10.9191452815919 |
