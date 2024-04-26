---
description: "Learn more about: TBILLYIELD"
title: "TBILLYIELD function (DAX) | Microsoft Docs"
author: jajin7
---

# TBILLYIELD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the yield for a Treasury bill.

## Syntax

```dax
TBILLYIELD(<settlement>, <maturity>, <pr>)
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|settlement|The Treasury bill's settlement date. The security settlement date is the date after the issue date when the Treasury bill is traded to the buyer.|
|maturity|The Treasury bill's maturity date. The maturity date is the date when the Treasury bill expires.|
|pr|The Treasury bill's price per \\$100 face value.|

## Return Value

The Treasury bill's yield.

## Remarks

- Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899.

- TBILLYIELD is calculated as follows:

  $$\text{TBILLYIELD} = \frac{100 - \text{pr}}{\text{pr}} \times \frac{360}{\text{DSM}}$$

  where:

  - $\text{DSM}$ = number of days from settlement to maturity, excluding any maturity date that is more than one calendar year after the settlement date.

- settlement and maturity are truncated to integers.

- An error is returned if:
  - settlement or maturity is not a valid date.
  - settlement ≥ maturity or maturity is more than one year after settlement.
  - pr ≤ 0.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following DAX query:

| **Data**  | **Description**           |
| --------- | ------------------------- |
| 3/31/2008 | Settlement date           |
| 6/1/2008  | Maturity date             |
| \\$98.45    | Price per \\$100 face value |

```dax
EVALUATE
{
  TBILLYIELD(DATE(2008,3,31), DATE(2008,6,1), 98.45)
}
```

Returns the yield of a Treasury bill using the terms specified above.

| **[Value]**      |
| ------------------ |
| 0.0914169629253426 |
