---
description: "Learn more about: Error handling functions"
title: "Error handling functions"
ms.date: 11/15/2023
ms.custom: "nonautomated-date"
---
# Error handling functions

These functions can be used to trace or construct errors.

|Name|Description|
|------------|---------------|
|[Diagnostics.ActivityId](diagnostics-activityid.md)|Returns an opaque identifier for the currently-running evaluation.|
|[Diagnostics.CorrelationId](diagnostics-correlationid.md)|Returns an opaque identifier to correlate incoming requests with outgoing ones.|
|[Diagnostics.Trace](diagnostics-trace.md)|Writes a trace message, if tracing is enabled, and returns value.|
|[Error.Record](error-record.md)|Returns a record containing fields **Reason**, **Message**, and **Detail** set to the provided values. The record can be used to raise or throw an error.|
