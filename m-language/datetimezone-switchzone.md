---
title: "DateTimeZone.SwitchZone | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 6733d798-b76f-4661-af57-f50308691b82
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# DateTimeZone.SwitchZone
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Changes the timezone information for the input DateTimeZone.  
  
```  
DateTimeZone(dateTimeZone as datetimezone, timezoneHours as number,  optional timezoneMinutes as nullablenumber ) as nullable datetimezone  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTimeZone|The DateTimeZone to modify.|  
|timezoneHours|The house to add.|  
|optional timezoneMinutes|The minuts to add.|  
  
## <a name="__toc360789106"></a>Remarks  
  
-   If the input value does not have a timezone component, DateTimeZone.SwitchZone throws Expression.Error.  
  
## Examples  
  
```  
DateTimeZone.SwitchZone(#datetimezone(2010, 5, 4, 6, 5, 5, 0, 0), 8) equals #datetimezone(2010, 5, 4, 14, 5, 5, 8, 0)  
```  
  
```  
DateTimeZone.SwitchZone(#datetimezone(2010, 12, 31, 11, 56, 02, 7, 30), 0, -30) equals #datetimezone(2010, 12, 31, 3, 56, 2, 0, -30)  
```  
