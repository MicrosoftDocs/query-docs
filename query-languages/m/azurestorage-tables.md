---
description: "Learn more about: AzureStorage.Tables"
title: "AzureStorage.Tables"
ms.date: 5/25/2021
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo
---
# AzureStorage.Tables

## Syntax

<pre>
AzureStorage.Tables(<b>account</b> as text, optional <b>options</b> as nullable record) as table
</pre>

## About

Returns a navigational table containing a row for each table found at the account URL, `account`, from an Azure storage vault. Each row contains a link to the azure table. An optional record parameter, `options`, may be provided to specify additional properties. The record can contain the following fields:

* `Timeout`: A duration that controls how long to wait before abandoning the request to the server. The default value is source-specific.
