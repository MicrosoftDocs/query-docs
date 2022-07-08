---
description: "Learn more about: XIRR"
title: "XIRR function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 12/17/2021
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# XIRR
  
Returns the internal rate of return for a schedule of cash flows that is not necessarily periodic.  
  
## Syntax  
  
```dax
XIRR(<table>, <values>, <dates>, [, <guess>[, <alternateResult>]])  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|A table for which the values and dates expressions should be calculated.|  
|values|An expression that returns the cash flow value for each row of the table.|  
|dates|An expression that returns the cash flow date for each row of the table.|  
|guess|(Optional) An initial guess for the internal rate of return. If omitted, the default guess of 0.1 is used.|  
|alternateResult | (Optional) A value returned in place of an error when a solution cannot be determined.|
  
## Return value

Internal rate of return for the given inputs. If the calculation fails to return a valid result, an error or value specified as alternateResult is returned.
  
## Remarks

- The value is calculated as the rate that satisfies the following function:  

    $$\sum^{N}\_{j=1} \frac{P\_{j}}{(1 + \text{rate})^{\frac{d\_{j} - d\_{1}}{365}}}$$

    Where:

  - $P\_{j}$ is the $j^{th}$ payment
  - $d\_{j}$ is the $j^{th}$ payment date
  - $d\_{1}$ is the first payment date

- The series of cash flow values must contain at least one positive number and one negative number.  

- Avoid using ISERROR or IFERROR functions to capture an error returned by XIRR. If some inputs to the function may result in a no solution error, providing an alternateResult parameter is the most reliable and highest performing way to handle the error.

- To learn more about using the alternateResult parameter, be to check out this [video](https://www.microsoft.com/videoplayer/embed/RWLzrC).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following formula calculates the internal rate of return of the CashFlows table:  
  
```dax
= XIRR( CashFlows, [Payment], [Date] )  
```
  
|Date|Payment|  
|--------|-----------|  
|1/1/2014|-10000|  
|3/1/2014|2750|  
|10/30/2014|4250|  
|2/15/2015|3250|  
|4/1/2015|2750|  
  
Rate of return = 37.49%  
