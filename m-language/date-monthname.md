---
title: "Date.MonthName | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3dcacdbb-4dfb-4283-a0fc-cb4287755fd9
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Date.MonthName

<code>Date.MonthName(**date** as any, optional **culture** as nullable text)</code>

## About
Returns the name of the month component for the provided <code>date</code> and, optionally, a culture <code>culture</code>.

## Example
Get the month name.

<code>Date.MonthName(#datetime(2011, 12, 31, 5, 0, 0), "en-US")</code>

<code>"December"</code>

  
