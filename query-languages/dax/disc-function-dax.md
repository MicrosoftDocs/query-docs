---
title: "DISC function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend

---

# DISC

Returns the discount rate for a security.

## Syntax

```dax
DISC(<settlement>, <maturity>, <pr>, <redemption>[, <basis>])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|settlement|The security's settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer.|
|maturity|The security's maturity date. The maturity date is the date when the security expires.|
|pr|The security's price per \\$100 face value.|
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

The discount rate.

## Remarks

- Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899.

- The settlement date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2018, and is purchased by a buyer six months later. The issue date would be January 1, 2018, the settlement date would be July 1, 2018, and the maturity date would be January 1, 2048, 30 years after the January 1, 2018, issue date.

- DISC is calculated as follows:

  $$\text{DISC} = \frac{\text{redemption} - \text{par}}{\text{redemption}} \times \frac{\text{B}}{\text{DSM}}$$

  where:

  - $\text{B}$ = number of days in a year, depending on the year basis.

  - $\text{DSM}$ = number of days between settlement and maturity.

- settlement and maturity are truncated to integers.

- basis is rounded to the nearest integer.

- An error is returned if:
  - settlement or maturity is not a valid date.
  - settlement ≥ maturity.
  - pr ≤ 0.
  - redemption ≤ 0.
  - basis < 0 or basis > 4.

## Example

| **Data**   | **Description**                 |
| ---------- | ------------------------------- |
| 07/01/2018 | Settlement date                 |
| 01/01/2048 | Maturity date                   |
| 97.975     | Price                           |
| 100        | Redemption value                |
| 1          | Actual/actual basis (see above) |

The following DAX query:

```dax
EVALUATE
{
  DISC(DATE(2018,7,1), DATE(2048,1,1), 97.975, 100, 1)
}
```

Returns the bond discount rate, for a bond with the terms specified above.

| **[Value]**        |
| -------------------- |
| 0.000686384169121348 |
