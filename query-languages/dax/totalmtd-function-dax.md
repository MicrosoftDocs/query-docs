---
description: "Learn more about: TOTALMTD"
title: "TOTALMTD function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# TOTALMTD

Evaluates the value of the **expression** for the month to date, in the current context.  
  
## Syntax  
  
```dax
TOTALMTD(<expression>,<dates>[,<filter>])  
```
  
### Parameters  
  
|Parameter|Definition|  
|-------------|--------------|  
|expression|An expression that returns a scalar value.|  
|dates|A column that contains dates.|  
|filter|(optional) An expression that specifies a filter to apply to the current context.|  
  
## Return value

A scalar value that represents the **expression** evaluated for the dates in the current month-to-date, given the dates in **dates**.  
  
## Remarks

- The **dates** argument can be any of the following:  
  - A reference to a date/time column.  
  - A table expression that returns a single column of date/time values.  
  - A Boolean expression that defines a single-column table of date/time values.  

- Constraints on Boolean expressions are described in the topic, [CALCULATE](calculate-function-dax.md).  
  
- The **filter** expression has restrictions described in the topic, [CALCULATE](calculate-function-dax.md).  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following sample formula creates a measure that calculates the 'month running total' or 'month running sum' for Internet sales.

```dax
= TOTALMTD(SUM(InternetSales_USD[SalesAmount_USD]),DateTime[DateKey])  
```
  
## See also

[ALL](all-function-dax.md)  
[CALCULATE](calculate-function-dax.md)  
[TOTALYTD](totalytd-function-dax.md)  
[TOTALQTD](totalqtd-function-dax.md)  
