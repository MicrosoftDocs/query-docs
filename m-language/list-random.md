---
title: "List.Random | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: fca8c17f-2ced-4b91-81ae-97bf9761e171
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.Random
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a list of random numbers between 0 and 1, given the number of values to generate and an optional seed value. <ul> <li><code>count</code>: The number of random values to generate.</li> <li><code>seed</code>: <i>[Optional]</i> A numeric value used to seed the random number generator. If omitted a unique list of random numbers is generated each time you call the function. If you specify the seed value with a number every call to the function generates the same list of random numbers.</li> </ul>  
  
```  
List.Random(count as number, optional seed as nullable number) as { Number }  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|count|How many random numbers to return.|  
|optional seed|Randomization seed value.|  
  
## Example  
  
```  
List.Random(10) equals { 0.44298228502412434, 0.11142372065755712, 0.81061893087374925, 0.69705957299892773, 0.84984056970562816, 0.45717397865707704, 0.27344677656583805, 0.51387371612427468, 0.14493200795023331, 0.89694489161341684 }  
```  
