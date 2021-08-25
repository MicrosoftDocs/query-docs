---
description: "Learn more about: TBILLPRICE"
title: "TBILLPRICE function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend 
recommendations: false

---

# TBILLPRICE

Returns the price per \\$100 face value for a Treasury bill.

## Syntax

```dax
TBILLPRICE(<settlement>, <maturity>, <discount>)
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|settlement|The Treasury bill's settlement date. The security settlement date is the date after the issue date when the Treasury bill is traded to the buyer.|
|maturity|The Treasury bill's maturity date. The maturity date is the date when the Treasury bill expires.|
|discount|The Treasury bill's discount rate.|

## Return Value

The Treasury Bill's price per \\$100 face value.

## Remarks

- Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899.

- TBILLPRICE is calculated as follows:

  $$\text{TBILLPRICE} = 100 \times (1 - \frac{\text{discount} \times \text{DSM}}{360})$$

  where:

  - $\text{DSM}$ = number of days from settlement to maturity, excluding any maturity date that is more than one calendar year after the settlement date.

- settlement and maturity are truncated to integers.

- An error is returned if:
  - settlement or maturity is not a valid date.
  - settlement ≥ maturity or maturity is more than one year after settlement.
  - discount ≤ 0.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data**  | **Description**       |
| --------- | --------------------- |
| 3/31/2008 | Settlement date       |
| 6/1/2008  | Maturity date         |
| 9.0%      | Percent discount rate |

The following DAX query:

```dax
EVALUATE
{
  TBILLPRICE(DATE(2008,3,31), DATE(2008,6,1), 0.09)
}
```

Returns the Treasury Bill's price per \\$100 face value, given the terms specified above.

| **[Value]** |
| ------------- |
| 98.45         |
