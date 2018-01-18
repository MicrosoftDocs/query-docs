---
title: "DAX Semantic error: A function ‘CALCULATE’ has been used in a true-false expression that is used as a table filter expression. This is not allowed. | Microsoft Docs"
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
ms.assetid: 7d54a775-f504-4124-bae0-c903d121a414
caps.latest.revision: 3
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# DAX Semantic error: A function ‘CALCULATE’ has been used in a true-false expression that is used as a table filter expression. This is not allowed.
  
## Cause  
This error can appear when one or more filter expressions cannot be used in context of the measure or calculated column expression.  
  
In most cases, this error is caused by a filter expression specified as an argument to the [CALCULATE Function &#40;DAX&#41;](../DAX/calculate-function-dax.md) function. The CALCULATE function requires filters defined as a Boolean expression or a table expression.  
  
For example, the following measure expression returns the sum of SalesAmount in the Sales table for all sales in 2013. There is a relationship between the Sales table and a Date table with a CalendarYear column.  
  
```  
=CALCULATE(  
SUM(Sales[SalesAmount]),   
'Date'[CalendarYear] = 2013)   
)  
```  
In this case, `'Date'[CalendarYear] = 2013` is a filter expression passed to the CALCULATE function.  No error is returned and sum of SalesAmount is calculated successfully for all sales in 2013.  
  
This next measure expression attempts to return the sum of SalesAmount for the last year in CalendarYear.  
  
```  
=CALCULATE(  
SUM(Sales[SalesAmount]),   
MAX(Date[CalendarYear])  
)  
```  
The filter expression, `MAX('Date'[CalendarYear])` attempts to return the largest numeric value in the CalendarYear column.  However, in context of the measure expression, it cannot be passed as a table filter expression to the CALCULATE function, causing an error.  
  
## To fix this error  
Use the [FILTER Function &#40;DAX&#41;](../DAX/filter-function-dax.md) function to define filters as a table expression.  
  
Using the example above, to return the last year in CalendarYear, the FILTER function can be used to return a table filtered by another filter expression; one that uses the [MAX Function &#40;DAX&#41;](../DAX/max-function-dax.md) function to return the last year:  
  
```  
=CALCULATE(  
SUM(Sales[SalesAmount]),  
FILTER(  
ALL(  
       'Date'[CalendarYear]),   
      [CalendarYear] = MAX('Date'[CalendarYear])  
)  
)  
```  
The FILTER function evaluates the Date table according to the defined filter:  
  
```  
ALL('Date'[CalendarYear]), [CalendarYear] = MAX('Date'[CalendarYear])  
```  
This expression uses the MAX function to evaluate the CalendarYear column in the Date table and return the largest number. The [ALL Function &#40;DAX&#41;](../DAX/all-function-dax.md) function is used to clear any additional filters and evaluate all rows in the Date table. The FILTER function then passes the last year as a table filter expression to the CALCULATE function. The sum of SalesAmount is then evaluated by the table filter expression containing a single row and a single column, with the last year in CalendarYear. No error is returned and the calculation completes successfully.  
  
