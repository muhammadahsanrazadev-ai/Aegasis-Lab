"""Dummy portrait files. Each contact gets a distinct local PNG, not a remote URL."""

import struct
import zlib
from pathlib import Path


AVATAR_DIR = Path(__file__).resolve().parent / "static" / "avatars"

# One face color per directory row, in seed order.
FACE_COLORS = (
    (91, 97, 246),
    (217, 119, 6),
    (190, 18, 60),
    (15, 118, 110),
    (29, 78, 216),
    (109, 40, 217),
    (3, 105, 161),
    (22, 163, 74),
    (180, 83, 9),
)


def avatar_filename(first_name, last_name):
    return "{0}-{1}.png".format(first_name, last_name).lower().replace(" ", "-")


def write_avatar(filename, color):
    AVATAR_DIR.mkdir(parents=True, exist_ok=True)
    path = AVATAR_DIR / filename
    if not path.exists():
        path.write_bytes(_png(color))
    return filename


def _png(color):
    width = height = 96
    red, green, blue = color
    raw = bytearray()
    for y in range(height):
        raw.append(0)
        for x in range(width):
            distance = (x - 47) ** 2 + (y - 40) ** 2
            shoulder = (x - 47) ** 2 + (y - 92) ** 2
            if distance <= 22 ** 2:
                raw.extend((red, green, blue))
            elif shoulder <= 38 ** 2 and y > 58:
                raw.extend((max(red - 40, 0), max(green - 40, 0), max(blue - 40, 0)))
            else:
                raw.extend((243, 244, 248))
    compressed = zlib.compress(bytes(raw), 9)

    def chunk(tag, data):
        return (
            struct.pack(">I", len(data))
            + tag
            + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        )

    header = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header) + chunk(b"IDAT", compressed) + chunk(b"IEND", b"")
