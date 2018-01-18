---
title: "ActiveDirectory.Domains | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 0debabb5-08b2-4d16-b4ae-a0e6cd19f75a
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# ActiveDirectory.Domains
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table with Domain information available in the current domain or optional Active Directory forest.  
  
```  
ActiveDirectory.Domains(optional forestRootDomainName as nullable text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|optional forestRootDomainName|**Optional** Active Directory forest.|  
  
