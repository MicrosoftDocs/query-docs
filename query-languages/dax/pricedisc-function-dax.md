---
description: "Learn more about: PRICEDISC"
title: "PRICEDISC function (DAX) | Microsoft Docs"
author: jajin7
---

# PRICEDISC

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the price per \\$100 face value of a discounted security.

## Syntax

```dax
PRICEDISC(<settlement>, <maturity>, <discount>, <redemption>[, <basis>])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|settlement|The security's settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer.|
|maturity|The security's maturity date. The maturity date is the date when the security expires.|
|discount|The security's discount rate.|
|redemption|The security's redemption value per \\$100 face value.|
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

- The settlement date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2018, and is purchased by a buyer six months later. The issue date would be January 1, 2018, the settlement date would be July 1, 2018, and the maturity date would be January 1, 2048, 30 years after the January 1, 2018, issue date.

- PRICEDISC is calculated as follows:

  $$\text{PRICEDISC} = \text{redemption} - \text{discount} \times \text{redemption} \times \frac{\text{DSM}}{\text{B}}$$

  where:

  - $\text{B}$ = number of days in year, depending on year basis.
  - $\text{DSM}$ = number of days from settlement to maturity.

- settlement and maturity are truncated to integers.

- basis is rounded to the nearest integer.

- An error is returned if:
  - settlement or maturity is not a valid date.
  - settlement ≥ maturity.
  - discount ≤ 0.
  - redemption ≤ 0.
  - basis < 0 or basis > 4.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data**  | **Argument description** |
| --------- | ------------------------ |
| 2/16/2008 | Settlement date          |
| 3/1/2008  | Maturity date            |
| 5.25%     | Percent discount rate    |
| \\$100      | Redemption value         |
| 2         | Actual/360 basis         |

The following DAX query:

```dax
EVALUATE
{
  PRICEDISC(DATE(2008,2,16), DATE(2008,3,1), 0.0525, 100, 2)
}
```

Returns the bond price per \\$100 face value, for a bond with the terms specified above.

| **[Value]**    |
| ---------------- |
| 99.7958333333333 |
