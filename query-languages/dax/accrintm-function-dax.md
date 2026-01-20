---
description: "Learn more about: ACCRINTM"
title: "ACCRINTM function (DAX) "
author: jajin7
ms.topic: reference
---

# ACCRINTM

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the accrued interest for a security that pays interest at maturity.

## Syntax

```dax
ACCRINTM(<issue>, <maturity>, <rate>, <par>[, <basis>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`issue`|The security's issue date.|
|`maturity`|The security's maturity date.|
|`rate`|The security's annual coupon rate.|
|`par`|The security's par value.|
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

The accrued interest.

## Remarks

- Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899.

- ACCRINTM is calculated as follows:

  $$\text{ACCRINTM} = \text{par} \times \text{rate} \times \frac{\text{A}}{\text{D}}$$

  where:

  - $\text{A}$ = Number of accrued days counted according to a monthly basis. For interest at maturity items, the number of days from the issue date to the maturity date is used.
  - $\text{D}$ = Annual Year Basis.

- issue and maturity are truncated to integers.

- basis is rounded to the nearest integer.

- An error is returned if:
  - issue or maturity is not a valid date.
  - issue ≥ maturity.
  - rate ≤ 0.
  - par ≤ 0.
  - basis < 0 or basis > 4.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data**     | **Description**              |
| ------------ | ---------------------------- |
| 1-April-2008 | Issue date                   |
| 15-June-2008 | Maturity date                |
| 10%          | Percent coupon               |
| 1000         | Par value                    |
| 3            | Actual/365 basis (see above) |

The following DAX query:

```dax
EVALUATE
{
  ACCRINTM(DATE(2008,4,1), DATE(2008,6,15), 0.1, 1000, 3)
}
```

Returns the accrued interest for a security with the terms specified above.

| **[Value]**    |
| ---------------- |
| 20.5479452054795 |
