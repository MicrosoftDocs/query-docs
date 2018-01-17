---
title: "TableAction.InsertRows | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 6c7c3e4c-068a-4e51-9dc1-b4821fa6c4a6
caps.latest.revision: 3
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# TableAction.InsertRows
<code>TableAction.InsertRows(<b>table</b> as table, <b>rowsToInsert</b> as table) as action</code>  
## About  
Creates an action that inserts <code>rowsToInsert</code> into <code>table</code>. The action returns a table containing the inserted rows as they appear in <code>table</code> after the action executes. Target-specific default values are used for the columns in <code>table</code> that are not specified in <code>rowsToInsert</code>. The function raises an evaluation error if <code>table</code> is not updatable or if <code>rowsToInsert</code> is not compatible with <code>table</code>. The action raises an execution error if the operation fails.   
  
<b>NOTE:</b> <code>table</code> may be left in a partially updated state if an execution error occurs.  
