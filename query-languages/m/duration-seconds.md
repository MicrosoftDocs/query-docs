---
title: "Duration.Seconds | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
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
manager: "kfile"
---
# Duration.Seconds

  
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
