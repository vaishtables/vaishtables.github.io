sort words.md \
  | awk '!seen[$0]++' \
  | awk '{ print length, $0 }' \
  | sort -n -k1,1 -k2 \
  | cut -d' ' -f2- \
  > words.txt
