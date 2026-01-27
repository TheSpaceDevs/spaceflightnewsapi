# type: ignore

from logging import LogRecord

from json_log_formatter import JSONFormatter


class JSONFormatter(JSONFormatter):
    def json_record(self, message: str, extra: dict, record: LogRecord):
        extra.update({"level": record.levelname})
        return super().json_record(message, extra, record)
