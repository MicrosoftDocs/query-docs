---
title: "Text.Format | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 098ac7d8-f0ef-4ef2-89ad-b6dee5e6ef5f
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.Format
Text.Format(formatString as text, arguments as any, optional culture as nullable text) as text  
  
## About  
Returns formatted text that is created by applying arguments from a list or record to a format string formatString. Optionally, a culture may be specified.  
  
### Example 1  
Format a list of numbers.  
  
```  
Text.Format("#{0}, #{1}, and #{2}.", { 17, 7, 22 })  
```  
  
```  
Equals: "17, 7, and 22."  
```  
  
### Example 2  
Format different data types from a record according to United States English culture.  
  
```  
Text.Format("The time for the #[distance] km run held in #[city] on #[date] was #[duration].", [city = "Seattle", date = #date(2015, 3, 10), duration = #duration(0,0,54,40), distance = 10], "en-US")  
```  
  
```  
Equals: "The time for the 10 km run held in Seattle on 3/10/2015 was 00:54:40."  
```  
