---
description: "Learn more about: HASONEVALUE"
title: "HASONEVALUE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# HASONEVALUE

Returns **TRUE** when the context for *columnName* has been filtered down to one distinct value only. Otherwise is **FALSE**.  
  
## Syntax  
  
```html  
HASONEVALUE(<columnName>)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
| columnName   |  The name of an existing column, using standard DAX syntax. It cannot be an expression.  |  

## Return value

**TRUE** when the context for *columnName* has been filtered down to one distinct value only. Otherwise is **FALSE**.  
  
## Remarks  
  
- An equivalent expression for HASONEVALUE() is `COUNTROWS(VALUES(<columnName>)) = 1`.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following measure formula verifies if the context is being sliced by one value in order to estimate a percentage against a predefined scenario; in this case you want to compare Reseller Sales against sales in 2007, then you need to know if the context is filtered by single years. Also, if the comparison is meaningless you want to return BLANK.
  
```dax
= IF(HASONEVALUE(DateTime[CalendarYear]),SUM(ResellerSales_USD[SalesAmount_USD])/CALCULATE(SUM(ResellerSales_USD[SalesAmount_USD]),DateTime[CalendarYear]=2007),BLANK())  
```
