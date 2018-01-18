---
title: "CALCULATETABLE Function (DAX) | Microsoft Docs"
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
f1_keywords: 
  - "sql13.as.daxref.CALCULATETABLE.f1"
helpviewer_keywords: 
  - "CALCULATETABLE function"
ms.assetid: 8f0bb370-0ace-478d-9ea9-0f98c66db620
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# CALCULATETABLE Function (DAX)
Evaluates a table expression in a context modified by the given filters.  
  
## Syntax  
  
```  
CALCULATETABLE(<expression>,<filter1>,<filter2>,…)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**Expression**|The table expression to be evaluated|  
|**filter1***,***filter2***,…*|A Boolean expression or a table expression that defines a filter|  
  
The expression used as the first parameter must be a function that returns a table.  
  
The following restrictions apply to Boolean expressions that are used as arguments:  
  
-   The expression cannot reference a measure.  
  
-   The expression cannot use a nested CALCULATE function.  
  
-   The expression cannot use any function that scans a table or returns a table, including aggregation functions.  
  
However, a Boolean expression can use any function that looks up a single value, or that calculates a scalar value.  
  
## Return Value  
A table of values.  
  
## Remarks  
The CALCULATETABLE function changes the context in which the data is filtered, and evaluates the expression in the new context that you specify. For each column used in a filter argument, any existing filters on that column are removed, and the filter used in the filter argument is applied instead.  
  
This function is a synonym for the RELATEDTABLE function.  
  
## Example  
The following example uses the CALCULATETABLE function to get the sum of Internet sales for 2006. This value is later used to calculate the ratio of Internet sales compared to all sales for the year 2006.  
  
The following table shows the results from the following formula.  
  
|Row Labels|Internet SalesAmount_USD|CalculateTable 2006 Internet Sales|Internet Sales to 2006 ratio|  
|--------------|-----------------------------|--------------------------------------|--------------------------------|  
|2005|$2,627,031.40|$5,681,440.58|0.46|  
|2006|$5,681,440.58|$5,681,440.58|1.00|  
|2007|$8,705,066.67|$5,681,440.58|1.53|  
|2008|$9,041,288.80|$5,681,440.58|1.59|  
|Grand Total|$26,054,827.45|$5,681,440.58|4.59|  
  
```  
=SUMX( CALCULATETABLE('InternetSales_USD', 'DateTime'[CalendarYear]=2006)  
     , [SalesAmount_USD])  
```  
  
## See Also  
[RELATEDTABLE Function &#40;DAX&#41;](../DAX/relatedtable-function-dax.md)  
[Filter Functions &#40;DAX&#41;](../DAX/filter-functions-dax.md)  
  
