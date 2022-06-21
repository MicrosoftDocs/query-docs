---
description: "Learn more about: COUPNUM"
title: "COUPNUM function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend 
recommendations: false

---

# COUPNUM

Returns the number of coupons payable between the settlement date and maturity date, rounded up to the nearest whole coupon.

## Syntax

```dax
COUPNUM(<settlement>, <maturity>, <frequency>[, <basis>])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|settlement|The security's settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer.|  
|maturity|The security's maturity date. The maturity date is the date when the security expires.|
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

The number of coupons payable between the settlement date and maturity date.

## Remarks

- Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899.

- The settlement date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2008, and is purchased by a buyer six months later. The issue date would be January 1, 2008, the settlement date would be July 1, 2008, and the maturity date would be January 1, 2038, which is 30 years after the January 1, 2008, issue date.

- settlement and maturity are truncated to integers.

- frequency and basis are rounded to the nearest integer.

- An error is returned if:
  - settlement or maturity is not a valid date.
  - settlement ≥ maturity.
  - frequency is any number other than 1, 2, or 4.
  - basis < 0 or basis > 4.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data**  | **Description**                 |
| --------- | ------------------------------- |
| 25-Jan-07 | Settlement date                 |
| 15-Nov-08 | Maturity date                   |
| 2         | Semiannual coupon (see above)   |
| 1         | Actual/actual basis (see above) |

The following DAX query:

```dax
EVALUATE
{
  COUPNUM(DATE(2007,1,25), DATE(2008,11,15), 2, 1)
}
```

Returns the number of coupon payments for a bond with the terms specified above.

| **[Value]** |
| ------------- |
| 4             |
