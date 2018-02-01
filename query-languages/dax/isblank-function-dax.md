---
title: "ISBLANK Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.ISBLANK.f1"
helpviewer_keywords: 
  - "ISBLANK function"
ms.assetid: 034fc4c7-0967-4304-ad1e-a5034835e6a0
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# ISBLANK Function (DAX)
Checks whether a value is blank, and returns TRUE or FALSE.  
  
## Syntax  
  
```  
ISBLANK(<value>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**value**|The value or expression you want to test.|  
  
## Return Value  
A Boolean value of TRUE if the value is blank; otherwise FALSE.  
  
## Example  
This formula computes the increase or decrease ratio in sales compared to the previous year. The example uses the IF function to check the value for the previous year's sales in order to avoid a divide by zero error.  
  
|Row Labels|Total Sales|Total Sales Previous Year|Sales to Previous Year Ratio|  
|--------------|---------------|-----------------------------|--------------------------------|  
|2005|$10,209,985.08|||  
|2006|$28,553,348.43|$10,209,985.08|179.66%|  
|2007|$39,248,847.52|$28,553,348.43|37.46%|  
|2008|$24,542,444.68|$39,248,847.52|-37.47%|  
|Grand Total|$102,554,625.71|||  
  
```  
//Sales to Previous Year Ratio  
  
=IF( ISBLANK('CalculatedMeasures'[PreviousYearTotalSales])  
   , BLANK()  
   , ( 'CalculatedMeasures'[Total Sales]-'CalculatedMeasures'[PreviousYearTotalSales] )  
      /'CalculatedMeasures'[PreviousYearTotalSales])  
```  
  
## See Also  
[Information Functions &#40;DAX&#41;](information-functions-dax.md)  
  
