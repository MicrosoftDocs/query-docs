---
title: "DateTime.LocalNow | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.LocalNow

  
## About  
Returns a datetime value set to the current date and time on the system.  
  
## Syntax

<pre>
DateTime.LocalNow() as datetime  
</pre>
  
## Remarks  
  
-   The returned value does not contain timezone information.  
  
## Example  
  
```powerquery-m 
DateTime.LocalNow()equals 2013-03-08T14:22:42  
```  
