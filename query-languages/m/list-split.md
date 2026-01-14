---
description: "Learn more about: List.Split"
title: "List.Split"
ms.subservice: m-source
ms.topic: reference
---
# List.Split

## Syntax

<pre>
List.Split(<b>list</b> as list, <b>pageSize</b> as number) as list
</pre>

## About

Splits `list` into a list of lists where the first element of the output list is a list containing the first `pageSize` elements from the source list, the next element of the output list is a list containing the next `pageSize` elements from the source list, and so on.
