---
title: "Date.MonthName | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.MonthName

<code>Date.MonthName(**date** as any, optional **culture** as nullable text)</code>

## About
Returns the name of the month component for the provided <code>date</code> and, optionally, a culture <code>culture</code>.

## Example
Get the month name.

<code>Date.MonthName(#datetime(2011, 12, 31, 5, 0, 0), "en-US")</code>

<code>"December"</code>

  
