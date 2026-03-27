---
description: "Learn more about: Table.ViewError"
title: "Table.ViewError"
ms.subservice: m-source
ms.topic: reference
---

# Table.ViewError

## Syntax

<pre>
Table.ViewError(<b>errorRecord</b> as record) as record
</pre>

## About

Creates a modified error record from [`errorRecord`](error-record.md) which won't trigger a fallback when raised by a handler defined on a view (via [`Table.View`](table-view.md)).
