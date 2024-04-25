---
description: "Learn more about: XNPV"
title: "XNPV function (DAX) | Microsoft Docs"
---
# XNPV

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]
  
Returns the present value for a schedule of cash flows that is not necessarily periodic.  
  
## Syntax  
  
```dax
XNPV(<table>, <values>, <dates>, <rate>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|A table for which the values and dates expressions should be calculated.|  
|values|An expression that returns the cash flow value for each row of the table.|  
|dates|An expression that returns the cash flow date for each row of the table.|  
|rate|The discount rate to apply to the cash flow for each row of the table.|  
  
## Return value

Net present value.  
  
## Remarks

- The value is calculated as the following summation:  

    $$\sum^{N}\_{j=1} \frac{P\_{j}}{(1 + \text{rate})^{\frac{d\_{j} - d\_{1}}{365}}}$$

    Where:

  - $P\_{j}$ is the $j^{th}$ payment
  - $d\_{j}$ is the $j^{th}$ payment date
  - $d\_{1}$ is the first payment date

- The series of cash flow values must contain at least one positive number and one negative number.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following calculates the present value of the CashFlows table:  
  
```dax
= XNPV( CashFlows, [Payment], [Date], 0.09 )  
```
  
|Date|Payment|  
|--------|-----------|  
|1/1/2014|-10000|  
|3/1/2014|2750|  
|10/30/2014|4250|  
|2/15/2015|3250|  
|4/1/2015|2750|  
  
Present value = 2086.65  
