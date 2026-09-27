#!/bin/sh
# WebP alongside every JPEG. No AVIF encoder on this machine; add avifenc and a
# third <source> if you have one.
cd "$(dirname "$0")/images" || exit 1
for f in *.jpg; do
  cwebp -quiet -q 76 "$f" -o "${f%.jpg}.webp"
done
