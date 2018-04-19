---
title: "DateTime.ToRecord | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.ToRecord

  
## About  
Returns a record containing parts of a DateTime value.  
  
```  
DateTime.ToRecord(dateTime as datetime) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to parse.|  
  
## Example  
  
```  
DateTime.ToRecord(#datetime(2013,1,3,12,4,5)) equals  
[             
Year = 2013,   Month = 1,   Day = 3,         
Hour = 12,  Minute = 4, Second = 5  
]  
```  
