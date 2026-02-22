# Advanced HTTP Analyzer

A multi-threaded HTTP server built using Python sockets.

## Features

- Multi-threaded request handling
- Live request statistics
- Path-based analytics
- 403 Forbidden path blocking
- JSON log export
- File-based logging system

## Endpoints

| Endpoint | Description |
|----------|------------|
| `/` | Basic response |
| `/stats` | Shows live request statistics |
| `/logs` | Returns JSON logs |
| `/admin` | Blocked (403 Forbidden) |

## How to Run

```bash
python analyzer_server.py