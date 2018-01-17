---
title: "Duration.Seconds | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c067d5df-40eb-4d31-8e52-c17400be4fc1
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Duration.Seconds
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a second component of a Duration value.  
  
```  
Duration.Seconds(duration as nullable duration) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|duration|The Duration to parse.|  
  
## Examples  
  
```  
duration1 = Duration.FromText("2.05:55:20")  
```  
  
```  
duration2 = Duration.FromText("15:50")  
```  
  
```  
Duration.Days(duration1) equals 2  
```  
  
```  
Duration.Hours(duration1) equals 5  
```  
  
```  
Duration.Minutes(duration1) equals 55  
```  
  
```  
Duration.Seconds(duration1) equals 20  
```  
  
```  
Duration.Seconds(duration2) equals 0  
```  
