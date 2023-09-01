---
description: "Learn more about: Table.ViewError"
title: "Table.ViewError"
---
# Table.ViewError

## Syntax

<pre>
Table.ViewError(<b>errorRecord</b> as record) as record
</pre>

## About

Creates a modified error record from `errorRecord` which won't trigger a fallback when thrown by a handler defined on a view (via [Table.View](/powerquery-m/table-view)).
