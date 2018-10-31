---
title: "DateTimeZone.FixedLocalNow | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTimeZone.FixedLocalNow

  
## About  
Returns a DateTimeZone value set to the current date, time, and timezone offset on the system. This value is fixed and will not change with successive calls, unlike DateTime.LocalNow, which may return different values over the course of execution of an expression.  
  
## Syntax

<pre> 
DateTimeZone.FixedLocalNow() as datetimezone  
```  
