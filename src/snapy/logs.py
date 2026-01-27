from logging import LogRecord

import json_log_formatter


class JSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message: str, extra: dict, record: LogRecord):
        extra.update({"level": record.levelname})
        return super().json_record(message, extra, record)
