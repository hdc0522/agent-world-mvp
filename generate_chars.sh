#!/bin/bash
# 批量生成192个角色立绘
# 16 MBTI × 2 性别 × 6 年龄段

DIR="/home/hdc0522/agent-world-mvp/characters"
mkdir -p "$DIR"

TYPES=("INTJ" "INTP" "ENTJ" "ENTP" "INFJ" "INFP" "ENFJ" "ENFP" "ISTJ" "ISFJ" "ESTJ" "ESFJ" "ISTP" "ISFP" "ESTP" "ESFP")
GENDERS=("boy" "girl")
AGES=("toddler" "child" "teenager" "young_adult" "adult" "elderly")
AGE_PROMPTS=(
  "toddler, 3 years old, cute round face, small body, diaper or simple clothes"
  "child, 8 years old, lively expression, school uniform or casual clothes"
  "teenager, 16 years old, slender build, casual modern clothes"
  "young adult, 22 years old, confident posture, business casual or trendy outfit"
  "adult, 30 years old, mature appearance, professional or elegant attire"
  "elderly, 65 years old, wise face with wrinkles, formal traditional clothing"
)

STYLE="anime style, clean white background, simple outfit, full body portrait, character design sheet, front facing, consistent art style across all characters"

generate() {
  local type=$1
  local gender=$2
  local age_idx=$3
  local outfile="${DIR}/${type,,}_${gender}_age${age_idx}.png"
  
  if [ -f "$outfile" ]; then
    echo "SKIP: $outfile exists"
    return
  fi
  
  local age_prompt="${AGES[$age_idx]}"
  local extra_prompt="${AGE_PROMPTS[$age_idx]}"
  
  local prompt="${type} ${gender}, ${extra_prompt}, ${STYLE}"
  local encoded=$(python3 -c "import urllib.parse; print(urllib.parse.quote_plus('$prompt'))")
  local url="https://image.pollinations.ai/prompt/${encoded}?width=400&height=600&seed=$RANDOM&nologo=true"
  
  echo "Generating: $outfile"
  curl -L -o "$outfile" -A "Mozilla/5.0" --max-time 120 "$url" 2>/dev/null
  
  local size=$(stat -c%s "$outfile" 2>/dev/null || echo 0)
  if [ "$size" -gt 5000 ]; then
    echo "OK: $outfile (${size}B)"
  else
    echo "FAIL: $outfile"
    rm -f "$outfile"
  fi
  
  sleep 2
}

# 循环生成所有组合
for type in "${TYPES[@]}"; do
  for gender in "${GENDERS[@]}"; do
    for age_idx in {0..5}; do
      generate "$type" "$gender" $age_idx
    done
  done
done

echo "=== ALL DONE ==="
ls -la "$DIR" | wc -l
