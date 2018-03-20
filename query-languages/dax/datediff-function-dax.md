---
title: "DATEDIFF Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 729b2786-bd39-4cde-bec4-879f2d17aee7
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DATEDIFF Function (DAX)
  
Returns the count of interval boundaries crossed between two dates.  
  
## Syntax  
  
```  
DATEDIFF(<start_date>, <end_date>, <interval>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|start_date|A scalar datetime value.|  
|end_date|A scalar datetime value Return Value.|  
|interval|The interval to use when comparing dates. The value can be one of the following:<br /><br />-   SECOND<br />-   MINUTE<br />-   HOUR<br />-   DAY<br />-   WEEK<br />-   MONTH<br />-   QUARTER<br />-   YEAR|  
  
## Return Value  
The count of interval boundaries crossed between two dates.  
  
## Remarks  
An error is returned if start_date is larger than end_date.  
  
## Example  
  
|Date|  
|--------|  
|2012-12-31 23:59:59|  
|2013-01-01 00:00:00|  
  
The following all return 1:  
  
```  
DATEDIFF(MIN( Calendar[Date] ), MAX( Calendar[Date], second ) )  
  
DATEDIFF(MIN( Calendar[Date] ), MAX( Calendar[Date], minute ) )  
  
DATEDIFF(MIN( Calendar[Date] ), MAX( Calendar[Date], hour ) )  
  
DATEDIFF(MIN( Calendar[Date] ), MAX( Calendar[Date], day ) )  
  
DATEDIFF(MIN( Calendar[Date] ), MAX( Calendar[Date], week ) )  
  
DATEDIFF(MIN( Calendar[Date] ), MAX( Calendar[Date], month ) )  
  
DATEDIFF(MIN( Calendar[Date] ), MAX( Calendar[Date], quarter ) )  
  
DATEDIFF(MIN( Calendar[Date] ), MAX( Calendar[Date], year ) )  
```  
