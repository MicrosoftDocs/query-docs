---
description: "Learn more about: TOTALQTD"
title: "TOTALQTD function (DAX) | Microsoft Docs"
---
# TOTALQTD

Evaluates the value of the **expression** for the dates in the quarter to date, in the current context.  
  
## Syntax  
  
```dax
TOTALQTD(<expression>,<dates>[,<filter>])  
```
  
### Parameters  
  
|Parameter|Definition|  
|-------------|--------------|  
|expression|An expression that returns a scalar value.|  
|dates|A column that contains dates.|  
|filter|(optional) An expression that specifies a filter to apply to the current context.|  
  
## Return value

A scalar value that represents the **expression** evaluated for all dates in the current quarter to date, given the dates in **dates**.  
  
## Remarks

- The **dates** argument can be any of the following:  
  - A reference to a date/time column.  
  - A table expression that returns a single column of date/time values.  
  - A Boolean expression that defines a single-column table of date/time values.  
  
- Constraints on Boolean expressions are described in the topic, [CALCULATE](calculate-function-dax.md).  
  
- The **filter** expression has restrictions described in the topic, [CALCULATE](calculate-function-dax.md).  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following sample formula creates a measure that calculates the 'quarter running total' or 'quarter running sum' for Internet sales.  
  
```dax
= TOTALQTD(SUM(InternetSales_USD[SalesAmount_USD]),DateTime[DateKey])  
```
  
## See also

[ALL](all-function-dax.md)  
[CALCULATE](calculate-function-dax.md)  
[TOTALYTD](totalytd-function-dax.md)  
[TOTALMTD](totalmtd-function-dax.md)  
