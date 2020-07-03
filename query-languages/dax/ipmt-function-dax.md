---
title: "IPMT function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend

---

# IPMT

Returns the interest payment for a given period for an investment based on periodic, constant payments and a constant interest rate.

## Syntax

```dax
IPMT(<rate>, <per>, <nper>, <pv>[, <fv>[, <type>]])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|rate|The interest rate per period.|
|per|The period for which you want to find the interest. Must be between 1 and nper (inclusive).|
|nper|The total number of payment periods in an annuity.|
|pv|The present value, or the lump-sum amount that a series of future payments is worth right now.|
|fv|(Optional) The future value, or a cash balance you want to attain after the last payment is made. If fv is omitted, it is assumed to be BLANK.|
|type|(Optional) The number 0 or 1 which indicates when payments are due. If type is omitted, it is assumed to be 0. The accepted values are listed below this table.|

The **type** parameter accepts the following values:

| **Set type equal to** | **If payments are due**        |
| --------------------- | ------------------------------ |
| 0 or omitted          | At the end of the period       |
| 1                     | At the beginning of the period |

## Return Value

The interest payment for the given period.

## Remarks

- Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at 12 percent annual interest, use 0.12/12 for rate and 4*12 for nper. If you make annual payments on the same loan, use 0.12 for rate and 4 for nper.

- For all the arguments, cash you pay out, such as deposits to savings, is represented by negative numbers; cash you receive, such as dividend checks, is represented by positive numbers.

- type is rounded to the nearest integer.

- An error is returned if:
  - per < 1 or per > nper
  - nper < 1

## Examples

| **Data** | **Description**       |
| -------- | --------------------- |
| 10.00%   | Annual interest       |
| 3        | Years of loan         |
| \$8,000   | Present value of loan |

### Example 1

The following DAX query:

```dax
EVALUATE
{
  IPMT(0.1/12, 1, 3*12, 8000)
}
```

Returns the monthly interest due in the first month for a loan with the terms specified above.

| **[Value]**      |
| ------------------ |
| -66.6666666666667 |

### Example 2

The following DAX query:

```dax
EVALUATE
{
  IPMT(0.1, 3, 3, 8000)
}
```

Returns the yearly interest due in the last year for a loan with the terms specified above, where payments are made yearly.

| **[Value]**      |
| ------------------ |
| -292.447129909366 |
