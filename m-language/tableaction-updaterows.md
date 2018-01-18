---
title: "TableAction.UpdateRows | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: d9d16cc5-92a9-4f3c-b7d3-b0011bf4f9ab
caps.latest.revision: 3
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# TableAction.UpdateRows
  
<code>TableAction.UpdateRows(<b>table</b> as table, <b>columnUpdates</b> as list) as action</code>  
## About  
Creates an action to update the rows in <code>table</code> based on the set of operations in <code>columnUpdates</code>. The action returns a table containing the updated rows as they appear in <code>table</code> after the action executes. The value of <code>columnUpdates</code> may be a single <code>{columnName, columnFunction}</code> pair or a list of such pairs. For each pair, the <code>columnFunction</code> is the function to apply to a row to compute the new value for the <code>columnName</code> column for that row. To update a subset of the rows in <code>table</code>, use <code>Table.SelectRows</code> to apply a filter to <code>table</code> before using <code>TableAction.UpdateRows</code>. The function raises an evaluation error if <code>table</code> is not updatable or if any of the operations in <code>columnUpdates</code> are incompatible with <code>table</code>. The action raises an execution error if the operation fails.   
  
<b>NOTE:</b> <code>table</code> may be left in a partially updated state if an execution error occurs.  
