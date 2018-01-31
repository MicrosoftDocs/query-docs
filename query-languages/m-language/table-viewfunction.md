---
title: "Table.ViewFunction | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 50bc90e7-404f-40f4-8839-3e7999a76751
caps.latest.revision: 3
author: "MarkMcGeeAtAquent"
ms.author: "v-mamcge"
manager: "kfile"
---
# Table.ViewFunction
<code>Table.ViewFunction(<b>function</b> as function) as function</code>

## About
Creates a view function based on `function` that can be handled in a view created by `Table.View`. 

The `OnInvoke` handler of `Table.View` can be used to defined a handler for the view function. 

As with the handlers for built-in operations, if no `OnInvoke` handler is specified, or if it does not handle the view function, or if an error is raised by the handler, `function` is applied on top of the view. 

Please see the published documentation for a more complete description of `Table.View` and custom view functions.

