---
title: "DATEDIFF function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 11/19/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# DATEDIFF
  
Returns the count of interval boundaries crossed between two dates.  
  
## Syntax  
  
```dax
DATEDIFF(<start_date>, <end_date>, <interval>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|start_date|A scalar datetime value.|  
|end_date|A scalar datetime value Return value.|  
|interval|The interval to use when comparing dates. The value can be one of the following:<br /><br />-   SECOND<br />-   MINUTE<br />-   HOUR<br />-   DAY<br />-   WEEK<br />-   MONTH<br />-   QUARTER<br />-   YEAR|  
  
## Return value

The count of interval boundaries crossed between two dates.  
  
## Remarks

An error is returned if start_date is larger than end_date.  
  
## Example  
  
|Date|  
|--------|  
|2012-12-31 23:59:59|  
|2013-01-01 00:00:00|  
  
The following all return 1:  
  
```dax
DATEDIFF(MIN( Calendar[Date] ), MAX( Calendar[Date]), SECOND )  
  
DATEDIFF(MIN( Calendar[Date] ), MAX( Calendar[Date]), MINUTE )
  
DATEDIFF(MIN( Calendar[Date] ), MAX( Calendar[Date]), HOUR )
  
DATEDIFF(MIN( Calendar[Date] ), MAX( Calendar[Date]), DAY )
  
DATEDIFF(MIN( Calendar[Date] ), MAX( Calendar[Date]), WEEK )
  
DATEDIFF(MIN( Calendar[Date] ), MAX( Calendar[Date]), MONTH )
  
DATEDIFF(MIN( Calendar[Date] ), MAX( Calendar[Date]), QUARTER )
  
DATEDIFF(MIN( Calendar[Date] ), MAX( Calendar[Date]), YEAR ) 
```
