---
title: "ISERROR Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
  
