---
title: "Date.ToRecord | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.ToRecord

  
## About  
Returns a record containing parts of a Date value.  
  
```  
Date.ToRecord(date as date) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|date|The Date to parse.|  
  
## Example  
  
```  
Date.ToRecord(#date(2013, 1, 1) equals [Year=2013,Month=1,Day=1]  
```  
