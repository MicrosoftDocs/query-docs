---
title: "TBILLEQ function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend

---

# TBILLEQ

Returns the bond-equivalent yield for a Treasury bill.

## Syntax

```dax
TBILLEQ(<settlement>, <maturity>, <discount>)
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|settlement|The Treasury bill's settlement date. The security settlement date is the date after the issue date when the Treasury bill is traded to the buyer.|
|maturity|The Treasury bill's maturity date. The maturity date is the date when the Treasury bill expires.|
|discount|The Treasury bill's discount rate.|

## Return Value

The Treasury Bill's bond-equivalent yield.

## Remarks

- Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899.

- TBILLEQ is calculated as:

  $$\text{TBILLEQ} = \frac{365 \times \text{discount}}{360 - (\text{discount} \times \text{DSM})}$$

  where:

  - $\text{DSM}$ is the number of days between settlement and maturity computed according to the 360 days per year basis.

- settlement and maturity are truncated to integers.

- An error is returned if:
  - settlement or maturity is not a valid date.
  - settlement ≥ maturity or maturity is more than one year after settlement.
  - discount ≤ 0.

## Example

| **Data**  | **Description**       |
| --------- | --------------------- |
| 3/31/2008 | Settlement date       |
| 6/1/2008  | Maturity date         |
| 9.14%     | Percent discount rate |

The following DAX query:

```dax
EVALUATE
{
  TBILLEQ(DATE(2008,3,31), DATE(2008,6,1), 0.0914)
}
```

Returns the bond-equivalent yield for a Treasury bill using the terms specified above.

| **[Value]**     |
| ----------------- |
| 0.094151493565943 |
