---
description: "Learn more about: AzureStorage.DataLake"
title: "AzureStorage.DataLake"
ms.topic: reference
ms.subservice: m-source
---
# AzureStorage.DataLake

## Syntax

<pre>
AzureStorage.DataLake(<b>endpoint</b> as text, optional <b>options</b> as nullable record) as table
</pre>

## About

Returns a navigational table containing the documents found in the specified container and its subfolders at the account URL, `endpoint`, from an Azure Data Lake Storage filesystem. `options` may be specified to control the following options:

* `BlockSize`: The number of bytes to read before waiting on the data consumer. The default value is 4 MB.
* `RequestSize`: The number of bytes to try to read in a single HTTP request to the server. The default value is 4 MB.
* `ConcurrentRequests`: The ConcurrentRequests option supports faster download of data by specifying the number of requests to be made in parallel, at the cost of memory utilization. The memory required is (ConcurrentRequest * RequestSize). The default value is 16.
* `HierarchicalNavigation`: A logical (true/false) that controls whether the files are returned in a tree-like directory view or in a flat list. The default value is false.
