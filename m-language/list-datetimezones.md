---
title: "List.DateTimeZones | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 77931583-f19b-41f5-b543-7bd0b2d9d434
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.DateTimeZones
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a list of of datetimezone values from size count, starting at start and adds an increment to every value.  
  
```  
List.DateTimeZones(start as datetimezone,  count as number, increment as duration) as { datetime }  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|start|The DateTimeZone to start at.|  
|count|The number of values to return.|  
|increment|The increment to add.|  
  
## Example  
  
```  
List.DateTimeZones(#datetimezone(2011, 12, 31, 23, 55, 0, -8, 0), 10, #duration(0, 0, 1, 0))  
  
equals  
  
{  
  
    #datetimezone(2011, 12, 31, 23, 55, 0, -8, 0),  
  
    #datetimezone(2011, 12, 31, 23, 56, 0, -8, 0),  
  
    #datetimezone(2011, 12, 31, 23, 57, 0, -8, 0),  
  
    #datetimezone(2011, 12, 31, 23, 58, 0, -8, 0),  
  
    #datetimezone(2011, 12, 31, 23, 59, 0, -8, 0),  
  
    #datetimezone(2012, 1, 1, 0, 0, 0, -8, 0),  
  
    #datetimezone(2012, 1, 1, 0, 1, 0, -8, 0),  
  
    #datetimezone(2012, 1, 1, 0, 2, 0, -8, 0),  
  
    #datetimezone(2012, 1, 1, 0, 3, 0, -8, 0),  
  
    #datetimezone(2012, 1, 1, 0, 4, 0, -8, 0)  
  
}  
```  
