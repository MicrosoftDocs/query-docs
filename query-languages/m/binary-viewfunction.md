---
description: "Learn more about: Binary.ViewFunction"
title: "Binary.ViewFunction"
ms.subservice: m-source
---
# Binary.ViewFunction

## Syntax

<pre>
Binary.ViewFunction(<b>function</b> as function) as function
</pre>

## About

Creates a view function based on `function` that can be handled in a view created by [Binary.View](binary-view.md).

The `OnInvoke` handler of **Binary.View** can be used to define a handler for the view function.

As with the handlers for built-in operations, if no `OnInvoke` handler is specified, or if it does not handle the view function, or if an error is raised by the handler, `function` is applied on top of the view.

Refer to the published Power Query custom connector documentation for a more complete description of **Binary.View** and custom view functions.
