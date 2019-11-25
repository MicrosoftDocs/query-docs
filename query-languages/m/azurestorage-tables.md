---
title: "AzureStorage.Tables | Microsoft Docs"
ms.date: 12/12/2018
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# AzureStorage.Tables

## Syntax

<pre>
AzureStorage.Tables(<b>account</b> as text) as table
</pre>

## About

Returns a navigational table containing a row for each table found at the account URL, `account`, from an Azure storage vault. Each row contains a link to the azure table.
