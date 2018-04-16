---
title: "Duration.FromText | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Duration.FromText

  
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
