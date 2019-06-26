---
title: "ISBLANK function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/26/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ISBLANK
Checks whether a value is blank, and returns TRUE or FALSE.  
  
## Syntax  
  
```dax
ISBLANK(<value>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|value|The value or expression you want to test.|  
  
## Return value  
A Boolean value of TRUE if the value is blank; otherwise FALSE.  
  
## Example  
This formula computes the increase or decrease ratio in sales compared to the previous year. The example uses the IF function to check the value for the previous year's sales in order to avoid a divide by zero error.  

```dax
//Sales to Previous Year Ratio  
  
=IF( ISBLANK('CalculatedMeasures'[PreviousYearTotalSales])  
   , BLANK()  
   , ( 'CalculatedMeasures'[Total Sales]-'CalculatedMeasures'[PreviousYearTotalSales] )  
      /'CalculatedMeasures'[PreviousYearTotalSales])  
```

Result 

|Row Labels|Total Sales|Total Sales Previous Year|Sales to Previous Year Ratio|  
|--------------|---------------|-----------------------------|--------------------------------|  
|2005|$10,209,985.08|||  
|2006|$28,553,348.43|$10,209,985.08|179.66%|  
|2007|$39,248,847.52|$28,553,348.43|37.46%|  
|2008|$24,542,444.68|$39,248,847.52|-37.47%|  
|Grand Total|$102,554,625.71|||  
  

  
## See also  
[Information functions &#40;DAX&#41;](information-functions-dax.md)  
  
