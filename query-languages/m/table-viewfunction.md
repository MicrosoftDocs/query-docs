---
description: "Learn more about: Table.ViewFunction"
title: "Table.ViewFunction"
---
# Table.ViewFunction

## Syntax

<pre>
Table.ViewFunction(<b>function</b> as function) as function
</pre>

## About

Creates a view function based on `function` that can be handled in a view created by [Table.View](/powerquery-m/table-view).

The `OnInvoke` handler of [Table.View](table-view.md) can be used to define a handler for the view function.

As with the handlers for built-in operations, if no `OnInvoke` handler is specified, or if it does not handle the view function, or if an error is raised by the handler, `function` is applied on top of the view.

Refer to the published [Power Query custom connector documentation](/power-query/samples/trippin/10-tableview1/readme#using-tableview) for a more complete description of **Table.View** and custom view functions.
