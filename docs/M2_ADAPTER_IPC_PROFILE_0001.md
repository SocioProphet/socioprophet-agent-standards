# M2 Adapter IPC Profile 0001

Status: draft normative profile.

## Purpose

This profile defines the required adapter IPC contract between agents and their execution/runner environments. This contract standardizes the message exchange structure and is required for agents conforming to the AgentOS spec.

## Required fields

Each M2 adapter should declare:
- `adapter_ref`
- `message_type`
- `message_payload`
- `status_code`
- `error_code`

## IPC Operations

1. **Lock Validate**: Ensures agent execution locks are valid before proceeding with tasks.
2. **Task Run**: Defines the structure for invoking tasks via the IPC layer.
3. **Deps Inventory**: A required field for tracking dependencies during task execution.
4. **Info**: Basic info operation to confirm readiness and agent health.
5. **Error Handling**: Specifying error handling structures in case of IPC failure.

## IPC Message Example

```json
{
  "adapter_ref": "task-runner-01",
  "message_type": "task_run",
  "message_payload": {
    "task_id": "1234",
    "task_name": "backup_task"
  },
  "status_code": 200,
  "error_code": null
}
```
