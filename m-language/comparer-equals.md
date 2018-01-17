---
title: "Comparer.Equals | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: df753936-e08c-4d79-9042-3fd474b36f6f
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Comparer.Equals
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a logical value based on the equality check over the two given values.  
  
```  
Comparer.Equals(comparer as function, x as any, y as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|comparer|The comparer function is used to perform the operation.|  
|x|The left value to compare.|  
|y|The right value to compare.|  
  
## Example  
  
```  
let  
comparer1 = Comparer.FromCulture("en-us", false),  
comparer2 = Comparer.FromCulture("en-us", true)      
in       
[         
Test1 =  Comparer.Equals(comparer1,"a","A"), equals false   
Test2 = Comparer.Equals(comparer2,"a","A") equals true       
]  
```  
