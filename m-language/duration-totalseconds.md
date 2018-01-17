---
title: "Duration.TotalSeconds | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: db5259e6-2eb8-4855-b342-fbc52879e5d5
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Duration.TotalSeconds
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the total magnitude of seconds from a duration value.  
  
```  
Duration.TotalSeconds(duration as nullable duration) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|duration|The Duration to parse.|  
  
## <a name="__goback"></a>Example  
  
```  
let  
duration = #duration(2,22,120,20)  
in  
[  
totaldays= Duration.TotalDays(duration) equals 3.0002  
totalhours= Duration.TotalHours(duration) equals 72.005  
totalminutes= Duration.TotalMinutes(duration) equals 4320.33  
totalseconds=Duration.TotalSeconds(duration) equals 259220  
]  
```  
