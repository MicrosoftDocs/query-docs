---
title: "Json.FromValue | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Json.FromValue
Json.FromValue(value as any, optional encoding as nullable number) as binary  
  
## About  
Produces a JSON representation of a given value value with a text encoding specified by encoding. If encoding is omitted, UTF8 is used. Values are represented as follows:  
  
|Value|  
|---------|  
|Null, text and logical values are represented as the corresponding JSON types.|  
|Numbers are represented as numbers in JSON, except that #infinity, -#infinity and #nan are converted to null.|  
|Lists are represented as JSON arrays.|  
|Records are represented as JSON objects.|  
|Tables are represented as an array of objects.|  
|Dates, times, datetimes, datetimezones and durations are represented as ISO-8601 text.|  
|Binary values are represented as base-64 encoded text.|  
|Types and functions produce an error.|  
  
### Example 1  
Convert a complex value to JSON.  
  
```  
Text.FromBinary(Json.FromValue([A={1, true, "3"}, B=#date(2012, 3, 25)]))  
```  
  
```  
Equals: "{""A"":[1,true,""3""],""B"":""2012-03-25""}"  
```  
