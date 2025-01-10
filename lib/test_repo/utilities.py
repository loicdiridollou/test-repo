"""Utilities module."""

import logging
from pathlib import Path

from test_repo.__version__ import __version__

log = logging.getLogger(__name__)


def configure_logger(
    log_name: str | None = None,
    log_path: Path | None = None,
    verbose: bool = False,
) -> Path | None:
    """Supply a path to a log file or log_name to write into default logs folder."""
    handlers: list[logging.Handler] = [logging.StreamHandler()]

    if log_path and log_name:
        raise Exception("Cannot set both path and log_name")
    if log_name:
        log_base = Path(".")

        if not log_base.exists():
            log_base.mkdir()
            log_base.chmod(0o1777)

        log_path = log_base / f"{log_name}.log"
        if not log_path.parent.exists():
            log_path.parent.mkdir(parents=True)

    if log_path:
        handlers.append(logging.FileHandler(log_path))

    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
        handlers=handlers,
        force=True,
    )

    if log_name:
        log.info("Running %s %s", log_name, __version__)

    if log_path:
        log.info("Writing logs to: %s", log_path)

    return log_path
