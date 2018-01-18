---
title: "Number.Exp | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: cf19e771-4796-4172-bf4b-e1afdb71f219
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Number.Exp
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a number representing *e* raised to a power.  
  
```  
Number.Exp(number as nullable number) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|number|A number for which the exponential function is to be calculated. If number is null,  Number.Exp returns null.|  
  
## Examples  
  
```  
Number.Exp(0) equals 1  
```  
  
```  
Number.Exp(3) equals 20.085536923187668  
```  
