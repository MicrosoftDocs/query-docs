---
title: "RRI function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend

---

# RRI

Returns an equivalent interest rate for the growth of an investment.

## Syntax

```dax
RRI(<nper>, <pv>, <fv>)
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|nper|The number of periods for the investment.|
|pv|The present value of the investment.|
|fv|The future value of the investment.|

## Return Value

The equivalent interest rate.

## Remarks

- RRI returns the interest rate given $\text{nper}$ (the number of periods), $\text{pv}$ (present value), and $\text{fv}$ (future value), calculated by using the following equation:

  $$\bigg( \frac{\text{fv}}{\text{pv}} \bigg)^{(\frac{1}{\text{}nper})} - 1$$

- An error is returned if:
  - nper ≤ 0.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

| **Data** | **Description** |
| -------- | --------------- |
| \\$10,000  | Present value   |
| \\$21,000  | Future value    |
| 4        | Years invested  |

The following DAX query:

```dax
EVALUATE
{
  RRI(4*12, 10000, 21000)
}
```

Returns an equivalent interest rate for the growth of an investment with the terms specified above.

| **[Value]**      |
| ------------------ |
| 0.0155771057566627 |
