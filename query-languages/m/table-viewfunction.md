---
title: "Table.ViewFunction | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ViewFunction

## Syntax

<pre>
Table.ViewFunction(<b>function</b> as function) as function
</pre>

## About
Creates a view function based on `function` that can be handled in a view created by `Table.View`. 

The `OnInvoke` handler of `Table.View` can be used to defined a handler for the view function. 

As with the handlers for built-in operations, if no `OnInvoke` handler is specified, or if it does not handle the view function, or if an error is raised by the handler, `function` is applied on top of the view. 

Please see the published documentation for a more complete description of `Table.View` and custom view functions.

