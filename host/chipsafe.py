#!/usr/bin/env python3
"""MSA-ChipSafe: auditoría no destructiva de una placa ESP32.

No ejecuta comandos de escritura. La lectura completa de flash se deja para
una orden explícita posterior y siempre se guarda con SHA-256.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def ports() -> list[dict[str, str]]:
    try:
        from serial.tools import list_ports
    except ImportError:
        return []
    return [
        {"device": p.device, "description": p.description or "", "hwid": p.hwid or ""}
        for p in list_ports.comports()
    ]


def identify(device: str | None) -> dict:
    result = {"device": device, "tool": "unavailable", "output": ""}
    exe = shutil.which("esptool") or shutil.which("esptool.exe")
    if not exe:
        result["hint"] = "Instala esptool y pyserial para identificación por USB-UART."
        return result
    if not device:
        result["hint"] = "Indica --device COMx (Windows) o /dev/ttyUSBx."
        return result
    # chip_id es una consulta de lectura; nunca usa write_flash/erase_flash.
    cmd = [exe, "--port", device, "chip_id"]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
    result.update({"tool": "esptool", "returncode": proc.returncode,
                   "output": (proc.stdout + proc.stderr).strip()})
    return result


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description="Auditoría ESP32 de solo lectura")
    ap.add_argument("--device", help="COM4, /dev/ttyUSB0, etc.")
    ap.add_argument("--out", type=Path, default=Path("chipsafe-report.json"))
    ap.add_argument("--hash", type=Path, help="Calcula SHA-256 de una copia existente")
    args = ap.parse_args()
    report = {"tool": "MSA-ChipSafe", "timestamp": datetime.now(timezone.utc).isoformat(),
              "ports": ports(), "identification": identify(args.device)}
    if args.hash:
        report["file"] = {"path": str(args.hash), "bytes": args.hash.stat().st_size,
                           "sha256": sha256(args.hash)}
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
