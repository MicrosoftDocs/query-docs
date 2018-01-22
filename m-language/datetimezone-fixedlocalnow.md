---
title: "DateTimeZone.FixedLocalNow | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 659f5278-3673-4d2b-8ae8-4a222377a1ae
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTimeZone.FixedLocalNow

  
## About  
Returns a DateTimeZone value set to the current date, time, and timezone offset on the system. This value is fixed and will not change with successive calls, unlike DateTime.LocalNow, which may return different values over the course of execution of an expression.  
  
```  
DateTimeZone.FixedLocalNow() as datetimezone  
```  
