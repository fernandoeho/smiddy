# API Response Envelope

All API responses use a consistent `{ success, data, error }` envelope.

## Pattern

```json
// Success
{ "success": true, "data": { ... } }

// Error
{ "success": false, "error": { "code": "AUTH_001", "message": "Token expired." } }
```

## Rules

- Always wrap responses in the envelope — never return raw data or raw errors
- Success responses include `data` and omit `error`
- Error responses include `error` with both `code` and `message`; omit `data`
- Log the full error server-side; return only the safe `message` to the client
- Error codes follow `DOMAIN_NNN` format (e.g. `AUTH_001`, `DB_002`, `VAL_003`)

## Why

Frontend can always check `success` first, then branch on `code` without inspecting message text. Consistent codes make client-side error handling and alerting rules predictable across every endpoint.

## Exceptions

None — apply in all cases.
