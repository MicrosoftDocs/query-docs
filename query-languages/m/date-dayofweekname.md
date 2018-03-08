---
title: "Date.DayOfWeekName | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
applies_to: 
  - "Power BI"
ms.assetid: bc66ef9f-2e47-420f-8e4d-16ef39d09124
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.DayOfWeekName
 

<code>Date.DayOfWeekName(**date** as any, optional **culture** as nullable text)</code>

## About
Returns the day of the week name for the provided <code>date</code> and, optionally, a culture <code>culture</code>.

## Example
Get the day of the week name.

<code>Date.DayOfWeekName(#date(2011, 12, 31), "en-US")</code>

<code>"Saturday"</code>


  
