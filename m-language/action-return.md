---
title: "Action.Return | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 352efd58-8ae9-4f8b-8b78-eccdf7a99ec6
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Action.Return
  
<code>Action.Return(<b>value</b> as any) as action</code>  
  
## About  
  
Creates an action that performs no action when executed and returns <code>value</code> as its result.  
  
## Example 1  
Creates an action that, when executed, performs no action and returns the value <code>"hello world!"</code> as its result.  
  
<code>Action.Return("hello world!")</code>  
  
<code>action</code>  
