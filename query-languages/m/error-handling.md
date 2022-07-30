---
description: "Learn more about: Error handling functions"
title: "Error handling functions"
ms.date: 5/16/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Error handling functions

These functions can be used to trace or construct errors.

|Name|Description|
|------------|---------------|
|[Diagnostics.ActivityId](diagnostics-activityid.md)|Returns an opaque identifier for the currently-running evaluation.|
|[Diagnostics.Trace](diagnostics-trace.md)|Writes a trace message, if tracing is enabled, and returns value.|
|[Error.Record](error-record.md)|Returns a record containing fields **Reason**, **Message**, and **Detail** set to the provided values. The record can be used to raise or throw an error.|
