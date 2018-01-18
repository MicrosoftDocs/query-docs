---
title: "ValueAction.Replace | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c4900602-1eb8-4ff4-bbae-52f060482c1c
caps.latest.revision: 3
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# ValueAction.Replace
<code>ValueAction.Replace(<b>target</b> as any, <b>source</b> as any) as action</code>  
## About  
Creates an action that when executed replaces the content of <code>target</code> with <code>source</code>. The function raises an evaluation error if <code>target</code> is not updatable or if <code>source</code> is not compatible with <code>target</code>. The action raises an execution error if the operation fails.   
  
<b>NOTE:</b> <code>target</code> may be left in a partially updated state if an execution error occurs.  
