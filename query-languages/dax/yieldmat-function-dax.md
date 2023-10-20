---
description: "Learn more about: YIELDMAT"
title: "YIELDMAT function (DAX) | Microsoft Docs"
author: jajin7
---

# YIELDMAT

Returns the annual yield of a security that pays interest at maturity.

## Syntax

```dax
YIELDMAT(<settlement>, <maturity>, <issue>, <rate>, <pr>[, <basis>])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|settlement|The security's settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer.|
|maturity|The security's maturity date. The maturity date is the date when the security expires.|
|issue|The security's issue date.|
|rate|The security's interest rate at date of issue.|
|pr|The security's price per \\$100 face value.|
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

The annual yield.

## Remarks

- Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899.

- The settlement date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2008, and is purchased by a buyer six months later. The issue date would be January 1, 2008, the settlement date would be July 1, 2008, and the maturity date would be January 1, 2038, which is 30 years after the January 1, 2008, issue date.

- settlement, maturity, and issue are truncated to integers.

- basis is rounded to the nearest integer.

- An error is returned if:
  - settlement, maturity, or issue is not a valid date.
  - maturity > settlement > issue is not satisfied.
  - rate < 0.
  - pr ≤ 0.
  - basis < 0 or basis > 4.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data**  | **Description**           |
| --------- | ------------------------- |
| 15-Mar-08 | Settlement date           |
| 3-Nov-08  | Maturity date             |
| 8-Nov-07  | Issue date                |
| 6.25%     | Percent semiannual coupon |
| 100.0123  | Price                     |
| 0         | 30/360 basis (see above)  |

The following DAX query:

```dax
EVALUATE
{
  YIELDMAT(DATE(2008,3,15), DATE(2008,11,3), DATE(2007,11,8), 0.0625, 100.0123, 0)
}
```

Returns the yield for a security using the terms specified above.

| **[Value]**      |
| ------------------ |
| 0.0609543336915387 |
