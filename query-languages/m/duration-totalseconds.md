---
title: "Duration.TotalSeconds | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Duration.TotalSeconds

  
## About  
Returns the total magnitude of seconds from a duration value.  
  
## Syntax

<pre>
Duration.TotalSeconds(duration as nullable duration) as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|duration|The Duration to parse.|  
  
## <a name="__goback"></a>Example  
  
```powerquery-m
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
