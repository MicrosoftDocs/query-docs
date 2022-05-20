---
description: "Learn more about: Table.ViewError"
title: "Table.ViewError | Microsoft Docs"
ms.date: 4/13/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.ViewError

## Syntax

<pre>
Table.ViewError(<b>errorRecord</b> as record) as record
</pre>

## About

Creates a modified error record from `errorRecord` which won't trigger a fallback when thrown by a handler defined on a view (via [Table.View](/powerquery-m/table-view)).
