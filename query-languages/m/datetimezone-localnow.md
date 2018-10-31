---
title: "DateTimeZone.LocalNow | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTimeZone.LocalNow

  
## About  
Returns a DateTime value set to the current system date and time.  
  
## Syntax

<pre>
DateTimeZone.LocalNow() as datetimezone  
</pre>
  
## Remarks  
  
-   The return value contains timezone information representing the local timezone.  
  
## Example  
  
```powerquery-m 
DateTimeZone.LocalNow() equals 2011-02-20T22:19:38-08:00  
```  
