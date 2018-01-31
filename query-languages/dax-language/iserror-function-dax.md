---
title: "ISERROR Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.ISERROR.f1"
helpviewer_keywords: 
  - "ISERROR function"
ms.assetid: 070f340e-8e31-4cc4-9516-2372fce19202
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# ISERROR Function (DAX)
Checks whether a value is an error, and returns TRUE or FALSE.  
  
## Syntax  
  
```  
ISERROR(<value>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**value**|The value you want to test.|  
  
## Return Value  
A Boolean value of TRUE if the value is an error; otherwise FALSE.  
  
## Example  
The following example calculates the ratio of total Internet sales to total reseller sales. The ISERROR function is used to check for errors, such as division by zero. If there is an error a blank is returned, otherwise the ratio is returned.  
  
```  
= IF( ISERROR(  
       SUM('ResellerSales_USD'[SalesAmount_USD])  
       /SUM('InternetSales_USD'[SalesAmount_USD])  
             )  
    , BLANK()  
    , SUM('ResellerSales_USD'[SalesAmount_USD])  
      /SUM('InternetSales_USD'[SalesAmount_USD])  
    )  
```  
  
## See Also  
[Information Functions &#40;DAX&#41;](information-functions-dax.md)  
[IFERROR Function &#40;DAX&#41;](iferror-function-dax.md)  
[IF Function &#40;DAX&#41;](if-function-dax.md)  
  
