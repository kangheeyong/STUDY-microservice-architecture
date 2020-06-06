from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class DownloadConfig:
    cache_dir: Optional[str] = None
    force_download: bool = False
    resume_download: bool = False
    local_files_only: bool = False
    proxies: Optional[dict] = None
    user_agent: Optional[str] = None
    extract_compressed_file: bool = False
    force_extract: bool = False

