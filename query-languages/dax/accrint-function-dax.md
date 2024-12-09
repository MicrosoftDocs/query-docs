---
description: "Learn more about: ACCRINT"
title: "ACCRINT function (DAX) "
author: jajin7
---

# ACCRINT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the accrued interest for a security that pays periodic interest.

## Syntax

```dax
ACCRINT(<issue>, <first_interest>, <settlement>, <rate>, <par>, <frequency>[, <basis>[, <calc_method>]])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|`issue`|The security's issue date.|  
|`first_interest`|The security's first interest date.|
|`settlement`|The security's settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer.|
|`rate`|The security's annual coupon rate.|
|`par`|The security's par value.|
|`frequency`|The number of coupon payments per year. For annual payments, frequency = 1; for semiannual, frequency = 2; for quarterly, frequency = 4.|
|`basis`|(Optional) The type of day count basis to use. If basis is omitted, it is assumed to be 0. The accepted values are listed below this table.|
|`calc_method`|(Optional) A logical value that specifies the way to calculate the total accrued interest when the date of settlement is later than the date of first_interest. If calc_method is omitted, it is assumed to be `TRUE`. <br/> - If calc_method evaluates to `TRUE` or is omitted, ACCRINT returns the total accrued interest from issue to settlement. <br/> - If calc_method evaluates to `FALSE`, ACCRINT returns the accrued interest from first_interest to settlement.|

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

- ACCRINT is calculated as follows:

  $$\text{ACCRINT} = \text{par} \times \frac{\text{rate}}{\text{frequency}} \times \sum^{\text{NC}}\_{i=1}\frac{\text{A}\_{i}}{\text{NL}\_{i}}$$

  where:

  - $\text{A}\_{i}$ = number of accrued days for the $i^{th}$ quasi-coupon period within odd period.
  - $\text{NC}$ = number of quasi-coupon periods that fit in odd period. If this number contains a fraction, raise it to the next whole number.
  - $\text{NL}\_{i}$ = normal length in days of the quasi-coupon period within odd period.

- issue, first_interest, and settlement are truncated to integers.

- frequency and basis are rounded to the nearest integer.

- An error is returned if:
  - issue, first_interest, or settlement is not a valid date.
  - issue ≥ settlement.
  - rate ≤ 0.
  - par ≤ 0.
  - frequency is any number other than 1, 2, or 4.
  - basis < 0 or basis > 4.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Examples

| **Data**       | **Description**                     |
| -------------- | ----------------------------------- |
| 1-March-2007   | Issue date                          |
| 31-August-2008 | First interest date                 |
| 1-May-2008     | Settlement date                     |
| 10%            | Coupon rate                         |
| 1000           | Par value                           |
| 2              | Frequency is semiannual (see above) |
| 0              | 30/360 basis (see above)            |

### Example 1

The following DAX query:

```dax
EVALUATE
{
  ACCRINT(DATE(2007,3,1), DATE(2008,8,31), DATE(2008,5,1), 0.1, 1000, 2, 0)
}
```

Returns the accrued interest from issue to settlement, for a security with the terms specified above.

| **[Value]**    |
| ---------------- |
| 116.944444444444 |

### Example 2

The following DAX query:

```dax
EVALUATE
{
  ACCRINT(DATE(2007,3,1), DATE(2008,8,31), DATE(2008,5,1), 0.1, 1000, 2, 0, FALSE)
}
```

Returns the accrued interest from first_interest to settlement, for a security with the terms specified above.

| **[Value]**    |
| ---------------- |
| 66.9444444444445 |
