---
title: "Date.DayOfWeekName | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.DayOfWeekName
 

<code>Date.DayOfWeekName(**date** as any, optional **culture** as nullable text)</code>

## About
Returns the day of the week name for the provided <code>date</code> and, optionally, a culture <code>culture</code>.

## Example
Get the day of the week name.

<code>Date.DayOfWeekName(#date(2011, 12, 31), "en-US")</code>

<code>"Saturday"</code>


  
