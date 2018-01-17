---
title: "Duration.FromText | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 2254fc69-e06f-4aee-b50b-d62ba3478de8
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Duration.FromText
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a Duration value from a text value.  
  
```  
Duration.FromText(duration as nullable text) as nullable duration  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|Duration|The text to convert.|  
  
## Duration settings  
  
|**Format**|  
|--------------|  
|[-]hh:mm[:ss]|  
|[-]ddd.hh:mm[:ss]|  
  
**Note**: The values within brackets [] are optional.  
  
### Format parts  
  
|**Part**|**Description**|  
|------------|-------------------|  
|[-]|The text value is prepended with an optional negative sign [-] to indicate a negative duration value.|  
|[d]|The [d] part represents the day portion of the duration value.|  
|[m]|The [m] part represents the minute portion of the duration value.|  
|[s]|The [s] part represents the second portion of the duration value.|  
  
## Examples  
  
```  
Duration.FromText("15:35") equals 15 hours, 35 minutes  
```  
  
```  
Duration.FromText("2.15:00") equals 2 days, 15 hours  
```  
