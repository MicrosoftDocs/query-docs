---
description: "Learn more about: Binary.ViewError"
title: "Binary.ViewError | Microsoft Docs"
ms.date: 7/19/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo
---
# Binary.ViewError

## Syntax

<pre>
Binary.ViewError(<b>errorRecord</b> as record) as record
</pre>

## About

Creates a modified error record from `errorRecord` which won't trigger a fallback when thrown by a handler defined on a view (via [Binary.View](binary-view.md)).
