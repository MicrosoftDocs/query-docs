---
title: "List.DateTimeZones | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.DateTimeZones

  
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
