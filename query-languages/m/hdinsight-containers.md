---
description: "Learn more about: HdInsight.Containers"
title: "HdInsight.Containers"
ms.subservice: m-source
---
# HdInsight.Containers

## Syntax

<pre>
HdInsight.Containers(<b>account</b> as text) as table
</pre>

## About

Returns a navigational table containing a row for each container found at the account URL, `account`, from an Azure storage vault. Each row contains a link to the container blobs.
