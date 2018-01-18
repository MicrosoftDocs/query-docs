---
title: "Value.Equals | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: deeffc0d-9ba9-4d78-832c-6b9b01a51fbb
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Value.Equals
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns whether two values are equal.  
  
```  
Value.Equals(left as any, right as any, equater as record) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|left|The left value to compare.|  
|right|The right value to compare.|  
|equater|Optional equater record.|  
  
## Examples  
  
```  
Value.Equals(2,4)   
equals false  
```  
  
```  
Value.Equals(2,4,  
[     
Equals= (x,y) => Number.Mod(x,2)=Number.Mod(y,2),     
Hash = (x) => Value.Hash(x)  
])equals true  
```  
